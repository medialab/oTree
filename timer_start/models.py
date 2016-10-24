from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, safe_json
)


author = 'Davy Peter Braun <davy.braun@sciencespo.fr>'

doc = """
Starts the global timer for the experiment.
Must be used in conjunction with, and <strong>before</strong> timer_stop app.
"""


class Constants(BaseConstants):
    name_in_url = 'timer_start'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    epoch = models.CharField(max_length=500, null=True, blank=True)
