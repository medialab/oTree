# -*- coding: utf-8 -*-$
"""Views for Survey."""
from __future__ import division
from ._builtin import Page
from . import models


def vars_for_all_templates(self):
    """Return variables for all templates."""
    return {
        'q_1_7_label_1': 'Your family',
        'q_1_7_label_2': 'People in your neighborhood',
        'q_1_7_label_3': 'People you know personally',
        'q_1_7_label_4': 'People you meet for the first time',
        'q_1_7_label_5': 'People of another religion',
        'q_1_7_label_6': 'People of another nationality',
        'q_2_1_label_1': 'Your government',
        'q_2_1_label_2': 'The police',
        'q_2_1_label_3': 'The media',
        'q_2_2_label_1': 'Public institutions deliver public \
services in the best possible way',
        'q_2_2_label_2': 'Public institutions pursue long term objectives',
        'q_2_2_label_3': 'People working in public institutions \
behave according to ethical standards aimed at avoiding corruption',
        'q_2_2_label_4': 'Public institutions are transparent',
        'q_2_2_label_5': 'Public institutions treat all citizens \
fairly regardless of their gender, race, age or economic condition equally',
    }


class TrustAndTrustingBehaviour1(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_1']


class TrustAndTrustingBehaviour2(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_2']


class TrustAndTrustingBehaviour3(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_3']


class TrustAndTrustingBehaviour4(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_4']


class TrustAndTrustingBehaviour5(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_5']


class TrustAndTrustingBehaviour6(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_6']


class TrustAndTrustingBehaviour7(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = [
        'q_1_7_1', 'q_1_7_2', 'q_1_7_3', 'q_1_7_4', 'q_1_7_5', 'q_1_7_6'
    ]


class TrustAndTrustingBehaviour8(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_8']


class TrustAndTrustingBehaviour9(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_9']


class TrustInInstitution1(Page):
    """Page for Trust In Institution."""

    form_model = models.Player
    form_fields = ['q_2_1']


class TrustInInstitution2(Page):
    """Page for Trust In Institution."""

    form_model = models.Player
    form_fields = ['q_2_2']


class Demographics1(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_birthdate']


class Demographics2(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_gender']


class Demographics3(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_household']


class Demographics4(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_country']


class Demographics5(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_country_year']


class Demographics6(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_country_citizenship']


class Demographics7(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_education']


class Demographics8(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_situation']


class Demographics9(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_work_sector']


class Demographics10(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_trust']


class Demographics11(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_income_sources']


class Demographics12(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_income_total']


class Demographics13(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_religion']


class Demographics14(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_jewish']


class WrapUp1(Page):
    """Survey wrap-up page."""

    form_model = models.Player
    form_fields = ['q_4_1']


class WrapUp2(Page):
    """Survey wrap-up page."""

    form_model = models.Player
    form_fields = ['q_4_2']


class WrapUp3(Page):
    """Survey wrap-up page."""

    form_model = models.Player
    form_fields = ['q_4_3']


class WrapUp4(Page):
    """Survey wrap-up page."""

    form_model = models.Player
    form_fields = ['q_4_4']


class WrapUp5(Page):
    """Survey wrap-up page."""

    form_model = models.Player
    form_fields = ['q_4_5']


page_sequence = [
    TrustAndTrustingBehaviour1,
    TrustAndTrustingBehaviour2,
    TrustAndTrustingBehaviour3,
    TrustAndTrustingBehaviour4,
    TrustAndTrustingBehaviour5,
    TrustAndTrustingBehaviour6,
    TrustAndTrustingBehaviour7,
    TrustAndTrustingBehaviour8,
    TrustAndTrustingBehaviour9,
    TrustInInstitution1,
    TrustInInstitution2,
    Demographics1,
    Demographics2,
    Demographics3,
    Demographics4,
    Demographics5,
    Demographics6,
    Demographics7,
    Demographics8,
    Demographics9,
    Demographics10,
    Demographics11,
    Demographics12,
    Demographics13,
    Demographics14,
    WrapUp1,
    WrapUp2,
    WrapUp3,
    WrapUp4,
    WrapUp5
]
