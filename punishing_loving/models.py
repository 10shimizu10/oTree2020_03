
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
	name_in_url = 'punishing_loving'
	players_per_group = None
	num_rounds = 1
class Subsession(BaseSubsession):
	pass
class Group(BaseGroup):
	pass
class Player(BasePlayer):
	forgiving = models.IntegerField(choices=[[1, '1 – Strongly disagree'], [2, '2 – Disagree'], [3, '3 – Somewhat disagree'], [4, '4 – Neither agree or disagree'], [5, '5 – Somewhat agree'], [6, '6 – Agree'], [7, '7 – Strongly agree']], label='The word "forgiving" applies to my conception of God.')
	loving = models.IntegerField(choices=[[1, '1 – Strongly disagree '], [2, '2 – Disagree '], [3, '3 – Somewhat disagree '], [4, '4 – Neither agree or disagree'], [5, '5 – Somewhat agree'], [6, '6 – Agree'], [7, '7 – Strongly agree']], label='The word "loving" applies to my conception of God.')
	compassionate = models.IntegerField(choices=[[1, '1 – Strongly disagree'], [2, '2 – Disagree'], [3, '3 – Somewhat disagree'], [4, '4 – Neither agree or disagree'], [5, '5 – Somewhat agree '], [6, '6 – Agree'], [7, '7 – Strongly agree']], label='The word "compassionate" applies to my conception of God.')
	gentle = models.IntegerField(choices=[[1, '1 – Strongly disagree'], [2, '2 – Disagree'], [3, '3 – Somewhat disagree'], [4, '4 – Neither agree or disagree'], [5, '5 – Somewhat agree'], [6, '6 – Agree'], [7, '7 – Strongly agree']], label='The word "gentle" applies to my conception of God.')
	kind = models.IntegerField(choices=[[1, '1 – Strongly disagree'], [2, '2 – Disagree'], [3, '3 – Somewhat disagree'], [4, '4 – Neither agree or disagree'], [5, '5 – Somewhat agree'], [6, '6 – Agree'], [7, '7 – Strongly agree']], label='The word "kind" applies to my conception of God.')
	comforting = models.IntegerField(choices=[[1, '1 – Strongly disagree'], [2, '2 – Disagree'], [3, '3 – Somewhat disagree'], [4, '4 – Neither agree or disagree'], [5, '5 – Somewhat agree'], [6, '6 – Agree'], [7, '7 – Strongly agree']], label='The word "comforting" applies to my conception of God.')
	peaceful = models.IntegerField(choices=[[1, '1 – Strongly disagree'], [2, '2 – Disagree'], [3, '3 – Somewhat disagree'], [4, '4 – Neither agree or disagree'], [5, '5 – Somewhat agree'], [6, '6 – Agree'], [7, '7 – Strongly agree']], label='The word "peaceful" applies to my conception of God.')
	vengeful = models.IntegerField(choices=[[1, '1 – Strongly disagree'], [2, '2 – Disagree'], [3, '3 – Somewhat disagree'], [4, '4 – Neither agree or disagree '], [5, '5 – Somewhat agree'], [6, '6 – Agree'], [7, '7 – Strongly agree ']], label='The word "vengeful" applies to my conception of God.')
	harsh = models.IntegerField(choices=[[1, '1 – Strongly disagree'], [2, '2 – Disagree'], [3, '3 – Somewhat disagree'], [4, '4 – Neither agree or disagree'], [5, '5 – Somewhat agree'], [6, '6 – Agree'], [7, '7 – Strongly agree']], label='The word "harsh" applies to my conception of God.')
	fearsome = models.IntegerField(choices=[[1, '1 – Strongly disagree'], [2, '2 – Disagree'], [3, '3 – Somewhat disagree'], [4, '4 – Neither agree or disagree'], [5, '5 – Somewhat agree'], [6, '6 – Agree'], [7, '7 – Strongly agree']], label='The word "fearsome" applies to my conception of God.')
	angry = models.IntegerField(choices=[[1, '1 – Strongly disagree'], [2, '2 – Disagree'], [3, '3 – Somewhat disagree'], [4, '4 – Neither agree or disagree'], [5, '5 – Somewhat agree '], [6, '6 – Agree'], [7, '7 – Strongly agree']], label='The word "angry" applies to my conception of God.')
	punishing = models.IntegerField(choices=[[1, '1 – Strongly disagree'], [2, '2 – Disagree'], [3, '3 – Somewhat disagree'], [4, '4 – Neither agree or disagree'], [5, '5 – Somewhat agree'], [6, '6 – Agree'], [7, '7 – Strongly agree']], label='The word "punishing" applies to my conception of God.')
	jealous = models.IntegerField(choices=[[1, '1 – Strongly disagree '], [2, '2 – Disagree'], [3, '3 – Somewhat disagree'], [4, '4 – Neither agree or disagree'], [5, '5 – Somewhat agree'], [6, '6 – Agree'], [7, '7 – Strongly agree']], label='The word "jealous" applies to my conception of God.')
	terrifying = models.IntegerField(choices=[[1, '1 – Strongly disagree'], [2, '2 – Disagree'], [3, '3 – Somewhat disagree'], [4, '4 – Neither agree or disagree'], [5, '5 – Somewhat agree'], [6, '6 – Agree'], [7, '7 – Strongly agree']], label='The word "terrifying" applies to my conception of God.')