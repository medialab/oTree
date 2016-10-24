from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, safe_json
)


author = 'Davy Peter Braun <davy.braun@sciencespo.fr>'

doc = """
Stops the global timer for the experiment.<br>
Must be used in conjunction with, and <strong>after</strong> timer_start app.
"""


class Constants(BaseConstants):
    name_in_url = 'timer_stop'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    epoch = models.CharField(max_length=500, null=True, blank=True)
    global_time_in_seconds = models.CharField(
        max_length=500, null=True, blank=True
    )
