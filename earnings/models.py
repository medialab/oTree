"""Models for Earnings."""
# -*- coding: utf-8 -*-
from __future__ import division
import random
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer, Session
from otree.common import Currency

doc = """
This application calculates earnings for the Trustlab experiments,
and provides a webpage instructing participants of their final earnings.
"""
source_code = ""
bibliography = ()
links = {}
keywords = {}


class Constants(BaseConstants):
    """Constants model."""

    name_in_url = 'earnings'
    players_per_group = None
    num_rounds = 1

    # List of games to pick from, from which the calculation will be based.
    eligible_games = ['trust', 'dictator', 'public_goods']

    # Base money for all games.
    allocated_amount = Currency(10)


class Subsession(BaseSubsession):
    """Subsession model."""

    def before_session_starts(self):
        """
        Assign global variable informing on type of treatment.

        Refers to treatment as set in settings.
        """
        if 'treatment' in self.session.config:
            self.session.vars['treatment'] = self.session.config['treatment']


class Group(BaseGroup):
    """Group model."""

    def calculate_payoff(self, player):
        """
        Calculate and return earnings for a player.

        Save key variables and results in the model.
        """
        # Choose (and save reference in DB) a game.
        chosen_game = self.chose_game(Constants.eligible_games)
        player.calculation_from_game = chosen_game

        # Get payoff from game.
        if chosen_game is 'trust':
            return self.payoff_trust(player)
        elif chosen_game is 'public_goods':
            return self.payoff_public_goods(player)
        elif chosen_game is 'dictator':
            return self.payoff_dictator(player)

    def chose_game(self, games):
        """Choose an eligible game at random."""
        return random.choice(games)

    def get_role(self, player, game):
        """Fetch role of current Player in chosen game."""
        pass

    def payoff_trust(self, player):
        """Calculate and return payoff for Trust game."""
        payoff = None
        base_money = Constants.allocated_amount

        # Get the occurence of this player when she played 'Trust'.
        for p in player.participant.get_players():
            if p._meta.app_label is 'trust':
                # If her role was A.
                if p.role() is 'A':
                    player.calculation_from_role = 'A'
                    given_by_player_a = p.sent_amount
                    given_by_player_b = self.strat_player_a_trust(
                        p, given_by_player_a
                    )
                    payoff = base_money - given_by_player_a + given_by_player_b
                # If her role was B.
                else:
                    player.calculation_from_role = 'B'
                    given_by_player_b = self.strat_player_b_trust(p)
                    given_by_player_a = getattr(
                        'sent_back_amount_', given_by_player_b
                    )
                    payoff = base_money + given_by_player_a - given_by_player_b
                break

        return payoff

    def payoff_dictator(self, player):
        """Calculate and return payoff for Trust game."""
        payoff = None
        base_money = Constants.allocated_amount

        # All players were player A, but we simulate gains for both roles.
        role = random.choice(['A', 'B'])

        # Get the occurence of this player when she played 'Dictator'.
        for p in player.participant.get_players():
            if p._meta.app_label is 'dictator':
                # If her role was A.
                if role is 'A':
                    player.calculation_from_role = 'A'
                    payoff = base_money - p.given
                # If her role was A.
                else:
                    player.calculation_from_role = 'B'
                    payoff = base_money - self.strat_player_dictator(p)
                break

        return payoff

    def payoff_public_goods(self, player):
        """Calculate and return payoff for Public Goods game."""
        payoff = None
        base_money = Constants.allocated_amount

        # There's no A/B role in this game.
        player.calculation_from_role = None

        # Get the occurence of this player when she played 'Public Goods'.
        for p in player.participant.get_players():
            if p._meta.app.app_label is 'public_goods':
                p_gave = p.contribution
                joint_sum = self.strat_player_public_goods(p)
                payoff = (base_money - p_gave) + ((joint_sum * 1.3) / 4)
                break

        return payoff

    def strat_player_a_trust(self, player_a, player_a_gave):
        """Select a player B for Trust and return related amount."""
        # Payoff group for this session
        pg = self.session.config['payoff_group']

        # In sessions from same payoff_group, find a random player B.
        # If we wanted only players from this session:
        # all_other_players = self.get_players()
        other_players = []

        def add_player_if_eligible(player):
            if player._meta.app_label is 'trust' and player.role() is 'B':
                # Should never happen, but double check nonetheless.
                if player is not player_a:
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
        player_b = random.choice(other_players)
        return getattr(player_b, 'sent_back_amount_' + player_a_gave)

    def strat_player_b_trust(self, player_b):
        """Select a player B for Trust and return related amount."""
        # Payoff group for this session
        pg = self.session.config['payoff_group']

        # In sessions from same payoff_group, find a random player A.
        # If we wanted only players from this session:
        # all_other_players = self.get_players()
        other_players = []

        def add_player_if_eligible(player):
            if player._meta.app_label is 'trust' and player.role() is 'A':
                # Should never happen, but double check nonetheless.
                if player is not player_b:
                    other_players.append(player)

        for s in Session.objects.all():
            if 'payoff_group' in s.config and s.config['payoff_group'] is pg:
                    # `Participants` are all possible players.
                    for p in s.get_participants():
                        # For each participant, get their occurence of Trust
                        # game players and see if they are eligible.
                        trust_player = p.get_players()[0]
                        add_player_if_eligible(trust_player)

        # Pick a random player A from eligible players and return money.
        player_a = random.choice(other_players)
        return getattr(player_a, 'sent_amount')

    def strat_player_dictator(self, player):
        """Pick and return a given amount from another Dictator player."""
        # Payoff group for this session
        pg = self.session.config['payoff_group']

        # In sessions from same payoff_group, find a random player A.
        # If we wanted only players from this session:
        # all_other_players = self.get_players()
        other_players = []

        def add_player_if_eligible(p):
            if p._meta.app_label is 'dictator' and p is not player:
                other_players.append(p)

        for s in Session.objects.all():
            if 'payoff_group' in s.config and s.config['payoff_group'] is pg:
                for p in s.get_participants():
                    dictator_player = p.get_players()[2]
                    add_player_if_eligible(dictator_player)

        return random.choice(other_players).given

    def strat_player_public_goods(self, player):
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
            if p._meta.app_label is 'public_goods' and p is not player:
                other_players.append(p)

        for s in Session.objects.all():
            if 'payoff_group' in s.config and s.config['payoff_group'] is pg:
                for p in s.get_participants():
                    public_goods_player = p.get_players[1]
                    add_player_if_eligible(public_goods_player)

        # Shuffle and pick three.
        random.shuffle(other_players)
        other_players = other_players[:3]

        # Return the sum of their contributions related to 1st player's
        # plus 1st player's contribution.
        joint_sum = [
            getattr(p, 'contribution_back_') for p in other_players
        ]
        joint_sum.append(p.contribution)
        return sum(joint_sum)


class Player(BasePlayer):
    """Player model."""

    # Field used when user chooses to donate to UNICEF.
    donation = models.IntegerField(
        verbose_name='Please enter the amount you wish to donate to UNICEF'
    )

    # Chosen game for earnings calculation.
    calculation_from_game = models.CharField(max_length=50)

    # Role played by this user in chosen game.
    calculation_from_role = models.CharField(max_length=3)

    def calculate_payoff(self):
        """
        Calculate and return earnings for a player.

        Save key variables and results in the model.
        Proxies method of the same name in Group.
        """
        return self.group.calculate_payoff(self)
