
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = '\nOne player decides how to divide a certain amount between himself and the other\nplayer.\n\nSee: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness\nand the assumptions of economics." Journal of business (1986):\nS285-S300.\n\n'
class Constants(BaseConstants):
	name_in_url = 'dictator'
	players_per_group = None
	num_rounds = 1
	endowment = c(100)
	instructions_template = 'dictator/instructions.html'
class Subsession(BaseSubsession):
	def my_method(self):
		pass
class Group(BaseGroup):
	def payoffs(self):
		pass
class Player(BasePlayer):
	send = models.CurrencyField(max=Constants.endowment, min=0)
	def set_payoffs(self):
		self.payoff = Constants.endowment - self.send