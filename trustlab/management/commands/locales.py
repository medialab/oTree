from django.core.management.base import BaseCommand
from django.core.management import call_command
from settings import BASE_DIR
from time import sleep
import subprocess


class Command(BaseCommand):
    """Batch application of the makemessages/compilemessages command."""

    help = 'Batch application of the makemessages/compilemessages commands.'

    def add_arguments(self, parser):
        """Add arguments."""
        parser.add_argument('command', metavar='command', help='Either make or compile')

    def handle(self, *args, **options):
        """Run command."""
        script = BASE_DIR + '/_bin/bash_scripts/' + options['command'] + 'messages.sh'
        subprocess.call([script], shell=True)
