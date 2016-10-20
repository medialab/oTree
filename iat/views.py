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
    form_model = models.Player


class EndGame(Page):
    """End of game page."""

    form_model = models.Player

    def vars_for_template(self):
        """Make data available in template."""
        return {
            'normal_render': self.group.treatment()[
                'oecd_iat'
            ] is True and 'hide' or '',
            'oecd_render': self.group.treatment()[
                'oecd_iat'
            ] is not True and 'hide' or ''
        }


class IAT(Page):
    """Main game page."""

    form_model = models.Player
    form_fields = ['iat_results']


page_sequence = [IAT, EndGame]
