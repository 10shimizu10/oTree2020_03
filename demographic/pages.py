
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Survey5(Page):
	form_model = 'player'
	form_fields = ['age', 'gender', 'religion']
page_sequence = [Survey5]