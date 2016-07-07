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
        'total_time',
        '_01_how_satisfied_are_you_with_life_as_a_whole',
        '_01_would_you_say_that_most_people_can_be_trusted',
        '_01_are_you_a_person_fully_prepared_to_take_risks'
    ]


class Survey02(Page):
    """Page 2 of survey."""

    form_model = models.Player
    form_fields = [
        '_02_treats_you_unfairly',
        '_02_treats_others_unfairly',
        '_02_give_to_good_causes'
    ]


class Survey02A(Page):
    """Page 2A of survey."""

    form_model = models.Player
    form_fields = [
        '_02A_altruism'
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


class Survey04A(Page):
    """Page 4 of survey."""

    form_model = models.Player
    form_fields = [
        '_04A_try_to_help_each_other',
        '_04A_try_to_take_advantage_of_you',
        '_04A_can_be_justified'
    ]


class Survey04B(Page):
    """Page 4 of survey."""

    form_model = models.Player
    form_fields = [
        '_04B_your_family',
        '_04B_your_neighbourhood',
        '_04B_personally',
        '_04B_meet_for_the_first_time',
        '_04B_another_religion',
        '_04B_another_nationality',
    ]


class Survey04C(Page):
    """Page 4 of survey."""

    form_model = models.Player
    form_fields = [
        '_04C_wallet',
        '_04C_you_vote_in_the_last_national_election',
        '_04C_good_at_math',
    ]


class Survey05(Page):
    """Page 5 of survey."""

    form_model = models.Player
    form_fields = [
        '_05_your_government',
        '_05_the_police',
        '_05_the_media',
        '_05_the_judicial_system',
        '_05_financial_institutions'
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
        '_07_all_the_people_who_live_in_the_same_household',
        '_07_how_many_people_adults',
        '_07_how_many_people_children',
        '_07_which_country_were_you_born',
        '_07_what_year_did_you_arrive_in_country',
        '_07_do_you_live_in'
    ]


class Survey08(Page):
    """Page 8 of survey."""

    form_model = models.Player
    form_fields = [
        '_08_highest_level_of_education_that_you_have_completed',
    ]


class Survey09(Page):
    """Page 9 of survey."""

    form_model = models.Player
    form_fields = [
        '_09_which_of_these_best_describes_your_situation',
        '_09_do_you_work_in_the',
        '_09_people_only_have_the_best_intentions'
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
        '_11_which_device_did_you_take_this_study',
        'total_time'
    ]

    def vars_for_template(self):
        """Make data available in template."""
        return {'start_time': self.player.total_time}


class EndGame(Page):
    """End of survey."""

    form_fields = ['total_time']

    def vars_for_template(self):
        """Make data available in template."""
        return {'start_time': self.player.total_time}


page_sequence = [
    Survey01,
    Survey02,
    Survey02A,
    Survey03,
    Survey04,
    Survey04A,
    Survey04B,
    Survey04C,
    Survey05,
    Survey06,
    Survey07,
    Survey08,
    Survey09,
    Survey10,
    Survey11,
    # EndGame
]
