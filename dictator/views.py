# -*- coding: utf-8 -*-
"""Views for Dictator game."""
from __future__ import division
from . import models
from ._builtin import Page
from .models import Constants
from django.utils.translation import ugettext_lazy as _


def vars_for_all_templates(self):
    """Return variables accessible for all templates."""
    return {
        'instructions': 'dictator/Instructions.html',
        'constants': Constants,
        'lang': self.session.vars['lang']
    }


class EndGame(Page):
    """End game page."""

    form_model = models.Player


class Simulation(Page):
    """Simulation page."""

    def vars_for_template(self):
        max = {'fr': 10, 'en': 10, 'ko': 12000}
        step = {'fr': 1, 'en': 1, 'ko': 1000}
        return {
            'max': max[self.session.vars['lang']],
            'step': step[self.session.vars['lang']]
        }


class Introduction(Page):
    """Introduction page."""

    template_name = 'global/Introduction.html'
    form_model = models.Player

    def vars_for_template(self):
        amount = {
            'fr': _(u'10 euros'),
            'en': _(u'$10'),
            'ko': _(u'12.000 Won')
        }
        return {
            'amount': amount[self.session.vars['lang']]
        }


class Offer(Page):
    """Offer (participant A) page."""

    form_model = models.Player
    form_fields = ['given']

    def vars_for_template(self):
        amount = {
            'fr': _(u'10 euros'),
            'en': _(u'$10'),
            'ko': _(u'12.000 Won')
        }
        return {
            'amount': amount[self.session.vars['lang']]
        }


page_sequence = [
    Introduction,
    # Simulation,
    Offer,
    EndGame
]
