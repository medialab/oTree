# -*- coding: utf-8 -*-
"""Test bot for Public Goods."""

from __future__ import division
import random
from ._builtin import Bot
from .models import Constants
from . import views


class PlayerBot(Bot):
    """Player test bot for Public Goods."""

    def play_round(self):
        """Play test round."""
        self.submit(views.Introduction)
        self.submit(views.Question, {"question": 92})
        self.submit(views.Feedback)
        self.submit(
            views.Contribute, {
                "contribution": random.choice(
                    range(0, int(Constants.endowment)))
            }
        )
        self.submit(views.Results)

    def validate_play(self):
        """Assert tests for test round."""
        pass
