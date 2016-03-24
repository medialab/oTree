# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

import json
import jsonfield

author = 'Davy Peter Braun <davy.braun@sciencespo.fr>'

doc = """
An implementation of the Implicit Association Test for oTree.
"""


class Constants(BaseConstants):
    name_in_url = 'iat'
    players_per_group = None
    num_rounds = 1
    data = open('iat/static/iat.json', 'r').read()
    test_title = json.loads(data)['config']['title']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    iat_results = jsonfield.JSONField()
