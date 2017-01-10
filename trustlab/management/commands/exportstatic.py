from django.core.management.base import BaseCommand
from django.core.management import call_command
from settings import BASE_DIR
from time import sleep
import subprocess


class Command(BaseCommand):
  """Command to copy exports of sims before running collectstatic."""

  help = 'Copy exported simulations into static files directory before running "collectstatic" command.'

  def handle(self, *args, **options):
    """Runs command."""
    subprocess.call([BASE_DIR + '/_bin/bash_scripts/copysims.sh'], shell=True)
    call_command('collectstatic')
