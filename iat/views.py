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
        'lang': self.session.vars['lang']
    }


class Introduction(Page):
    """Introduction page."""

    template_name = 'global/Introduction.html'
    form_model = models.Player


class EndGame(Page):
    """End of game page."""

    form_model = models.Player


class IAT(Page):
    """Main game page."""

    form_model = models.Player
    form_fields = ['iat_successes', 'iat_failures', 'iat_meta']

    def vars_for_template(self):
        """Pass usable data to template."""
        return {
            'participant_id': self.player.id,
            'participant_code': self.player.participant.code,
            'participant_label': self.player.participant.label
        }


page_sequence = [IAT, EndGame]
