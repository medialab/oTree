# -*- coding: utf-8 -*-$
"""Views for Survey."""
from __future__ import division
from ._builtin import Page
from . import models
# from django.utils.translation import ugettext_lazy as _


class Survey01(Page):
    """Page 1 of survey."""

    form_model = models.Player
    form_fields = [
        '_01_how_satisfied_are_you_with_life_as_a_whole',
        '_01_would_you_say_that_most_people_can_be_trusted',
        '_01_are_you_a_person_fully_prepared_to_take_risks'
    ]


class Survey02(Page):
    """Page 2 of survey."""

    form_model = models.Player
    form_fields = [
        '_02_people_are_only_looking_out_for_themselves',
        '_02_people_would_try_to_take_advantage_of_you',
        '_02_the_following_action_can_always_be_justified'
    ]


class Survey03(Page):
    """Page 3 of survey."""

    form_model = models.Player
    form_fields = [
        '_03_your_family',
        '_03_people_in_your_neighborhood',
        '_03_people_you_know_personally',
        '_03_people_you_meet_for_the_first_time',
        '_03_people_of_another_religion',
        '_03_people_of_another_nationality',
    ]


class Survey04(Page):
    """Page 4 of survey."""

    form_model = models.Player
    form_fields = [
        '_04_you_lost_a_wallet_or_a_purse',
        '_04_you_vote_in_the_last_national_election'
    ]


class Survey05(Page):
    """Page 5 of survey."""

    form_model = models.Player
    form_fields = [
        '_05_your_government',
        '_05_the_police',
        '_05_the_media'
    ]


class Survey06(Page):
    """Page 6 of survey."""

    form_model = models.Player
    form_fields = [
        '_06_public_institutions_deliver_services_in_the_best_way',
        '_06_public_institutions_pursue_long_term_objectives',
        '_06_people_working_in_public_institutions_ethical',
        '_06_public_institutions_are_transparent',
        '_06_public_institutions_treat_all_citizens_fairly'
    ]


class Survey07(Page):
    """Page 7 of survey."""

    form_model = models.Player
    form_fields = [
        '_07_what_is_your_date_of_birth',
        '_07_what_is_your_gender',
        '_07_all_the_people_who_live_in_the_same_household_as_you',
        '_07_which_country_were_you_born',
        '_07_what_year_did_you_arrive_in_France'
    ]


class Survey08(Page):
    """Page 8 of survey."""

    form_model = models.Player
    form_fields = [
        '_08_highest_level_of_education_that_you_have_completed',
        '_08_which_of_these_best_describes_your_situation',
    ]


class Survey09(Page):
    """Page 9 of survey."""

    form_model = models.Player
    form_fields = [
        '_09_do_you_work_in_the',
        '_09_would_you_say_that_most_people_can_be_trusted',
        '_09_got_income_in_the_last_12_months_ending_today'
    ]


class Survey10(Page):
    """Page 10 of survey."""

    form_model = models.Player
    form_fields = [
        '_10_what_was_your_total_income',
        '_10_are_you'
    ]


class Survey11(Page):
    """Page 11 of survey."""

    form_model = models.Player
    form_fields = [
        '_11_other_participants_are_real_persons',
        '_11_earnings_will_be_calculated_in_euro',
        '_11_you_read_the_descriptions_associated',
        '_11_were_you_in_a_calm_environment',
        '_11_have_you_ever_participated_in_another_study',
        '_11_which_device_did_you_take_this_study'
    ]


class EndGame(Page):
    """End of survey."""

    pass


page_sequence = [
    Survey01,
    Survey02,
    Survey03,
    Survey04,
    Survey05,
    Survey06,
    Survey07,
    Survey08,
    Survey09,
    Survey10,
    Survey11,
    EndGame
]
