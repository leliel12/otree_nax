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

from django.conf import settings
from django.utils.translation import ungettext,  ugettext_lazy as _

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'treatment_2'
    players_per_group = None
    num_rounds = 60
    phase_2_round_start = 21
    phase_3_round_start = 41
    invest_limits = 0, 100


class Subsession(BaseSubsession):

    def before_session_starts(self):
        if self.round_number != 1:
            self.match_players("perfect_strangers")


class Group(BaseGroup):

    def set_payoff(self):
        players = self.get_players()
        quantities_total = sum(p.invest for p in players)
        price = (3000 / quantities_total) - 10.
        for p in players:
            p.payoff = price * p.invest + 100


class Player(BasePlayer):

    invest = models.IntegerField(
        choices=range(Constants.invest_limits[0], Constants.invest_limits[1] + 1),
        verbose_name=_("How much money do you want to invest?"))
