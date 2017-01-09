from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Start(Page):

    def vars_for_template(self):
      return {
        'participant_label': self.player.participant.label
      }


page_sequence = [
    Start
]
