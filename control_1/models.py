# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'control_1'
    players_per_group = None
    num_rounds = 60


class Subsession(BaseSubsession):
    pass

    #~ def before_session_starts(self):
        #~ if self.round_number != 1:
            #~ print self.round_number
            #~ self.match_players("perfect_strangers")


class Group(BaseGroup):

    def set_payoff(self):
        players = self.get_players()
        players.sort(key=lambda p: p.invest, reverse=True)
        for p in players:
            p.payoff = 10


class Player(BasePlayer):

    invest = models.CurrencyField(
        min=0, max=100, widget=widgets.SliderInput(),
        verbose_name="How many money do you want to invest?")
