from typing import Any

from django.contrib.auth.management.commands.createsuperuser import (
    Command as BaseCommand,
)

from user_data.models import Company


class Command(BaseCommand):
    def add_arguments(self, parser: Any) -> None:
        super().add_arguments(parser)
        parser.add_argument(
            "--company-name",
            dest="company_name",
            type=str,
            help="Specifies the company name of the super user.",
        )

    def handle(self, *args: Any, **options: Any) -> None:
        company_name = options.get("company_name")

        if company_name:
            try:
                company, created = Company.objects.get_or_create(name=company_name)
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f"Created new company {company.name}.")
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS(f"Use existing company {company.name}")
                    )

                options["company_id"] = company.id
                super().handle(*args, **options)
            except Exception as e:
                self.stderr.write(
                    self.style.ERROR(f"Error creating and assigning related model: {e}")
                )
        else:
            companies = Company.objects.all()
            for i, company in enumerate(companies, start=1):
                self.stdout.write(f"{i}. {company.name}")
            company_input = input(
                "Select a company by number or enter a new company name: "
            )
            try:
                company_number = int(company_input)
                if 1 <= company_number <= len(companies):
                    company = companies[company_number - 1]
                    self.stdout.write(
                        self.style.SUCCESS(f"Use existing company {company.name}")
                    )
                else:
                    raise ValueError
            except ValueError:
                company_name = company_input
                company, created = Company.objects.get_or_create(name=company_name)
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f"Created new company {company.name}.")
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS(f"Use existing company {company.name}")
                    )
            options["company_id"] = company.id
            super().handle(*args, **options)
