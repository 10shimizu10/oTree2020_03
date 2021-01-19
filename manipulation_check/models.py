
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
	name_in_url = 'manipulation_check'
	players_per_group = None
	num_rounds = 1
class Subsession(BaseSubsession):
	pass
class Group(BaseGroup):
	pass
class Player(BasePlayer):
	sports = models.StringField(choices=[['0', '---------'], ['skiing', 'skiing'], ['soccer', 'soccer'], ['snowboarding', 'snowboarding'], ['running', 'running'], ['hockey', 'hockey'], ['football', 'football'], ['swimming', 'swimming'], ['tennis', 'tennis'], ['basketball', 'basketball'], ['cycling', 'cycling']], initial='0', label='Most modern theories of decision making recognize the fact that decisions do not take place in a vacuum. Individual preferences and knowledge, along with situational variables can greatly impact the decision process. In order to facilitate our research on decision making we are interested in knowing certain factors about you, the decision maker. Specifically, we are interested in whether you actually take the time to read the directions; if not, then some of our manipulations that rely on changes in the instructions will be ineffective. So, in order to demonstrate that you have read the instructions, please ignore following choices. Instead, simply click on the next button. Thank you very much.')