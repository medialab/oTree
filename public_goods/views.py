# -*- coding: utf-8 -*-
"""Views for Public Goods."""

from __future__ import division
from . import models
from ._builtin import Page
from otree.common import Currency
from .models import Constants


class Introduction(Page):
    """Introduction for Public Goods."""

    pass


class EndGame(Page):
    """End page for Public Goods."""

    pass


class Simulation(Page):
    """Simuation for Public Goods."""

    pass


class DecisionInstructions(Page):
    """Decision instructions page for Public Goods."""

    pass


class Contribute(Page):
    """Participant A's contribution."""

    form_model = models.Player
    form_fields = ['contribution']

    timeout_submission = {'contribution': Currency(Constants.endowment / 2)}


class ContributeBack(Page):
    """Participant B's contribution."""

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


page_sequence = [
    Introduction,
    Simulation,
    DecisionInstructions,
    Contribute,
    ContributeBack,
    EndGame
]
