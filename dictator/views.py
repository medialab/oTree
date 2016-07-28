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
        'constants': Constants
    }


class EndGame(Page):
    """End game page."""

    form_model = models.Player
    form_fields = ['total_time']

    def vars_for_template(self):
        """Make data available in template."""
        return {'start_time': self.player.total_time}


class Simulation(Page):
    """Simulation page."""

    def vars_for_template(self):
        max = {'fr': 10, 'us': 10, 'ko': 10000}
        return {
            'max': max[self.session.vars['lang']]
        }


class Introduction(Page):
    """Introduction page."""

    template_name = 'global/Introduction.html'
    form_model = models.Player
    form_fields = ['total_time']

    def vars_for_template(self):
        return {
            'fr': {'amount': _(u'10 euros')},
            'ko': {'amount': _(u'12.000 Won')},
        }


class Offer(Page):
    """Offer (participant A) page."""

    form_model = models.Player
    form_fields = ['given']

    def vars_for_template(self):
        return {
            'fr': {'amount': _(u'10 euros')},
            'ko': {'amount': _(u'12.000 Won')},
        }


page_sequence = [
    Introduction,
    # Simulation,
    Offer,
    EndGame
]
