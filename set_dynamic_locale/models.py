# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
from django.utils.translation import activate, get_language
import otree
# </standard imports>

author = 'Davy Peter Braun <davy.braun@sciencespo.fr>'

doc = """
Dynamically set locale for the experiment, based on data set in the
experiment config.<br>Falls back to default locale.
"""


class Constants(BaseConstants):
    name_in_url = 'set_dynamic_locale'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):

    def before_session_starts(self):
        """Check locale from config and apply it."""
        if 'language_code' in self.session.config:
            self.session.vars['lang'] = (
                self.session.config['language_code'][:2]
            )
            activate(self.session.config['language_code'])
        else:
            self.session.vars['lang'] = 'en-us'
        print('set_dynamic_locale language code: ', get_language())

        if self.session.vars['lang'] == 'en-us':
            otree.settings.REAL_WORLD_CURRENCY_CODE = 'EUR'
        elif self.session.vars['lang'] == 'fr-fr':
            otree.settings.REAL_WORLD_CURRENCY_CODE = 'EUR'
        elif self.session.vars['lang'] == 'ko-kr':
            otree.settings.REAL_WORLD_CURRENCY_CODE = 'KRW'
        else:
            otree.settings.REAL_WORLD_CURRENCY_CODE = 'EUR'


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
