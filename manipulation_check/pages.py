
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Survey6(Page):
	form_model = 'player'
	form_fields = ['sports']
page_sequence = [Survey6]