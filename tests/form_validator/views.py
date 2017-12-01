from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    def is_displayed(self):
        return self.player.admin == True

    def before_next_page(self):
        print('******************************************************')
        print ('Se ejecuta cuando se da clic en el boton de otree, antes de pasar a la pagina siguiente')
        print('******************************************************')

    def vars_for_template(self):
        print('******************************************************')
        print ('Se ejecuta cuando se accede a la pagina actual (incluida las recargas)')
        print ('a las variables en el tempalte se acceden con {{ variable }}')
        print('******************************************************')
        return{
            'variable1': 'algo',
            'variable2': 100
        }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    MyPage,
    ResultsWaitPage,
    Results
]
