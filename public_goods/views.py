# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants

class Introduction(Page):

    """Description of the game: How to play and returns expected"""
    pass


class EndGame(Page):
    pass


class Simulation(Page):
    pass


class Question(Page):

    def is_displayed(self):
        return True

    form_model = models.Player
    form_fields = ['question']


class Feedback(Page):
    def is_displayed(self):
        return True


class DecisionInstructions(Page):
    pass


class Contribute(Page):

    """Player: Choose how much to contribute"""

    form_model = models.Player
    form_fields = ['contribution']

    timeout_submission = {'contribution': c(Constants.endowment/2)}


class ContributeBack(Page):

    form_model = models.Player
    form_fields = [
        'contribution_back_0',
        'contribution_back_1',
        'contribution_back_2',
        'contribution_back_3',
        'contribution_back_4',
        'contribution_back_5',
        'contribution_back_6',
        'contribution_back_7',
        'contribution_back_8',
        'contribution_back_9',
        'contribution_back_10'
    ]


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

    body_text = "Waiting for other participants to contribute."


class Results(Page):

    """Players payoff: How much each has earned"""

    def vars_for_template(self):

        return {
            'total_earnings': self.group.total_contribution * Constants.efficiency_factor,
            'individual_earnings': self.player.payoff - Constants.base_points,
        }

page_sequence = [
            Introduction,
            Simulation,
            # Question,
            # Feedback,
            DecisionInstructions,
            Contribute,
            ContributeBack,
            # ResultsWaitPage,
            # Results
            EndGame
        ]
