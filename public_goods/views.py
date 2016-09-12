# -*- coding: utf-8 -*-
"""Views for Public Goods."""

from __future__ import division
from . import models
from ._builtin import Page
from otree.common import Currency
from .models import Constants
from django.utils.translation import ugettext_lazy as _


def vars_for_all_templates(self):
    """Provide global template variables."""
    return {
        'lang': self.session.vars['lang']
    }


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

    def vars_for_template(self):
        max = {'fr': 10, 'en': 10, 'ko': 12000}
        step = {'fr': 1, 'en': 1, 'ko': 1000}
        return {
            'max': max[self.session.vars['lang']],
            'step': step[self.session.vars['lang']]
        }


class DecisionInstructions(Page):
    """Decision instructions page for Public Goods."""

    pass


class Contribute(Page):
    """Participant A's contribution."""

    form_model = models.Player
    form_fields = ['contribution']

    timeout_submission = {'contribution': Currency(Constants.endowment / 2)}

    def vars_for_template(self):
        amount = {
            'fr': _(u'10 euros'),
            'en': _(u'$10'),
            'ko': _(u'12.000 Won')
        }
        return {
            'amount': amount[self.session.vars['lang']]
        }


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
        contribution_back_0_label = {
            'fr': _(u'If on average, each of the other \
    group members contributes 0 euro:'),
            'en': _(u'If on average, each of the other \
    group members contributes 0 euro:'),
            'ko': _(u'If on average, each of the other \
    group members contributes 0 Won:')
        }

        contribution_back_1_label = {
            'fr': _(u'If on average, each of the other \
    group members contributes 1 euro:'),
            'en': _(u'If on average, each of the other \
    group members contributes 1 euro:'),
            'ko': _(u'If on average, each of the other \
    group members contributes 1.200 Won Won:')
        }

        contribution_back_2_label = {
            'fr': _(u'If on average, each of the other \
    group members contributes 2 euros:'),
            'en': _(u'If on average, each of the other \
    group members contributes 2 euros:'),
            'ko': _(u'If on average, each of the other \
    group members contributes 2.400 Won:')
        }

        contribution_back_3_label = {
            'fr': _(u'If on average, each of the other \
    group members contributes 3 euros:'),
            'en': _(u'If on average, each of the other \
    group members contributes 3 euros:'),
            'ko': _(u'If on average, each of the other \
    group members contributes 3.600 Won:')
        }

        contribution_back_4_label = {
            'fr': _(u'If on average, each of the other \
    group members contributes 4 euros:'),
            'en': _(u'If on average, each of the other \
    group members contributes 4 euros:'),
            'ko': _(u'If on average, each of the other \
    group members contributes 4.800 Won:')
        }

        contribution_back_5_label = {
            'fr': _(u'If on average, each of the other \
    group members contributes 5 euros:'),
            'en': _(u'If on average, each of the other \
    group members contributes 5 euros:'),
            'ko': _(u'If on average, each of the other \
    group members contributes 6.000 Won:')
        }

        contribution_back_6_label = {
            'fr': _(u'If on average, each of the other \
    group members contributes 6 euros:'),
            'en': _(u'If on average, each of the other \
    group members contributes 6 euros:'),
            'ko': _(u'If on average, each of the other \
    group members contributes 7.200 Won:')
        }

        contribution_back_7_label = {
            'fr': _(u'If on average, each of the other \
    group members contributes 7 euros:'),
            'en': _(u'If on average, each of the other \
    group members contributes 7 euros:'),
            'ko': _(u'If on average, each of the other \
    group members contributes 8.400 Won:')
        }

        contribution_back_8_label = {
            'fr': _(u'If on average, each of the other \
    group members contributes 8 euros:'),
            'en': _(u'If on average, each of the other \
    group members contributes 8 euros:'),
            'ko': _(u'If on average, each of the other \
    group members contributes 9.600 Won:')
        }

        contribution_back_9_label = {
            'fr': _(u'If on average, each of the other \
    group members contributes 9 euros:'),
            'en': _(u'If on average, each of the other \
    group members contributes 9 euros:'),
            'ko': _(u'If on average, each of the other \
    group members contributes 10.800 Won:')
        }

        contribution_back_10_label = {
            'fr': _(u'If on average, each of the other \
    group members contributes 10 euros:'),
            'en': _(u'If on average, each of the other \
    group members contributes 10 euros:'),
            'ko': _(u'If on average, each of the other \
    group members contributes 12.000 Won:')
        }

        return {
            'contribution_back_0_label': contribution_back_0_label[
                self.session.vars['lang']
            ],
            'contribution_back_1_label': contribution_back_1_label[
                self.session.vars['lang']
            ],
            'contribution_back_2_label': contribution_back_2_label[
                self.session.vars['lang']
            ],
            'contribution_back_3_label': contribution_back_3_label[
                self.session.vars['lang']
            ],
            'contribution_back_4_label': contribution_back_4_label[
                self.session.vars['lang']
            ],
            'contribution_back_5_label': contribution_back_5_label[
                self.session.vars['lang']
            ],
            'contribution_back_6_label': contribution_back_6_label[
                self.session.vars['lang']
            ],
            'contribution_back_7_label': contribution_back_7_label[
                self.session.vars['lang']
            ],
            'contribution_back_8_label': contribution_back_8_label[
                self.session.vars['lang']
            ],
            'contribution_back_9_label': contribution_back_9_label[
                self.session.vars['lang']
            ],
            'contribution_back_10_label': contribution_back_10_label[
                self.session.vars['lang']
            ],
        }


page_sequence = [
    Introduction,
    Simulation,
    Contribute,
    ContributeBack,
    EndGame
]
