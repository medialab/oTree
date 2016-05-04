# -*- coding: utf-8 -*-
"""Views for Trust game."""

from __future__ import division
from ._builtin import Page
from . import models
from .models import Constants
from django.utils.translation import ugettext_lazy as _


def vars_for_all_templates(self):
    """Provide global template variables."""
    return {'instructions': 'trust/Instructions.html', 'total_q': 1}


class ExperimentIntroduction(Page):
    """
    Page introducing the entire experiment.

    Assumes this is the first test.
    """

    form_model = models.Player
    form_fields = ['email']

    def vars_for_template(self):
        """Return variables for use in template."""
        return {
            'email_label': _(u'Email')
        }


class GamesIntroduction(Page):
    """Page introducing the games. Assumes this is the first test."""

    pass


class Introduction(Page):
    """Page introducing the Trust game."""

    template_name = 'global/Introduction.html'
    form_model = models.Player
    form_fields = ['total_time']

    def vars_for_template(self):
        """Local variables for the template."""
        return {'amount_allocated': Constants.amount_allocated}


class Simulation(Page):
    """Simulation page."""

    template_name = 'trust/Simulation.html'


class Send(Page):
    """Page where Player 1 sends money."""

    form_model = models.Group
    form_fields = ['sent_amount']

    def vars_for_template(self):
        """Return variables for use in template."""
        return {
            'amount_allocated': Constants.amount_allocated,
            'sent_amount_label': _(u'Please enter a number from 0 to 10')
        }

    def is_displayed(self):
        """Display rule stating 'Send' is displayed for Player 1 only."""
        return self.group.treatment()[:1] == 'A'


class SendBack(Page):
    """Page where Player 2 sends mony in return for possible P1 grants."""

    form_model = models.Group
    form_fields = [
        'sent_back_amount_0',
        'sent_back_amount_1',
        'sent_back_amount_2',
        'sent_back_amount_3',
        'sent_back_amount_4',
        'sent_back_amount_5',
        'sent_back_amount_6',
        'sent_back_amount_7',
        'sent_back_amount_8',
        'sent_back_amount_9',
        'sent_back_amount_10',
    ]

    def vars_for_template(self):
        """Return variables for use in template."""
        return {
            'sent_back_amount_0_label': _(
                u'If the other group members make an \
average contribution of 0'
            ),
            'sent_back_amount_1_label': _(
                u'If the other group members make an \
average contribution of 1'
            ),
            'sent_back_amount_2_label': _(
                u'If the other group members make an \
average contribution of 2'
            ),
            'sent_back_amount_3_label': _(
                u'If the other group members make an \
average contribution of 3'
            ),
            'sent_back_amount_4_label': _(
                u'If the other group members make an \
average contribution of 4'
            ),
            'sent_back_amount_5_label': _(
                u'If the other group members make an \
average contribution of 5'
            ),
            'sent_back_amount_6_label': _(
                u'If the other group members make an \
average contribution of 6'
            ),
            'sent_back_amount_7_label': _(
                u'If the other group members make an \
average contribution of 7'
            ),
            'sent_back_amount_8_label': _(
                u'If the other group members make an \
average contribution of 8'
            ),
            'sent_back_amount_9_label': _(
                u'If the other group members make an \
average contribution of 9'
            ),
            'sent_back_amount_10_label': _(
                u'If the other group members make an \
average contribution of 10'
            ),
        }

    def is_displayed(self):
        """Display rule stating 'SendBack' appears for Player B only."""
        return self.group.treatment()[:1] == 'B'


class EndGame(Page):
    """End of the game."""

    form_model = models.Player
    form_fields = ['total_time']

    def vars_for_template(self):
        """Make data available in template."""
        return {'start_time': self.player.total_time}


page_sequence = [
    ExperimentIntroduction,
    GamesIntroduction,
    Introduction,
    Simulation,
    Send,
    SendBack,
    EndGame
]
