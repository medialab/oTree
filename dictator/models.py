# -*- coding: utf-8 -*-
"""Models for Dictator game."""

# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
from otree.common import Currency
# </standard imports>


doc = """
One player decides how to divide a certain amount between himself and the other
player.
"""

source_code = "https://github.com/oTree-org/oTree/tree/master/dictator"


bibliography = (
    (
        'Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness '
        'and the assumptions of economics." Journal of business (1986): '
        'S285-S300.'
    ),
    (
        'Hoffman, Elizabeth, Kevin McCabe, and Vernon L. Smith. "Social '
        'distance and other-regarding behavior in dictator games." The '
        'American Economic Review(1996): 653-660.'
    )
)


links = {
    "Wikipedia": {
        "Dictator Game": "https://en.wikipedia.org/wiki/Dictator_game"
    }
}


keywords = ("Dictator Game", "Fairness", "Homo Economicus")


class Constants(BaseConstants):
    """Constants for Dictator game."""

    name_in_url = 'dictator'
    players_per_group = 2
    num_rounds = 1

    bonus = Currency(1)

    # Initial amount allocated to the dictator
    allocated_amount = Currency(10)


class Subsession(BaseSubsession):
    """Subsession for Dictator game."""

    def before_session_starts(self):
        """
        Assign global variable informing on type of treatment.

        Refers to treatment as set in settings.
        """
        if 'treatment' in self.session.config:
            self.session.vars['treatment'] = self.session.config['treatment']


class Group(BaseGroup):
    """Group for Dictator game."""

    given = models.CurrencyField(
        doc="""Amount dictator decided to given""",
        min=0, max=Constants.allocated_amount,
        verbose_name=''
    )

    def set_payoffs(self):
        """Set payoffs (used by test bot)."""
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.bonus + self.given
        p2.payoff = Constants.bonus + Constants.allocated_amount - self.given


class Player(BasePlayer):
    """Player for Dictator game."""

    training_participant1_payoff = models.CurrencyField(
        verbose_name="Participant 1's payoff would be")
    training_participant2_payoff = models.CurrencyField(
        verbose_name="Participant 2's payoff would be")
