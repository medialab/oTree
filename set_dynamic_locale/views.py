# -*- coding: utf-8 -*-
from __future__ import division

from ._builtin import Page
from django.utils import translation


class SetLocale(Page):

    def vars_for_templates(self):
        lang = translation.get_language()
        return {
            'lang': lang
        }

class Results(Page):
    pass


page_sequence = [
    SetLocale
]
