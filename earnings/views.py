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


class Display(Page):
    """Display page."""

    form_model = models.Player
    form_fields = ['donation']

    def vars_for_template(self):
        """Variable in template."""
        return {
            'payoff': self.player.payoff,
            'role': self.player.calculation_from_role,
            'chosen_game': self.player.calculation_from_game,
            'trust_game_player_a_transfer': (
                self.player.trust_game_player_a_transfer
            ),
            'trust_game_player_b_transfer': (
                self.player.trust_game_player_b_transfer
            ),
            'pg_player_b_transfer': self.player.pg_player_b_transfer,
            'pg_player_c_transfer': self.player.pg_player_c_transfer,
            'pg_player_d_transfer': self.player.pg_player_d_transfer,
            'pg_amount': self.player.pg_joint_sum,
            'pg_multiplied_amount': Public_goods_const.efficiency_factor,
            'dictator_player_a_transfer': (
                self.player.trust_game_player_a_transfer
            ),
            'dictator_player_a_remaining': (
                self.player.dictator_player_a_remaining
            ),
            'redirect': self.session.vars['redirect_complete'],
            'label': self.participant.label,
            'language_code': self.session.vars['language_code'],
        }


page_sequence = [Calculate, Display]
