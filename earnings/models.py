"""Models for Earnings."""
# -*- coding: utf-8 -*-
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

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


class Subsession(BaseSubsession):
    """Subsession model."""

    pass


class Group(BaseGroup):
    """Group model."""

    pass


class Player(BasePlayer):
    """Player model."""

    donation = models.IntegerField(
        verbose_name='Please enter the amount you wish to donate to UNICEF'
    )
