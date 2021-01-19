
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
	name_in_url = 'GOD'
	players_per_group = None
	num_rounds = 1
class Subsession(BaseSubsession):
	pass
class Group(BaseGroup):
	pass
class Player(BasePlayer):
	GOD = models.IntegerField(label="Do you think God exist? Please answer from 0 (“I'm sure God doesn't exist”) to 100 (“I'm sure God exists”)", max=100, min=0)