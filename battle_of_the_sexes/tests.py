# -*- coding: utf-8 -*-
from __future__ import division
from . import views
from ._builtin import Bot
import random
from otree.common import Money, money_range

class PlayerBot(Bot):

    def play(self):

        # random decision
        choice = random.choice(['Football', 'Opera'])

        self.submit(views.Decide, {"decision": choice})

        # results
        self.submit(views.Results)