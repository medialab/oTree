# -*- coding: utf-8 -*-
"""IAT game."""

from __future__ import division
from otree.db import models
from os import environ
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
from django.utils.translation import get_language

author = 'Davy Peter Braun <davy.braun@sciencespo.fr>'

doc = """
Implementation of the <a href="https://implicit.harvard.edu/implicit/education.html" target="_blank" rel="noopener">Implicit Association Test for oTree</a>.
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
            'A1': {'order': 'ABCDE', 'iat_file': 'iat_1.json'},
            'A2': {'order': 'ABCDEF', 'iat_file': 'iat_2.json'},
            'B1': {'order': 'ABCDE', 'iat_file': 'iat_1.json'},
            'B2': {'order': 'ABCDEF', 'iat_file': 'iat_2.json'},
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
            
        self.session.vars['lang'] = get_language()


class Group(BaseGroup):
    """Group for IAT."""

    def treatment(self):
        """Get data derived from chosen treatment."""
        return {
            'data': self.session.vars['data'],
            'order': self.session.vars['order'],
            'lang': environ.get('OTREE_LANGUAGE_CODE')
        }


class Player(BasePlayer):
    """Player for IAT."""

    iat_successes = models.TextField()
    iat_failures = models.TextField()
    iat_meta = models.TextField()
