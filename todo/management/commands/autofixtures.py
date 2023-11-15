from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata", "todo_address.json")
        call_command("loaddata", "todo_country.json")
        call_command("loaddata", "todo_country_attribute.json")
        call_command("loaddata", "todo_user.json")
        call_command("loaddata", "todo_todo.json")

# Command
# python3 manage.py autofixtures
