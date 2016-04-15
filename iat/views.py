# -*- coding: utf-8 -*-
"""Views for IAT."""
from __future__ import division
from . import models
from ._builtin import Page


def vars_for_all_templates(self):
    """Return variables for all views."""
    return {
        'instructions': 'iat/Instructions.html',
        'data': self.group.treatment()['data'],
        'order': self.group.treatment()['order'],
        'language_code': self.group.treatment()['language_code']
    }


class Introduction(Page):
    """Introduction page."""

    template_name = 'global/Introduction.html'


class EndGame(Page):
    """End of game page."""

    pass


class IAT(Page):
    """Main game page."""

    form_model = models.Player
    form_fields = ['iat_results']


page_sequence = [
    Introduction,
    IAT,
    EndGame
]
