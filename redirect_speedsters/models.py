from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, safe_json
)


author = 'Your name here'

doc = """
Redirect "speedsters" based on the value of `speedster_threshold`
in app setting (number of seconds below which one is considered a speedster).
<br>
It <strong>must</strong> be used in conjunction with apps timer_start and
timer_stop, <strong>after</strong> timer_stop.
"""


class Constants(BaseConstants):
    name_in_url = 'speed_check'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
