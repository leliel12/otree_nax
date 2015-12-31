# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1


class Question(Page):

    form_model = models.Player
    form_fields = ["invest"]


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoff()


class Results(Page):

    def is_displayed(self):
        pass


page_sequence = [
    Instructions, Question, ResultsWaitPage, Results
]
