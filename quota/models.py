# -*- coding: utf-8 -*-
"""Models for Quota."""

from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
import json
# from otree.common import Currency

doc = """
Quota calculator screening the user passing the experiments.

Settings for the experiment should have `quotas` field such as:

'quotas': [
    {'age=XX&gender=XX&sc=XXX&sn=XX': 1}
]

The `quotas` field is an array filled with dictionnaries,
where each key is a string that can be parsed to extract
the variables for this quota (similar to GET variables),
and the value is the actual number of slots for the quota.
"""


class Constants(BaseConstants):
    """Constants for Quota."""

    name_in_url = 'quota'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    """Subsession for Quota."""

    def before_session_starts(self):
        """Parse information config."""
        if 'quotas' in self.session.config:
            self.session.vars['quotas'] = self.session.config['quotas']


class Group(BaseGroup):
    """Group for Quota."""

    quotas = models.CharField(blank=True, null=True)
    current = models.CharField(blank=True, null=True, default=0)
    initialized = models.BooleanField(default=False)

    def init_quotas(self, data):
        """Initialize quota count by serializing entry data."""
        if self.initialized is False:
            self.quotas = json.dumps(data)
            self.initialized = True

    def get_quotas(self, key=None):
        """
        Return deserialized quotas.

        If a key was passed and found in them, return the related value.
        """
        if self.quotas is None:
            self.init_quotas(self.session.vars['quotas'])

        quotas = json.loads(self.quotas)
        if key:
            for quota in quotas:
                if key in quota:
                    return quota
        return quotas

    def set_quotas(self, key, value):
        """Update the quota count."""
        quotas = self.get_quotas()
        for quota in quotas:
            if key in quota:
                quota[key]['current'] = value
                break


class Player(BasePlayer):
    """Player for Quota."""

    pass
