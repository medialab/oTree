"""Models for Earnings."""
# -*- coding: utf-8 -*-
from . import models
from ._builtin import Page
# from .models import Constants


class Calculate(Page):
    """Calculate then redirect to last page."""

    form_model = models.Player

    def before_next_page(self):
        """Return variables for the template."""
        self.player.calculate_payoff()


class Earnings(Page):
    """Earnings page."""

    form_model = models.Player
    # form_fields = ['donation']

    def vars_for_template(self):
        """Variable in template."""
        return {
            'payoff': self.player.payoff
        }


page_sequence = [Calculate, Earnings]
