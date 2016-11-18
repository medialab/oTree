# -*- coding: utf-8 -*-
"""Models for Quota."""

from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
from django.utils.translation import get_language
import json
import jsonfield
# from otree.common import Currency

doc = """
Quota calculator screening the user passing the experiments.
"""


class Constants(BaseConstants):
    """Constants for Quota."""

    name_in_url = 'quota'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    """Subsession for Quota."""

    def before_session_starts(self):
        """
        Parse information config.

        Store it in session vars. In the first view of the app,
        we will use it to initialize control data for quota monitoring.
        """
        if 'language_code' in self.session.config:
            self.session.vars['language_code'] = (
                self.session.config['language_code']
            )
        else:
            self.session.vars['language_code'] = {}

        if 'quota_redirects' in self.session.config:
            self.session.vars['redirects'] = (
                self.session.config['quota_redirects']
            )
        else:
            self.session.vars['redirects'] = {}

        if 'quota_total_population' in self.session.config:
            self.session.vars['total_population'] = (
                self.session.config['quota_total_population']
            )
        else:
            self.session.vars['total_population'] = {}

        # if 'quota_income_groups' in self.session.config:
        #     self.session.vars['income_groups'] = (
        #         self.session.config['quota_income_groups']
        #     )
        # else:
        #     self.session.vars['income_groups'] = {}

        if 'quota_gender_age_groups' in self.session.config:
            self.session.vars['gender_age_groups'] = (
                self.session.config['quota_gender_age_groups']
            )
        else:
            self.session.vars['gender_age_groups'] = {}


class Group(BaseGroup):
    """Group for Quota."""

    total_population = jsonfield.JSONField(blank=True, null=True)
    gender_age_groups = jsonfield.JSONField(blank=True, null=True)
    income_groups = jsonfield.JSONField(blank=True, null=True)

    initialized = models.BooleanField(default=False)

    def init_quotas(self, total_population, gender_age_groups):
        """Initialize quota count by serializing control data."""
        if self.initialized is False:
            self.save_quota_set('total_population', total_population)
            # self.save_quota_set('income_groups', income_groups)
            self.save_quota_set('gender_age_groups', gender_age_groups)
            self.initialized = True

    def get_quotas(self):
        """
        Return deserialized quotas.

        If a key was passed and found in them, return the related value.
        """
        if get_language()[:2] != 'ko':
            return ''

        # Initialize data on the very first call, if needed.
        if self.initialized is False:
            self.init_quotas(
                self.session.vars['total_population'],
                #self.session.vars['income_groups'],
                self.session.vars['gender_age_groups']
            )

        # Deserialize data.
        total_population = self.total_population
        # income_groups = self.income_groups
        gender_age_groups = self.gender_age_groups

        # First use json.dumps to ensure payload is a string,
        # Then return proper json content using json.loads
        if type(total_population) is dict:
            total_population = json.dumps(total_population)

        # if type(income_groups) is dict:
        #     income_groups = json.dumps(income_groups)

        if type(gender_age_groups) is dict:
            gender_age_groups = json.dumps(gender_age_groups)

        return {
            'total_population': json.loads(total_population),
            # 'income_groups': json.loads(income_groups),
            'gender_age_groups': json.loads(gender_age_groups)
        }

    def save_quota_set(self, fieldname, data):
        """Save serialized data to relevant field."""
        setattr(self, fieldname, json.dumps(data))

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
