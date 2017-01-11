from django.core.management.base import BaseCommand
from django.core.management import call_command
from settings import BASE_DIR
import subprocess


class Command(BaseCommand):
    """Deploy an instance by pushing to the git branch relevant to desired country/locale."""

    help = 'Deploy an instance by pushing to the git branch relevant to desired country/locale.'

    def add_arguments(self, parser):
        """Add arguments."""
        parser.add_argument('locale', metavar='locale', help='A 2-character locale code (i.e. \'en\')')

    def handle(self, *args, **options):
        """Run command."""
        script = BASE_DIR + '/_bin/bash_scripts/deploy' + options['locale'] + '.sh'
        subprocess.call([script], shell=True)
