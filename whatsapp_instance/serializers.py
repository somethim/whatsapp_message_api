import asyncio
import time
from datetime import timedelta

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from user_data.models import Client

# Fetch all clients
clients = Client.objects.all()

# Initialize an empty list to store the phone numbers and messages
combo = []

# Iterate over all clients
for client in clients:
    try:
        # Get the phone number and message for each client
        phone_number = client.phone_number
        message = "Test MSG nga Arbi"  # Replace this with the actual message

        # Add the phone number and message to the combo list
        combo.append((phone_number, message))
    except ObjectDoesNotExist:
        print(f"Client with id {client.id} does not exist.")


async def send_message(driver, phone_number, message):
    driver.get(
        "https://web.whatsapp.com/send?phone=" + phone_number + "&text=" + message
    )
    await asyncio.sleep(5)  # Wait for the page to load

    try:
        # Simulate 'Enter' key press
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
    except NoSuchElementException:
        print("Failed to send message to", phone_number)


class MessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=1000, read_only=True)
    phone_number = serializers.CharField(max_length=1000, read_only=True)
    date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data: dict) -> dict:
        from user_data.models import Client

        client_id = self.context["request"].query_params.get("client_id")
        if client_id is not None:
            try:
                client_obj = Client.objects.get(id=client_id)
                validated_data["message"] = client_obj.message
                validated_data["phone_number"] = client_obj.phone_number
                if client_obj.next_meeting_date is not None:
                    validated_data["date"] = client_obj.next_meeting_date - timedelta(
                        days=1
                    )

                # Use a persistent Firefox profile
                profile = webdriver.FirefoxProfile(
                    "/home/arbikullakshi/.mozilla/firefox/a0er8uae.default-release"
                )

                # Set Firefox to run in headless mode
                options = Options()
                options.headless = True

                # Send the message using Selenium with Firefox
                driver = webdriver.Firefox(
                    executable_path="/usr/local/bin/geckodriver",
                    firefox_profile=profile,
                    options=options,
                )

                driver.get("http://web.whatsapp.com")
                time.sleep(10)  # Wait for the user to scan the QR code

                # Run the message sending process in the background
                loop = asyncio.get_event_loop()
                loop.run_until_complete(
                    send_message(
                        driver,
                        validated_data["phone_number"],
                        validated_data["message"],
                    )
                )

            except Client.DoesNotExist:
                raise serializers.ValidationError(
                    "Client with given id does not exist."
                )
        else:
            raise serializers.ValidationError("Client id must be provided.")

        return validated_data
