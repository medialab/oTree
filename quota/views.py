# -*- coding: utf-8 -*-
"""Views for Quota."""
from ._builtin import Page
from . import models


def vars_for_all_templates(self):
    return {
        'quotas': self.group.get_quotas(),
        'label': self.participant.label,
        'total_population': self.group.total_population,
        'language_code': self.session.vars['language_code'],
        'redirects': self.session.vars['redirects']
    }


class Init(Page):
    """Entry page, where direction decision is made based on quota."""

    form_model = models.Group
    form_fields = ['income_groups', 'gender_age_groups']


class Entry(Page):
    """Entry page, where direction decision is made based on quota."""

    form_model = models.Group


page_sequence = [Init, Entry]
