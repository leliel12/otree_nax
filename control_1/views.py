# -*- coding: utf-8 -*-
from __future__ import division

from django.conf import settings

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
        if self.subsession.round_number == Constants.num_rounds:
            self.group.select_random_round()


class Results(Page):

    def is_displayed(self):
        return True


class FinalResults(Page):

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        participation_fee = float(settings.SESSION_CONFIG_DEFAULTS["participation_fee"])
        ratio = float(settings.SESSION_CONFIG_DEFAULTS["real_world_currency_per_point"])
        final_payment = (participation_fee + float(self.player.selected_payoff_to_pay)) * ratio
        return {"final_payment": final_payment}


page_sequence = [
    Instructions, Question, ResultsWaitPage, Results, FinalResults
]
