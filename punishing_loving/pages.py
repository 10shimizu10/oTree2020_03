
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Survey3(Page):
	form_model = 'player'
	form_fields = ['forgiving', 'loving', 'compassionate', 'gentle', 'kind', 'comforting', 'peaceful', 'vengeful', 'harsh', 'fearsome', 'angry', 'punishing', 'jealous', 'terrifying']
page_sequence = [Survey3]