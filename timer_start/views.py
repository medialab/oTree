from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Start(Page):

    def before_next_page(self):
        """Store start time to be used at the end of the XP."""
        self.player.epoch = int(time.time())
        self.participant.vars['global_time_start'] = int(time.time())


page_sequence = [
    Start
]
