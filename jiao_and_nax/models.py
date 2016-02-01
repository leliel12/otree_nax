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

author = 'Jiao, Nax and Juan'


ungettext("{} point", "{} points", 1)
ungettext("point", "points", 1)


doc = """
Instructions for an experiment on individual decision-making in a Cournot triopoly.

The instructions follow as closely as possible the instructions by
Friedman et al. 2015 and Huck et al. 1999. The main novelty of the experiment
is a more nuanced and fine-grained variation of the information setting,
ranging from “black box” (Burton-Chellew and West 2013, Nax et al. 2013) to
standard full information settings, placing Friedman et al. 2015 somewhere in
the middle.
"""


class Constants(BaseConstants):
    name_in_url = 'jiao_and_nax'
    players_per_group = None
    num_rounds = 1
    participation_fee = c(settings.SESSION_CONFIG_DEFAULTS["participation_fee"])
    ratio = settings.SESSION_CONFIG_DEFAULTS["real_world_currency_per_point"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
