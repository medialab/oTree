# -*- coding: utf-8 -*-
"""IAT game."""

# <standard imports>
from __future__ import division
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

import jsonfield

author = 'Davy Peter Braun <davy.braun@sciencespo.fr>'

doc = """
An implementation of the Implicit Association Test for oTree.
"""


class Constants(BaseConstants):
    """Constants for IAT."""

    name_in_url = 'iat'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    """Subsession for IAT."""

    def before_session_starts(self):
        """Derive data from chosen treatment."""
        treatments = {
            'A1a': {'order': 'ABCDEFG', 'iat_file': 'iat_1.json'},
            'A1b': {'order': 'ACBEDGF', 'iat_file': 'iat_1.json'},
            'A2a': {'order': 'ABCDEF', 'iat_file': 'iat_2.json'},
            'A2b': {'order': 'ACBDFE', 'iat_file': 'iat_2.json'},
            'B1a': {'order': 'ABCDEFG', 'iat_file': 'iat_1.json'},
            'B1b': {'order': 'ACBEDGF', 'iat_file': 'iat_1.json'},
            'B2a': {'order': 'ABCDEF', 'iat_file': 'iat_2.json'},
            'B2b': {'order': 'ACBDFE', 'iat_file': 'iat_2.json'},
        }

        if 'treatment' in self.session.config:
            self.session.vars['order'] = treatments[
                self.session.config['treatment']
            ]['order']

            self.session.vars['iat_file'] = treatments[
                self.session.config['treatment']
            ]['iat_file']

            self.session.vars['data'] = open(
                'iat/static/' + self.session.vars['iat_file'], 'r'
            ).read()


class Group(BaseGroup):
    """Group for IAT."""

    def treatment(self):
        """Get data derived from chosen treatment."""
        return {
            'data': self.session.vars['data'],
            'order': self.session.vars['order'],
            'language_code': self.session.config['language_code']
        }


class Player(BasePlayer):
    """Player for IAT."""

    iat_results = jsonfield.JSONField()
