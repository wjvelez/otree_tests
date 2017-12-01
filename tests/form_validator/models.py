from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Se tienen 5 jugadores, al inciiar la sesion se sortea un administrador del grupo,
solo el administrador debe asignar montos de castigo a los demas jugadores (a el no )


"""


import random

class Constants(BaseConstants):
    name_in_url = 'form_validator'
    players_per_group = 5
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for g in self.get_groups():
            g.admin = random.randint(1, Constants.players_per_group)
            for jugador in g.get_players():
                if jugador.id_in_group == g.admin:
                    jugador.admin = True
                else:
                    jugador.admin = False


class Group(BaseGroup):
    admin = models.IntegerField()


class Player(BasePlayer):
    admin = models.BooleanField()
    castigo = models.IntegerField(initial=0)
