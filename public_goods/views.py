# -*- coding: utf-8 -*-
"""Views for Public Goods."""

from __future__ import division
from . import models
from ._builtin import Page
from otree.common import Currency
from .models import Constants
from django.utils.translation import ugettext_lazy as _


class Introduction(Page):
    """Introduction for Public Goods."""

    form_model = models.Player
    form_fields = ['total_time']


class EndGame(Page):
    """End page for Public Goods."""

    form_model = models.Player
    form_fields = ['total_time']

    def vars_for_template(self):
        """Make data available in template."""
        return {'start_time': self.player.total_time}


class Simulation(Page):
    """Simulation for Public Goods."""

    pass


class DecisionInstructions(Page):
    """Decision instructions page for Public Goods."""

    pass


class Contribute(Page):
    """Participant A's contribution."""

    form_model = models.Player
    form_fields = ['contribution']

    timeout_submission = {'contribution': Currency(Constants.endowment / 2)}


class ContributeBack(Page):
    """Participant B's contribution."""

    form_model = models.Player
    form_fields = [
        'contribution_back_0',
        'contribution_back_1',
        'contribution_back_2',
        'contribution_back_3',
        'contribution_back_4',
        'contribution_back_5',
        'contribution_back_6',
        'contribution_back_7',
        'contribution_back_8',
        'contribution_back_9',
        'contribution_back_10'
    ]

    def vars_for_template(self):
        """Return variables available for template."""
        return {
            'contribution_back_0_label': _(u'If the other group members make an \
average contribution of 0:'),
            'contribution_back_1_label': _(u'If the other group members make an \
average contribution of 1:'),
            'contribution_back_2_label': _(u'If the other group members make an \
average contribution of 2:'),
            'contribution_back_3_label': _(u'If the other group members make an \
average contribution of 3:'),
            'contribution_back_4_label': _(u'If the other group members make an \
average contribution of 4:'),
            'contribution_back_5_label': _(u'If the other group members make an \
average contribution of 5:'),
            'contribution_back_6_label': _(u'If the other group members make an \
average contribution of 6:'),
            'contribution_back_7_label': _(u'If the other group members make an \
average contribution of 7:'),
            'contribution_back_8_label': _(u'If the other group members make an \
average contribution of 8:'),
            'contribution_back_9_label': _(u'If the other group members make an \
average contribution of 9:'),
            'contribution_back_10_label': _(u'If the other group members make an \
average contribution of 10:'),
        }


page_sequence = [
    Introduction,
    Simulation,
    DecisionInstructions,
    Contribute,
    ContributeBack,
    EndGame
]
