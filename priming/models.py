
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
	name_in_url = 'priming'
	players_per_group = None
	num_rounds = 1
class Subsession(BaseSubsession):
	def creating_session(self):
		for player in self.get_players():
		    import random
		    player.fruit = random.choice(['apple', 'orange','banana'])
		
		
		
class Group(BaseGroup):
	pass
class Player(BasePlayer):
	apple = models.StringField(choices=[['yes', 'yes'], ['no', 'no']], label="Many thoughtful, reflective people maintain that moral rightness and wrongness are universal that they are independent of one's background or cultural upbringing. In other words, there are universal moral truths. Do you agree that moral rightness and wrongness are universal, that they are independent of one's background or cultural upbringing?")
	orange = models.StringField(choices=[['yes', 'yes'], ['no', 'no']], label="Many thoughtful, reflective people maintain that moral rightness and wrongness are relative—that they are determined solely by one's background or cultural upbringing. In other words, there are no universal moral truths.\xa0 Do you agree that moral rightness and wrongness are relative, that they are determined by one's background or cultural upbringing?")
	banana = models.StringField(choices=[['yes', 'yes'], ['no', 'no']], label='Many people agree that online studies have proven beneficial, as they speed up the process of data collection and allow participants to take part in the studies easily and from a variety of venues.\xa0 Do you agree that online studies are beneficial for researchers and participants?')
	fruit = models.StringField()