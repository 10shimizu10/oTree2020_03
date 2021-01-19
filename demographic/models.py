
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
	name_in_url = 'demographic'
	players_per_group = None
	num_rounds = 1
class Subsession(BaseSubsession):
	pass
class Group(BaseGroup):
	pass
class Player(BasePlayer):
	age = models.IntegerField(label='What is your age', max=125, min=13)
	gender = models.StringField(choices=[['Male', 'Male'], ['Female', 'Female']], label='What is your gender', widget=widgets.RadioSelect)
	religion = models.StringField(choices=[['Protestant Christian', 'Protestant Christian'], ['Roman Catholic', 'Roman Catholic'], ['Evangelical Christian', 'Evangelical Christian'], ['Other Christian', 'Other Christian'], ['Jewish', 'Jewish'], ['Muslim', 'Muslim'], ['Hindu', 'Hindu'], ['Buddhist', 'Buddhist'], ['other religion', 'other religion'], ['No religion', 'No religion']], label='What is your religion?')