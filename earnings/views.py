"""Models for Earnings."""
# -*- coding: utf-8 -*-
from os import environ
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

    def cleanup_money(self, str_amount):
        m = str_amount.replace(
            u'\xa0', u' '
        ).strip().strip('€').strip('$').strip('₩').strip()

        if environ.get(
            'OTREE_LANGUAGE_CODE', self.session.config['language_code']
        ) == 'ko-kr':
            # For Korean, find commas before decimal part,
            # and remove them.
            m = m.replace(',', '')
            print(m)
            return m
        else:
            # For th rest (i.e. French) some commas might be used for decimal.
            # Change them into expected dots.
            return m.replace(',', '.')

    def get_dictator_player_a_transfer(self):
        if self.player.dictator_player_a_transfer:
            return float(
                self.cleanup_money(self.player.dictator_player_a_transfer)
            )
        return 0

    def get_dictator_base_money(self):
        if self.player.dictator_base_money:
            if type(self.player.dictator_base_money) is str:
                return float(
                    self.cleanup_money(self.player.dictator_base_money)
                )
            return float(self.player.dictator_base_money)
        return 0

    def vars_for_template(self):
        """Variable in template."""
        return {
            'payoff': self.player.payoff,
            'role': self.player.calculation_from_role,
            'chosen_game': self.player.calculation_from_game,
            'trust_game_player_a_transfer': (
                self.cleanup_money(self.player.trust_game_player_a_transfer or '')
            ),
            'trust_game_player_b_transfer': (
                self.cleanup_money(self.player.trust_game_player_b_transfer or '')
            ),
            'pg_player_a_transfer': self.cleanup_money(self.player.pg_player_a_transfer or ''),
            'pg_player_b_transfer': self.cleanup_money(self.player.pg_player_b_transfer or ''),
            'pg_player_c_transfer': self.cleanup_money(self.player.pg_player_c_transfer or ''),
            'pg_player_d_transfer': self.cleanup_money(self.player.pg_player_d_transfer or ''),
            'pg_amount': self.cleanup_money(self.player.pg_joint_sum or ''),
            'pg_multiplied_amount': round(
                float(Public_goods_const.efficiency_factor) *
                float(str(self.cleanup_money(self.player.pg_joint_sum or '0')))
            ),
            'dictator_player_a_transfer': (
                self.cleanup_money(self.player.dictator_player_a_transfer or '')
            ),
            'dictator_player_a_remaining': (
                self.cleanup_money(self.player.dictator_player_a_remaining or '')
            ),
            'dictator_player_a_payoff': (
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
