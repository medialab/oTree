from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, safe_json
)


author = 'Davy Peter Braun <davy.braun@sciencespo.fr>'

doc = """
Introduction to the Trustlab experiment.
"""


class Constants(BaseConstants):
    name_in_url = 'introduction'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    """Subsession for Introduction."""

    def before_session_starts(self):
        """Set treatment of the game (see settings.py) as global var."""
        self.session.vars['redirects'] = self.session.config['quota_redirects']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
