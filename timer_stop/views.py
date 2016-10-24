from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Stop(Page):

    form_model = models.Player
    form_fields = ['epoch', 'global_time_in_seconds']

    def vars_for_template(self):
        self.participant.vars['global_time_stop'] = int(time.time())
        return {
            'global_time_start': self.participant.vars.get('global_time_start'),
            'global_time_stop': self.participant.vars.get('global_time_stop')
        }


page_sequence = [
    Stop
]
