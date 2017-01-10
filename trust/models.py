# -*- coding: utf-8 -*-
"""Models for trust game."""
from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, Currency
)
from django.utils.translation import get_language

doc = """
This is a standard 2-player trust game where the amount sent by player 1 gets
tripled. The trust game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.<br>
Trustlab's version uses the strategic method.
"""

amount_allocated = get_language() == 'ko' and 12000 or 10


def get_amount_allocated(base_fr_money):
    """
    Get allocated amount after sent back contribution.

    Calculate different results depending on locale.
    """
    if get_language() == 'ko':
        amount_allocated = 12000
        added = base_fr_money * 1200
    else:
        amount_allocated = 10
        added = base_fr_money

    return Currency(amount_allocated + added * Constants.multiplication_factor)


class Constants(BaseConstants):
    """Constants for Trust game."""

    name_in_url = 'trust'
    players_per_group = None
    num_rounds = 1

    instructions_template = 'trust/Instructions.html'

    # Initial amount allocated to each player
    multiplication_factor = 3


class Subsession(BaseSubsession):
    """Subsession model for Trust game."""

    def before_session_starts(self):
        """Set treatment of the game (see settings.py) as global var."""
        if 'treatment' in self.session.config:
            self.session.vars['treatment'] = self.session.config['treatment']
        self.session.vars['lang'] = get_language()


class Group(BaseGroup):
    """Group model for Trust game."""

    pass


class Player(BasePlayer):
    """Player model for Trust."""

    sent_amount = models.CurrencyField(
        doc="""Amount sent by P1""",
        min=Currency(0),
        max=get_amount_allocated(0)
    )

    sent_back_amount_0 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 0 from P1""",
        min=Currency(0),
        max=get_amount_allocated(0)
    )

    sent_back_amount_1 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 1 from P1""",
        min=Currency(0),
        max=get_amount_allocated(1)
    )

    sent_back_amount_2 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 2 from P1""",
        min=Currency(0),
        max=get_amount_allocated(2)
    )

    sent_back_amount_3 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 3 from P1""",
        min=Currency(0),
        max=get_amount_allocated(3)
    )

    sent_back_amount_4 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 4 from P1""",
        min=Currency(0),
        max=get_amount_allocated(4)
    )

    sent_back_amount_5 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 5 from P1""",
        min=Currency(0),
        max=get_amount_allocated(5)
    )

    sent_back_amount_6 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 6 from P1""",
        min=Currency(0),
        max=get_amount_allocated(6)
    )

    sent_back_amount_7 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 7 from P1""",
        min=Currency(0),
        max=get_amount_allocated(7)
    )

    sent_back_amount_8 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 8 from P1""",
        min=Currency(0),
        max=get_amount_allocated(8)
    )

    sent_back_amount_9 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 9 from P1""",
        min=Currency(0),
        max=get_amount_allocated(9)
    )

    sent_back_amount_10 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 10 from P1""",
        min=Currency(0),
        max=get_amount_allocated(10)
    )

    def role(self):
        """Return role ID/name based on ID in group."""
        return {1: 'A', 2: 'B'}[self.id_in_group]

    def treatment(self):
        """Return chosen treatment for XP."""
        return self.session.vars['treatment']
