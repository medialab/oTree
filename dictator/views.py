# -*- coding: utf-8 -*-
"""Views for Dictator game."""
from __future__ import division
from . import models
from ._builtin import Page
from .models import Constants


def vars_for_all_templates(self):
    """Return variables accessible for all templates."""
    return {
        'instructions': 'dictator/Instructions.html',
        'constants': Constants
    }


class EndGame(Page):
    """End game page."""

    pass


class Simulation(Page):
    """Simulation page."""

    pass


class Introduction(Page):
    """Introduction page."""

    template_name = 'global/Introduction.html'


class Offer(Page):
    """Offer (participant A) page."""

    form_model = models.Group
    form_fields = ['given']


page_sequence = [
    Introduction,
    Simulation,
    Offer,
    EndGame
]
