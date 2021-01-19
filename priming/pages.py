
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Apple(Page):
	form_model = 'player'
	form_fields = ['apple']
	def is_displayed(self):
		return self.player.fruit == 'apple'
class Orange(Page):
	form_model = 'player'
	form_fields = ['orange']
	def is_displayed(self):
		return self.player.fruit == 'orange'
class Banana(Page):
	form_model = 'player'
	form_fields = ['banana']
	def is_displayed(self):
		return self.player.fruit == 'banana'
page_sequence = [Apple, Orange, Banana]