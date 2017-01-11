from django.core.management.base import BaseCommand
from django.core.management import call_command
from settings import BASE_DIR
import subprocess


class Command(BaseCommand):
    """Run the (deprecated) IAT exporter Python script on a CSV file."""

    help = 'Run the (deprecated) IAT exporter Python script on a CSV file.'

    def add_arguments(self, parser):
        """Add arguments."""
        parser.add_argument('file', metavar='file', help='The CSV file extracted from oTree')

    def handle(self, *args, **options):
        """Run command."""
        script = 'python3 ' + BASE_DIR + '/_bin/old_iat_exporter.py ' + options['file']
        subprocess.call([script], shell=True)
