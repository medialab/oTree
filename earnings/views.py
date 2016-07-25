"""Models for Earnings."""
# -*- coding: utf-8 -*-
from . import models
from ._builtin import Page
from public_goods.models import Constants as Public_goods_const


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
            'payoff': self.player.payoff,
            'role': self.player.calculation_from_role,
            'chosen_game': self.player.calculation_from_game,
            'trust_game_player_a_transfer': '',
            'trust_game_player_b_transfer': '',
            'pg_player_b_transfer': '',
            'pg_player_c_transfer': '',
            'pg_player_d_transfer': '',
            'pg_amount': '',
            'pg_multiplied_amount': Public_goods_const.efficiency_factor,
            'dictator_player_a_transfer': '',
            'dictator_player_a_remaning': '',
        }


page_sequence = [Calculate, Earnings]
