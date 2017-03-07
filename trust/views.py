# -*- coding: utf-8 -*-
"""Views for Trust game."""

from ._builtin import Page
from . import models
from .models import amount_allocated
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language
from otree.api import Currency


def vars_for_all_templates(self):
    """Provide global template variables."""
    return {
        'instructions': 'trust/Instructions.html',
        'lang': get_language(),
        'amount_allocated': Currency(amount_allocated)
    }


class Introduction(Page):
    """Page introducing the Trust game."""

    template_name = 'global/Introduction.html'


class Simulation(Page):
    """Simulation page."""

    template_name = 'trust/Simulation.html'

    def vars_for_template(self):
        """Get vars for template."""
        max = {'fr': 10, 'en': 10, 'sl': 10, 'ko': 12000}
        step = {'fr': 1, 'en': 1, 'sl': 10, 'ko': 1000}
        return {
            'max': max[self.session.vars['lang']],
            'step': step[self.session.vars['lang']]
        }


class Send(Page):
    """Page where Player 1 sends money."""

    form_model = models.Player
    form_fields = ['sent_amount']

    def vars_for_template(self):
        """Return variables for use in template."""
        sent_amount_label = {
            'fr': _(u'Please enter a number from 0 to 10'),
            'en': _(u'Please enter a number from 0 to 10'),
            'sl': _(u'Please enter a number from 0 to 10'),
            'ko': _(u'Please enter a number from 0 to 12.000')
        }

        return {
            'sent_amount_label': sent_amount_label[self.session.vars['lang']]
        }

    def is_displayed(self):
        """Display rule stating 'Send' is displayed for Player 1 only."""
        return self.player.treatment()[:1] == 'A'


class SendContinued(Page):

    form_model = models.Player
    form_fields = ['expected_return_from_b']

    def vars_for_template(self):
        received_by_b = {
            'fr': _(u'15 euros'),
            'en': _(u'15 euros'),
            'sl': _(u'15 euros'),
            'ko': _(u'18.000 Won')
        }

        total_budget_b = {
            'fr': {'string': _(u'25 euros'), 'integer': 25},
            'en': {'string': _(u'25 euros'), 'integer': 25},
            'sl': {'string': _(u'25 euros'), 'integer': 25},
            'ko': {'string': _(u'30.000 Won'), 'integer': 30000},
        }

        return {
            'received_by_b': received_by_b[self.session.vars['lang']],
            'total_budget_b_str': total_budget_b[self.session.vars['lang']]['string'],
            'total_budget_b_int': total_budget_b[self.session.vars['lang']]['integer']
        }


class SendBack(Page):
    """Page where Player 2 sends mony in return for possible P1 grants."""

    form_model = models.Player
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
        sent_back_amount_0_label = {
            'fr': _(
                u'If Participant A sends you €0 (your total endowment is now €10). How much will you send back to Participant A:'
            ),
            'en': _(
                u'If Participant A sends you €0 (your total endowment is now €10). How much will you send back to Participant A:'
            ),
            'sl': _(
                u'If Participant A sends you €0 (your total endowment is now €10). How much will you send back to Participant A:'
            ),
            'ko': _(
                u'If Participant A sends you 0 Won (you receive 0 Won × 3 = 0 Won). How much will you send back to Participant A:'
            ),
        }

        sent_back_amount_1_label = {
            'fr': _(
                u'If Participant A sends you €1 (your total endowment is now €13). How much will you send back to Participant A:'
            ),
            'en': _(
                u'If Participant A sends you €1 (your total endowment is now €13). How much will you send back to Participant A:'
            ),
            'sl': _(
                u'If Participant A sends you €1 (your total endowment is now €13). How much will you send back to Participant A:'
            ),
            'ko': _(
                u'If Participant A sends you 1.200 Won (you receive 1.200 Won × 3 = 3.600 Won). How much will you send back to Participant A:'
            ),
        }

        sent_back_amount_2_label = {
            'fr': _(
                u'If Participant A sends you €2 (your total endowment is now €16). How much will you send back to Participant A:'
            ),
            'en': _(
                u'If Participant A sends you €2 (your total endowment is now €16). How much will you send back to Participant A:'
            ),
            'sl': _(
                u'If Participant A sends you €2 (your total endowment is now €16). How much will you send back to Participant A:'
            ),
            'ko': _(
                u'If Participant A sends you 2.400 Won (you receive 2.400 Won × 3 = 7.200 Won). How much will you send back to Participant A:'
            ),
        }

        sent_back_amount_3_label = {
            'fr': _(
                u'If Participant A sends you €3 (your total endowment is now €19). How much will you send back to Participant A:'
            ),
            'en': _(
                u'If Participant A sends you €3 (your total endowment is now €19). How much will you send back to Participant A:'
            ),
            'sl': _(
                u'If Participant A sends you €3 (your total endowment is now €19). How much will you send back to Participant A:'
            ),
            'ko': _(
                u'If Participant A sends you 3.600 Won (you receive 3.600 Won × 3 = 10.800 Won). How much will you send back to Participant A:'
            ),
        }

        sent_back_amount_4_label = {
            'fr': _(
                u'If Participant A sends you €4 (your total endowment is now €22). How much will you send back to Participant A:'
            ),
            'en': _(
                u'If Participant A sends you €4 (your total endowment is now €22). How much will you send back to Participant A:'
            ),
            'sl': _(
                u'If Participant A sends you €4 (your total endowment is now €22). How much will you send back to Participant A:'
            ),
            'ko': _(
                u'If Participant A sends you 4.800 Won (you receive 4.800 Won × 3 = 14.400 Won). How much will you send back to Participant A:'
            ),
        }

        sent_back_amount_5_label = {
            'fr': _(
                u'If Participant A sends you €5 (your total endowment is now €25). How much will you send back to Participant A:'
            ),
            'en': _(
                u'If Participant A sends you €5 (your total endowment is now €25). How much will you send back to Participant A:'
            ),
            'sl': _(
                u'If Participant A sends you €5 (your total endowment is now €25). How much will you send back to Participant A:'
            ),
            'ko': _(
                u'If Participant A sends you 6.000 Won (you receive 6.000 Won × 3 = 18.000 Won). How much will you send back to Participant A:'
            ),
        }

        sent_back_amount_6_label = {
            'fr': _(
                u'If Participant A sends you €6 (your total endowment is now €28). How much will you send back to Participant A:'
            ),
            'en': _(
                u'If Participant A sends you €6 (your total endowment is now €28). How much will you send back to Participant A:'
            ),
            'sl': _(
                u'If Participant A sends you €6 (your total endowment is now €28). How much will you send back to Participant A:'
            ),
            'ko': _(
                u'If Participant A sends you 7.200 Won (you receive 7.200 Won × 3 = 21.600 Won). How much will you send back to Participant A:'
            ),
        }

        sent_back_amount_7_label = {
            'fr': _(
                u'If Participant A sends you €7 (your total endowment is now €31). How much will you send back to Participant A:'
            ),
            'en': _(
                u'If Participant A sends you €7 (your total endowment is now €31). How much will you send back to Participant A:'
            ),
            'sl': _(
                u'If Participant A sends you €7 (your total endowment is now €31). How much will you send back to Participant A:'
            ),
            'ko': _(
                u'If Participant A sends you 8.400 Won (you receive 8.400 Won × 3 = 25.200 Won). How much will you send back to Participant A:'
            ),
        }

        sent_back_amount_8_label = {
            'fr': _(
                u'If Participant A sends you €8 (your total endowment is now €34). How much will you send back to Participant A:'
            ),
            'en': _(
                u'If Participant A sends you €8 (your total endowment is now €34). How much will you send back to Participant A:'
            ),
            'sl': _(
                u'If Participant A sends you €8 (your total endowment is now €34). How much will you send back to Participant A:'
            ),
            'ko': _(
                u'If Participant A sends you 9.600 Won (you receive 9.600 Won × 3 = 28.800 Won). How much will you send back to Participant A:'
            ),
        }

        sent_back_amount_9_label = {
            'fr': _(
                u'If Participant A sends you €9 (your total endowment is now €37). How much will you send back to Participant A:'
            ),
            'en': _(
                u'If Participant A sends you €9 (your total endowment is now €37). How much will you send back to Participant A:'
            ),
            'sl': _(
                u'If Participant A sends you €9 (your total endowment is now €37). How much will you send back to Participant A:'
            ),
            'ko': _(
                u'If Participant A sends you 10.800 Won (you receive 10.800 Won × 3 = 32.400 Won). How much will you send back to Participant A:'
            ),
        }

        sent_back_amount_10_label = {
            'fr': _(
                u'If Participant A sends you €10 (your total endowment is now €40). How much will you send back to Participant A:'
            ),
            'en': _(
                u'If Participant A sends you €10 (your total endowment is now €40). How much will you send back to Participant A:'
            ),
            'sl': _(
                u'If Participant A sends you €10 (your total endowment is now €40). How much will you send back to Participant A:'
            ),
            'ko': _(
                u'If Participant A sends you 12.000 Won (you receive 12.000 Won × 3 = 36.000 Won). How much will you send back to Participant A:'
            ),
        }

        return {
            'sent_back_amount_0_label': (
                sent_back_amount_0_label[self.session.vars['lang']]
            ),
            'sent_back_amount_1_label': (
                sent_back_amount_1_label[self.session.vars['lang']]
            ),
            'sent_back_amount_2_label': (
                sent_back_amount_2_label[self.session.vars['lang']]
            ),
            'sent_back_amount_3_label': (
                sent_back_amount_3_label[self.session.vars['lang']]
            ),
            'sent_back_amount_4_label': (
                sent_back_amount_4_label[self.session.vars['lang']]
            ),
            'sent_back_amount_5_label': (
                sent_back_amount_5_label[self.session.vars['lang']]
            ),
            'sent_back_amount_6_label': (
                sent_back_amount_6_label[self.session.vars['lang']]
            ),
            'sent_back_amount_7_label': (
                sent_back_amount_7_label[self.session.vars['lang']]
            ),
            'sent_back_amount_8_label': (
                sent_back_amount_8_label[self.session.vars['lang']]
            ),
            'sent_back_amount_9_label': (
                sent_back_amount_9_label[self.session.vars['lang']]
            ),
            'sent_back_amount_10_label': (
                sent_back_amount_10_label[self.session.vars['lang']]
            )
        }


class EndGame(Page):
    """End of the game."""

    pass


page_sequence = [
    Introduction,
    Simulation,
    Send,
    SendBack,
    SendContinued,
    EndGame
]
