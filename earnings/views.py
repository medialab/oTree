"""Models for Earnings."""
# -*- coding: utf-8 -*-
from os import environ
from . import models
from ._builtin import Page
from public_goods.models import Constants as Public_goods_const
from otree.common import Currency
from babel.numbers import parse_decimal
from decimal import Decimal


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

    def str_to_money(self, s):
        """Transform string representing money into float numbers."""
        return parse_decimal(
            (s or '0').strip('€').strip('$').strip('₩').strip(),
            locale=environ.get('OTREE_LANGUAGE_CODE')
        )

    def vars_for_template(self):
        """Variable in template."""
        return {
            'payoff': Currency(self.player.payoff),
            'float_payoff': float(Decimal(Currency(self.player.payoff))),
            'role': self.player.calculation_from_role,
            'chosen_game': self.player.calculation_from_game,
            'trust_game_player_a_transfer': (
                Currency(
                    self.str_to_money(
                        self.player.trust_game_player_a_transfer or 0.0
                    )
                )
            ),
            'trust_game_player_b_transfer': (
                Currency(
                    self.str_to_money(
                        self.player.trust_game_player_b_transfer or 0.0
                    )
                )
            ),
            'pg_player_a_transfer': Currency(
                self.str_to_money(self.player.pg_player_a_transfer) or 0.0
            ),
            'pg_player_b_transfer': Currency(
                self.str_to_money(self.player.pg_player_b_transfer) or 0.0
            ),
            'pg_player_c_transfer': Currency(
                self.str_to_money(self.player.pg_player_c_transfer) or 0.0
            ),
            'pg_player_d_transfer': Currency(
                self.str_to_money(self.player.pg_player_d_transfer) or 0.0
            ),
            'pg_amount': Currency(self.str_to_money(
                self.player.pg_joint_sum) or 0.0
            ),
            'pg_multiplied_amount': round(
                Public_goods_const.efficiency_factor *
                Currency(self.str_to_money(self.player.pg_joint_sum) or 0.0)
            ),
            'dictator_player_a_transfer': (
                Currency(self.str_to_money(
                    self.player.dictator_player_a_transfer
                ) or 0.0)
            ),
            'dictator_player_a_remaining': (
                Currency(self.str_to_money(
                    self.player.dictator_player_a_remaining
                ) or 0.0)
            ),
            'dictator_player_a_payoff': (
                Currency(self.str_to_money(
                    self.player.dictator_base_money or 0.0)
                ) - Currency(self.str_to_money(
                    self.player.dictator_player_a_transfer
                ) or 0.0)
            ),
            'redirect': (
                'redirects' in self.session.vars and
                self.session.vars['redirects']['complete'] or
                'http://sciences-po.fr'
            ),
            'label': self.participant.label,
            'lang': self.session.vars['lang'],
        }


page_sequence = [Calculate, Display]
