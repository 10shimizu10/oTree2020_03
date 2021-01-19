
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
	form_model = 'player'
class Offer(Page):
	form_model = 'player'
	form_fields = ['send']
	def before_next_page(self):
		self.player.set_payoffs()
class Results(Page):
	form_model = 'player'
	def vars_for_template(self):
		return dict(offer=Constants.endowment - self.player.send)
page_sequence = [Introduction, Offer, Results]