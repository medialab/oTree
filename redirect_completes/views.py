from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Redirect(Page):

    def vars_for_template(self):
        return {
            'redirect': (
                'redirects' in self.session.vars and
                self.session.vars['redirects']['complete'] or
                'http://sciences-po.fr'
            ),
            'label': self.participant.label
        }


page_sequence = [Redirect]
