# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

import jsonfield

author = 'Davy Peter Braun <davy.braun@sciencespo.fr>'

doc = """
An implementation of the Implicit Association Test for oTree.
"""


class Constants(BaseConstants):
    name_in_url = 'iat'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def before_session_starts(self):
        treatments = {
            'A1a': {'order': 'ABCDEFG', 'iat_file': 'iat_1.json'},
            'A1b': {'order': 'ACBEDGF', 'iat_file': 'iat_1.json'},
            'A2a': {'order': 'ABCDEFG', 'iat_file': 'iat_2.json'},
            'A2b': {'order': 'ACBEDGF', 'iat_file': 'iat_2.json'},
            'B1a': {'order': 'ABCDEFG', 'iat_file': 'iat_1.json'},
            'B1b': {'order': 'ACBEDGF', 'iat_file': 'iat_1.json'},
            'B2a': {'order': 'ABCDEFG', 'iat_file': 'iat_2.json'},
            'B2b': {'order': 'ACBEDGF', 'iat_file': 'iat_2.json'},
        }

        if 'treatment' in self.session.config:
            self.session.vars['order'] = treatments[
                self.session.config['treatment']
            ]['order']

            self.session.vars['iat_file'] = treatments[
                self.session.config['treatment']
            ]['iat_file']

            self.session.vars['data'] = open('iat/static/' + self.session.vars['iat_file'], 'r').read()


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    iat_results = jsonfield.JSONField()
