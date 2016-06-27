# -*- coding: utf-8 -*-
"""Views for Quota."""
from ._builtin import Page
from . import models


class Init(Page):
    """Entry page, where direction decision is made based on quota."""

    form_model = models.Group
    form_fields = ['current']

    def vars_for_template(self):
        return {
            'quotas': self.group.get_quotas(),
            'label': self.participant.label
        }


class Entry(Page):
    """Entry page, where direction decision is made based on quota."""

    form_model = models.Group

    def vars_for_template(self):
        return {
            'quotas': self.group.get_quotas()
        }


page_sequence = [Init, Entry]
