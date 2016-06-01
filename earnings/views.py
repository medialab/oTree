"""Models for Earnings."""
# -*- coding: utf-8 -*-
from . import models
from ._builtin import Page
# from .models import Constants


class Calculate(Page):

    form_model = models.Player

    def before_next_page(self):
        """Return variables for the template."""
        payoff = self.player.calculate_payoff()
        return {
            'payoff': payoff
        }


class Earnings(Page):
    """Earnings page."""

    form_model = models.Player
    form_fields = ['donation']


page_sequence = [Calculate, Earnings]
