"""Models for Earnings."""
# -*- coding: utf-8 -*-
from __future__ import division
import os
import json
import random
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer, Session
from otree.common import Currency

from public_goods.models import Constants as PublicGoodsConsts
from public_goods import models as PublicGoodModels  # noqa
from trust.models import Constants as TrustConsts
from trust import models as TrustModels  # noqa
from dictator import models as DictatorModels  # noqa
from django.utils.translation import get_language

doc = """
Calculates earnings for the Trustlab experiments,
and displays a webpage informing participants of their final earnings.
"""
source_code = ""
bibliography = ()
links = {}
keywords = {}


# Load fallback data for the very first players
# of the game who will not found anyone to match
path = os.path.dirname(os.path.realpath(__file__)) + (
    get_language() == 'ko' and
    '/fallback_data_ko.json' or '/fallback_data.json'
)
with open(path) as json_file:
    fallback_data = json.load(json_file)


class Constants(BaseConstants):
    """Constants model."""

    name_in_url = 'earnings'
    players_per_group = None
    num_rounds = 1

    # List of games to pick from, from which the calculation will be based.
    eligible_games = ['trust', 'dictator', 'public_goods']

    # Base money for all games.
    allocated_amount = Currency(10)

    # Define when to use fallback data for some games.
    min_other_players_for_pg = 3
    min_other_players_for_dictator = 1
    min_other_players_for_trust = 1


class Subsession(BaseSubsession):
    """Subsession model."""

    def before_session_starts(self):
        """
        Assign global variable informing on type of treatment.

        Refers to treatment as set in settings.
        """
        if 'treatment' in self.session.config:
            self.session.vars['treatment'] = self.session.config['treatment']

        self.session.vars['lang'] = get_language()

        if 'quota_redirects' in self.session.config:
            self.session.vars['redirect'] = (
                self.session.config['quota_redirects']['complete']
            )


class Group(BaseGroup):
    """Group model."""

    def calculate_payoff(self, player):
        """
        Calculate and return earnings for a player.

        Save key variables and results exists in the model.
        """
        # Choose (and save reference in DB) a game.
        chosen_game = self.choose_game(Constants.eligible_games)

        # Get payoff from game.
        payoff = None

        if chosen_game is 'dictator':
            (
                payoff, matched_id, role,
                player.dictator_player_a_transfer,
                player.dictator_player_a_remaining,
                player.dictator_base_money
            ) = self.payoff_dictator(player)
            player.calculation_from_game = 'dictator'
            player.calculation_from_matched_player_id = matched_id
            player.calculation_from_role = role
        elif chosen_game is 'public_goods':
            (
                payoff, matched_ids,
                player.pg_player_a_transfer,
                player.pg_player_b_transfer,
                player.pg_player_c_transfer,
                player.pg_player_d_transfer,
                player.pg_joint_sum
            ) = self.payoff_public_goods(player)
            player.calculation_from_game = 'public_goods'
            player.calculation_from_matched_player_id = matched_ids
            player.calculation_from_role = 'N/A'
        elif chosen_game is 'trust':
            (
                payoff, matched_id, role,
                player.trust_game_player_a_transfer,
                player.trust_game_player_b_transfer
            ) = self.payoff_trust(player)
            player.calculation_from_game = 'trust'
            player.calculation_from_matched_player_id = matched_id
            player.calculation_from_role = role

        return payoff

    def choose_game(self, games):
        """Choose an eligible game at random."""
        return random.choice(games)

    def payoff_trust(self, player):
        """Calculate and return payoff for Trust game."""
        payoff = None
        matched_id = None
        with_role = None

        base_money = get_language() == 'ko' and 12000 or 10

        trust_game_player_a_transfer = None
        trust_game_player_b_transfer = None

        # Get the occurence of this player when she played 'Trust'.
        for p in player.participant.get_players():
            if p._meta.app_label == 'trust':
                # If her role was A (role is based on app treatment in config)
                if self.session.vars['treatment'][:1] == 'A':
                    with_role = 'A'
                    given_by_player_a = p.sent_amount
                    given_by_player_b, matched_id = self.strat_trust_a(
                        p, float(given_by_player_a)
                    )
                    payoff = (
                        base_money - given_by_player_a + given_by_player_b
                    )

                    trust_game_player_a_transfer = given_by_player_a
                    trust_game_player_b_transfer = given_by_player_b

                # If her role was B.
                else:
                    with_role = 'B'
                    given_by_player_a, matched_id = self.strat_trust_b(p)
                    given_by_player_b = self.trust_sent_back(
                        p, float(given_by_player_a)
                    )
                    payoff = base_money + (
                        given_by_player_a * TrustConsts.multiplication_factor
                    ) - given_by_player_b

                    trust_game_player_a_transfer = given_by_player_a
                    trust_game_player_b_transfer = given_by_player_b
                break

        return [
            payoff, matched_id, with_role,
            trust_game_player_a_transfer,
            trust_game_player_b_transfer
        ]

    def payoff_dictator(self, player):
        """Calculate and return payoff for Trust game."""
        payoff = None
        matched_id = None

        base_money = get_language() == 'ko' and 12000 or 10

        player_a_transfer = None
        player_b_transfer = None

        # All players were player A, but we simulate gains for both roles.
        role = random.choice(['A', 'B'])

        # Get the occurence of this player when she played 'Dictator'.
        for p in player.participant.get_players():
            if p._meta.app_label == 'dictator':
                # If her role has been determined as A...
                # Basically we lose money we gave away.
                if role == 'A':
                    player_a_transfer = p.given
                    payoff = base_money - p.given
                    matched_id = 'N/A'
                # If her role has been determined as B...
                # We receive the money the chosen "Player A" has given away.
                else:
                    payoff, matched_id = self.strat_dictator(p)
                    player_a_transfer = payoff
                    player_b_transfer = 0
                break

        return [
            payoff, matched_id, role,
            player_a_transfer,
            player_b_transfer,
            base_money
        ]

    def payoff_public_goods(self, player):
        """Calculate and return payoff for Public Goods game."""
        my_contrib = None
        payoff = None
        joint_sum = None
        base_money = get_language() == 'ko' and 12000 or 10

        # Get the occurence of this player when she played 'Public Goods'.
        for p in player.participant.get_players():
            if p._meta.app_label == 'public_goods':
                # Get joint project sum and matching players' IDs.
                (
                    joint_sum, matched_ids, other_players_gave
                ) = self.strat_public_goods(p)
                my_contrib = p.contribution
                payoff = (base_money - my_contrib) + (
                    (joint_sum * PublicGoodsConsts.efficiency_factor) / 4
                )
                break

        return [
            payoff,
            matched_ids,
            my_contrib,
            other_players_gave[0],
            other_players_gave[1],
            other_players_gave[2],
            joint_sum
        ]

    def strat_trust_a(self, player_a, player_a_gave):
        """Select a player B for Trust and return related amount."""
        # Get relevant session IDs.
        sessions_ids = [
            s.id for s in Session.objects.all()
            if s.config['payoff_group'] == self.session.config['payoff_group']
        ]

        # Extract eligible player, that is every player of Trust Game
        # that is not the current user, and that has provided an answer
        # for the `sent_back_amount` field matching the `sent` amount
        # of the current user.
        players = list(TrustModels.Player.objects.filter(
            session__id__in=sessions_ids
        ).exclude(
            id=player_a.id
        ).exclude(
            sent_amount__isnull=True
        ))
        players = [
            p for p in players
            if getattr(p, self.trust_sent_back_amount(player_a_gave))
        ]

        # Get relevant data from a chosen player.
        # Revert to fallback players if none found.
        if len(players) >= Constants.min_other_players_for_trust:
            player_b = random.choice(players)
            matched_id = str(player_b.id)
            sent_back = getattr(
                player_b, self.trust_sent_back_amount(player_a_gave)
            )
        else:
            player_b = random.choice(fallback_data['trust'])
            sent_back = player_b[self.trust_sent_back_amount(player_a_gave)]
            matched_id = player_b['id']

        return [sent_back, matched_id]

    def strat_trust_b(self, player_b):
        """Select a player B for Trust and return related amount."""
        # Get relevant session IDs.
        sessions_ids = [
            s.id for s in Session.objects.all()
            if s.config['payoff_group'] == self.session.config['payoff_group']
        ]

        # Extract eligible player, that is every player of Trust Game
        # that is not the current user.
        players = list(TrustModels.Player.objects.filter(
            session__id__in=sessions_ids
        ).exclude(
            id=player_b.id
        ).exclude(
            sent_back_amount_10__isnull=True
        ).exclude(
            sent_amount__isnull=True
        ))

        if len(players) >= Constants.min_other_players_for_trust:
            player_a = random.choice(players)
            sent_amount = player_a.sent_amount
            matched_id = player_a.id
        else:
            player_a = random.choice(fallback_data['trust'])
            sent_amount = player_a['sent_amount']
            matched_id = player_a['id']

        return [sent_amount, matched_id]

    def strat_dictator(self, player):
        """Pick and return a given amount from another Dictator player."""
        # Get relevant session IDs.
        sessions_ids = [
            s.id for s in Session.objects.all()
            if s.config['payoff_group'] == self.session.config['payoff_group']
        ]

        players = list(DictatorModels.Player.objects.filter(
            session__id__in=sessions_ids
        ).exclude(
            id=player.id
        ).exclude(
            given__isnull=True
        ))

        if len(players) >= Constants.min_other_players_for_dictator:
            matched_player = random.choice(players)
            given = matched_player.given
            matched_id = str(matched_player.id)
        else:
            matched_player = random.choice(fallback_data['dictator'])
            given = matched_player['given']
            matched_id = matched_player['id']

        return [given, matched_id]

    def strat_public_goods(self, player):
        """
        Pick 3 other players in PG game in return the money.

        It is the sum of their contributions related to 1st player's,
        plus 1st player's.
        """
        # Get relevant session IDs.
        sessions_ids = [
            s.id for s in Session.objects.all()
            if s.config['payoff_group'] == self.session.config['payoff_group']
        ]

        # Fetch all eligible players of the Dictator game,
        # meaning they have completed it and are *not*
        # the current user.
        players = list(PublicGoodModels.Player.objects.filter(
            session__id__in=sessions_ids
        ).exclude(
            id=player.id
        ).exclude(
            contribution_back_10__isnull=True
        ))

        # Pick a 3 players sample, using fallback if number is not met.
        fallback_players = []
        if len(players) >= Constants.min_other_players_for_pg:
            players = random.sample(
                players, Constants.min_other_players_for_pg
            )
        else:
            fallback_players = random.sample(
                fallback_data['public_goods'],
                Constants.min_other_players_for_pg - len(players)
            )

        # Get relevant data.
        joint_sum = (
            [p.contribution for p in players] + [player.contribution] +
            [p['contribution'] for p in fallback_players]
        )
        matched_ids = ','.join([str(p.id) for p in players])

        return [sum(joint_sum), matched_ids, joint_sum]

    def trust_sent_back(self, player, given_by_player_a):
        """
        Return sent_back_amount from Trust game.

        Works by crafting the name of a method in Trust Player,
        based on which method returns the amount matching
        the endowment of player A.
        """
        # String representation of relevant method in Trust Player model.
        sent_back_amount = None

        # If Player A sent 0, it's easy — 0.
        # Otherwise, find it.
        if given_by_player_a == 0:
            sent_back_amount = 'sent_back_amount_0'
        else:
            if not sent_back_amount:
                sent_back_amount = self.trust_sent_back_amount(
                    given_by_player_a
                )

        return getattr(player, sent_back_amount)

    def trust_sent_back_amount(self, base):
        """Get Trust sent_back_amount value."""
        # Base endowment for Korea, roughly equals €1.
        k = 1200

        # Korean is complex because of the numbers used (higher than
        # a simple 0 to 10 units). So we simplify it by finding within
        # which ranges the endowment goes, each range then matching
        # a method name.
        if get_language() == 'ko':
            # Create a list of tuples representing ranges,
            # based on steps of 12000 Won just like the form
            # for Trust "send back" mentions.
            # Group those ranges in increasing order into a list
            # of 10 elements (each indices hence representing a range).
            r = [(0, k)]
            r += [(k * i + 1, k + k * i) for i in range(1, 10)]

            # Test within which range the endowment fits.
            # i.e. (0, 12000 representing 0 <= n <= 1200).
            # If you find the fitting index of this range, and add 1,
            # you get the desired output to use to create a proper
            # method name in Player matching the given money.
            # If nothing is found, use fallback data.
            i = list(
                map(lambda x: x[0] <= base <= x[1], r)
            ).index(True)

            sent_back_amount = 'sent_back_amount_' + str(i + 1)
        else:
            sent_back_amount = (
                'sent_back_amount_' + str(base)
            )

        return sent_back_amount


class Player(BasePlayer):
    """Player model."""

    # Field used when user chooses to donate to UNICEF.
    donation = models.DecimalField(
        verbose_name='Please enter the amount you wish to donate to UNICEF',
        max_digits=10,
        decimal_places=2
    )

    # Chosen game for earnings calculation.
    calculation_from_game = models.CharField(max_length=50)

    # Role played by this user in chosen game.
    calculation_from_role = models.CharField(max_length=3)

    # ID of matched player for calculations, if any.
    calculation_from_matched_player_id = models.CharField(max_length=50)

    # Store possible data from transfers if chosen game is Trust.
    trust_game_player_a_transfer = models.CharField(blank=True, null=True)
    trust_game_player_b_transfer = models.CharField(blank=True, null=True)

    # Store possible data from transfers if chosen game is Public Goods.
    pg_joint_sum = models.CharField(blank=True, null=True)
    pg_player_a_transfer = models.CharField(blank=True, null=True)
    pg_player_b_transfer = models.CharField(blank=True, null=True)
    pg_player_c_transfer = models.CharField(blank=True, null=True)
    pg_player_d_transfer = models.CharField(blank=True, null=True)

    # Store possible data from transfers if chosen game is Dictator.
    dictator_player_a_transfer = models.CharField(blank=True, null=True)
    dictator_player_a_remaining = models.CharField(blank=True, null=True)
    dictator_base_money = models.CharField(blank=True, null=True)

    def calculate_payoff(self):
        """
        Calculate and return earnings for a player.

        Save key variables and results in the model.
        Proxies method of the same name in Group.
        """
        self.payoff = self.group.calculate_payoff(self)
