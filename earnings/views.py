"""Models for Earnings."""
# -*- coding: utf-8 -*-
from . import models
from ._builtin import Page
from public_goods.models import Constants as Public_goods_const
from otree.common import Currency as c


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

    def get_dictator_player_a_transfer(self):
        return float(self.player.dictator_player_a_transfer)

    def get_dictator_base_money(self):
        if type(self.player.dictator_base_money) is str:
            return float(self.player.dictator_base_money[1:].strip())
        return float(self.player.dictator_base_money)

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
                self.player.dictator_player_a_transfer
            ),
            'dictator_player_a_remaining': (
                self.player.dictator_player_a_remaining
            ),
            'dictator_player_a_payoff': c(
                self.get_dictator_base_money() -
                self.get_dictator_player_a_transfer()
            ),
            'redirect': (
                'redirects' in self.session.vars and
                self.session.vars['redirects']['complete'] or
                'http://sciences-po.fr'
            ),
            'label': self.participant.label,
            'language_code': self.session.vars['language_code'],
        }


page_sequence = [Calculate, Display]
