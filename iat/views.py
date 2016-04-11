# -*- coding: utf-8 -*-
from __future__ import division

from . import models
from ._builtin import Page

def vars_for_all_templates(self):
    print self.session.vars['order']
    return {
        'instructions': 'iat/Instructions.html',
        'data': self.session.vars['data'],
        'order': self.session.vars['order']
    }

class Introduction(Page):

    template_name = 'global/Introduction.html'


class EndGame(Page):
    pass


class IAT(Page):
    form_model = models.Player
    form_fields = ['iat_results']


page_sequence = [Introduction, IAT, EndGame]
