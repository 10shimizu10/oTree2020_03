
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Last_Page(Page):
	form_model = 'player'
page_sequence = [Last_Page]