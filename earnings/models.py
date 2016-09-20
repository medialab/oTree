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
from public_goods.models import Constants as Public_goods_const
from trust.models import Constants as Trust_const

doc = """
This application calculates earnings for the Trustlab experiments,
and provides a webpage instructing participants of their final earnings.
"""
source_code = ""
bibliography = ()
links = {}
keywords = {}


# Load fallback data for the very first players
# of the game who will not found anyone to match
path = os.path.dirname(os.path.realpath(__file__)) + '/fallback_data.json'
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

        if 'language_code' in self.session.config:
            self.session.vars['language_code'] = (
                self.session.config['language_code']
            )

        if 'quota_redirects' in self.session.config:
            self.session.vars['redirect'] = (
                self.session.config['quota_redirects']['complete']
            )


class Group(BaseGroup):
    """Group model."""

    def calculate_payoff(self, player):
        """
        Calculate and return earnings for a player.

        Save key variables and results in the model.
        """
        # Choose (and save reference in DB) a game.
        # chosen_game = self.choose_game(Constants.eligible_games)
        chosen_game = 'public_goods'
        player.calculation_from_game = chosen_game

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

        base_money = Constants.allocated_amount

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
                        p, given_by_player_a
                    )
                    payoff = (base_money - given_by_player_a + given_by_player_b)

                    trust_game_player_a_transfer = given_by_player_a
                    trust_game_player_b_transfer = given_by_player_b

                # If her role was B.
                else:
                    with_role = 'B'
                    given_by_player_a, matched_id = self.strat_trust_b(p)
                    given_by_player_b = getattr(
                        p, 'sent_back_amount_' + str(int(given_by_player_a))
                    )
                    payoff = base_money + (
                        given_by_player_a * Trust_const.multiplication_factor
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

        base_money = Constants.allocated_amount

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
        base_money = Constants.allocated_amount

        # Get the occurence of this player when she played 'Public Goods'.
        for p in player.participant.get_players():
            if p._meta.app_label == 'public_goods':
                # Get joint project sum and matching players' IDs.
                (
                    joint_sum, matched_ids, other_players_gave
                ) = self.strat_public_goods(p)
                my_contrib = p.contribution
                payoff = (base_money - my_contrib) + (
                    (joint_sum * Public_goods_const.efficiency_factor) / 4
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
        # Payoff group for this session
        pg = self.session.config['payoff_group']

        # In sessions from same payoff_group, find a random player B.
        # If we wanted only players from this session:
        # all_other_players = self.get_players()
        other_players = []

        def add_player_if_eligible(player):
            if player._meta.app_label == 'trust':
                # Should never happen, but double check nonetheless.
                if player is not player_a:
                    if getattr(
                        player, 'sent_back_amount_' + str(int(player_a_gave))
                    ) is not None:
                        other_players.append(player)

        for s in Session.objects.all():
            if 'payoff_group' in s.config and s.config['payoff_group'] is pg:
                # `Participants` are all possible players.
                for p in s.get_participants():
                    # For each participant, get their occurence of Trust
                    # game players and see if they are eligible.
                    trust_player = p.get_players()[0]
                    add_player_if_eligible(trust_player)

        # Pick a random player B from eligible players and return money.
        # Use fallback data if none available yet.
        if len(other_players) >= Constants.min_other_players_for_trust:
            player_b = random.choice(other_players)

            # Store matched player's ID.
            matched_id = str(player_b.id)
            sent_back = getattr(
                player_b, 'sent_back_amount_' + str(int(player_a_gave))
            )
        else:
            u = random.choice(fallback_data['trust'])
            sent_back = u[
                'sent_back_amount_' + str(int(player_a_gave))
            ]
            matched_id = u['id']

        return [sent_back, matched_id]

    def strat_trust_b(self, player_b):
        """Select a player B for Trust and return related amount."""
        # Payoff group for this session
        pg = self.session.config['payoff_group']

        # In sessions from same payoff_group, find a random player A.
        # If we wanted only players from this session:
        # all_other_players = self.get_players()
        other_players = []

        def add_player_if_eligible(player):
            if player._meta.app_label == 'trust':
                # Should never happen, but double check nonetheless.
                if player is not player_b and player.sent_amount is not None:
                    other_players.append(player)

        for s in Session.objects.all():
            if 'payoff_group' in s.config and s.config['payoff_group'] is pg:
                # `Participants` are all possible players.
                for p in s.get_participants():
                    # For each participant, get their occurence of Trust
                    # game players and see if they are eligible.
                    trust_player = p.get_players()[0]
                    add_player_if_eligible(trust_player)

        # Pick a random player A from eligible players and return money and
        # store matched player's ID. Use fallback in case of lack of data.
        if len(other_players) >= Constants.min_other_players_for_trust:
            player_a = random.choice(other_players)
            sent_amount = player_a.sent_amount
            matched_id = player_a.id
        else:
            u = random.choice(fallback_data['trust'])
            sent_amount = u['sent_amount']
            matched_id = u['id']

        return [sent_amount, matched_id]

    def strat_dictator(self, player):
        """Pick and return a given amount from another Dictator player."""
        # Payoff group for this session
        pg = self.session.config['payoff_group']

        # In sessions from same payoff_group, find a random player A.
        # If we wanted only players from this session:
        # all_other_players = self.get_players()
        other_players = []

        def add_player_if_eligible(p):
            if p._meta.app_label == 'dictator' and p is not player:
                if p.given is not None:
                    other_players.append(p)

        for s in Session.objects.all():
            if 'payoff_group' in s.config and s.config['payoff_group'] is pg:
                for p in s.get_participants():
                    dictator_player = p.get_players()[2]
                    add_player_if_eligible(dictator_player)

        # Pick matching player, return money and matched player's ID.
        # Use fallback data if there are not enough players.
        if len(other_players) >= Constants.min_other_players_for_dictator:
            matched = random.choice(other_players)
            given = matched.given
            id = str(matched.id)
        else:
            u = random.choice(fallback_data['dictator'])
            given = u['given']
            id = u['id']

        return [given, id]

    def strat_public_goods(self, player):
        """
        Pick 3 other players in PG game in return the money.

        It is the sum of their contributions related to 1st player's,
        plus 1st player's.
        """
        # Payoff group for this session
        pg = self.session.config['payoff_group']

        # In sessions from same payoff_group, find a random player A.
        # If we wanted only players from this session:
        # all_other_players = self.get_players()
        other_players = []

        def add_player_if_eligible(p):
            if p._meta.app_label == 'public_goods' and p is not player:
                if p.contribution is not None:
                    other_players.append(p)

        for s in Session.objects.all():
            if 'payoff_group' in s.config and s.config['payoff_group'] is pg:
                for p in s.get_participants():
                    public_goods_player = p.get_players()[1]
                    add_player_if_eligible(public_goods_player)

        fallback_players = []
        if len(other_players) >= Constants.min_other_players_for_pg:
            # Shuffle and pick three.
            other_players = random.sample(
                other_players, Constants.min_other_players_for_pg
            )
        else:
            # first players will miss existing players to be matched to
            # let's use fallback data to add the missing results
            nb_missing_players = (
                Constants.min_other_players_for_pg - len(other_players)
            )

            fallback_players = random.sample(
                fallback_data['public_goods'], nb_missing_players
            )

        # Return the sum of their contributions
        # plus 1st player's contribution.
        joint_sum = [p.contribution for p in other_players]
        joint_sum += [p['contribution'] for p in fallback_players]

        # IDs of matched players.
        matched_ids = ','.join(
            [str(u.id) for u in other_players] +
            [u['id'] for u in fallback_players]
        )

        joint_sum.append(player.contribution)

        return [sum(joint_sum), matched_ids, joint_sum]


class Player(BasePlayer):
    """Player model."""

    # Field used when user chooses to donate to UNICEF.
    donation = models.DecimalField(
        verbose_name='Please enter the amount you wish to donate to UNICEF',
        max_digits=5,
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
