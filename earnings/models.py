"""Models for Earnings."""
# -*- coding: utf-8 -*-
# <standard imports>
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# # </standard imports>

doc = """
This application calculates earnings for the Trustlab experiments,
and provides a webpage instructing participants of their final earnings.
"""
source_code = ""
bibliography = ()
links = {}
keywords = {}


class Constants(BaseConstants):
    """Constants."""

    name_in_url = 'earnings'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    """Subsession."""

    pass


class Group(BaseGroup):
    """Group."""

    pass


class Player(BasePlayer):
    """Player."""

    pass
