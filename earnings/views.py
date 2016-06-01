"""Models for Earnings."""
# -*- coding: utf-8 -*-
from . import models
from ._builtin import Page
# from .models import Constants


class Earnings(Page):
    """Earnings page."""

    form_model = models.Player
    form_fields = ['donation']

    def vars_for_template(self):
        return {
            'payoff': self.player.calculate_payoff()
        }


page_sequence = [Earnings]
