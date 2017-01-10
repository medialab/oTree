from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, safe_json
)


author = 'Your name here'

doc = """
Enforces the presence of a <strong>participant_label</strong> variable in the URL used by the participant.
<br>No URL stops the progression right away.
"""


class Constants(BaseConstants):
    name_in_url = 'mandatory_participant_label'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
