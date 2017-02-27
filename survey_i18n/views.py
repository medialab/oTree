# -*- coding: utf-8 -*-$
"""Views for Survey."""
from __future__ import division
from ._builtin import Page
from . import models
import math
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _


def vars_for_all_templates(self):
    """Provide global template variables."""
    return {
        'lang': self.session.vars['lang'] or get_language()
    }


# TODO: update "Which device are you taking this study on?" in SL
class Survey00(Page):

    form_model = models.Player
    form_fields = [
        'which_device_did_you_take_this_study_on'
    ]


class Survey01(Page):

    form_model = models.Player
    form_fields = [
        'overall_how_satisfied_are_you_with_life',
        'would_you_say_that_most_people_can_be_trusted'
    ]


class Survey02(Page):

    form_model = models.Player
    form_fields = [
        'to_punish_someone_who_treats_others_unfairly',
        'to_give_to_good_causes'
    ]


class Survey03(Page):

    form_model = models.Player
    form_fields = [
        'fully_prepared_or_avoid_to_take_risks',
        'when_someone_does_me_a_favor'
    ]


class Survey04(Page):

    form_model = models.Player
    form_fields = [
        'people_are_looking_for_themselves_or_try_to_help_others',
        'people_would_take_advantage_of_you_or_be_fair',
        'receiving_government_benefits_to_which_you_are_not_entitled',
        'cheating_on_taxes_if_you_have_a_chance'
    ]


class Survey05(Page):

    form_model = models.Player
    form_fields = [
        'how_much_do_you_trust_your_family',
        'how_much_do_you_trust_people_in_your_neighborhood',
        'how_much_do_you_trust_people_you_know_personally',
        'how_much_do_you_trust_people_you_meet_for_the_first_time',
        'how_much_do_you_trust_people_of_another_religion',
        'how_much_do_you_trust_people_of_another_nationality',
        'how_much_do_you_trust_people_who_immigrated',
        'how_much_do_you_trust_people_who_seek_refuge',
    ]


class Survey06(Page):

    form_model = models.Player
    form_fields = [
        'i_am_good_at_math',
        'lost_your_wallet',
        'did_you_vote'
    ]


class Survey07(Page):

    form_model = models.Player
    form_fields = [
        'how_much_do_you_trust_most_people_in_your_country'
    ]


class Survey08(Page):

    form_model = models.Player
    form_fields = [
        'trust_the_government',
        'trust_the_parliament',
        'trust_the_judicial_system',
        'trust_the_police',
        'trust_the_media',
        'trust_financial_institutions'
    ]


class Survey09(Page):

    form_model = models.Player
    form_fields = [
        'public_institutions_deliver_service_in_the_best_way',
        'public_institutions_pursue_long_term_objectives',
        'people_in_public_institutions_are_ethical_and_not_corrupt',
        'public_institutions_are_transparent',
        'public_institutions_treat_all_citizens_fairly'
    ]


class Survey10(Page):

    form_model = models.Player
    form_fields = [
        'satisfied_with_the_education_system',
        'satisfied_with_the_health_care_system',
        'satisfied_with_public_transport',
        'satisfied_with_child_care_services',
        'satisfied_with_welfare_benefits',
        'satisfied_with_public_housing',
        'satisfied_with_security_and_crime_prevention',
        'satisfied_with_environmental_issues',
        'satisfied_with_cultural_facilities'
    ]

class Survey10_5(Page):

    form_model = models.Player
    form_fields = [
        'complaint_about_quality_of_public_service_likely_resolved',
        'technology_speed_up_likely_to_be_adopted'
    ]

class Survey11(Page):

    form_model = models.Player
    form_fields = [
        'information_about_administrative_producedure_easy_to_find',
        'decision_affecting_community_likely_to_be_consulted_upon'
    ]


class Survey12(Page):

    form_model = models.Player
    form_fields = [
        'start_a_business_conditions_stability',
        'natural_disaster_shelter_and_clothing_availability'
    ]


class Survey13(Page):

    form_model = models.Player
    form_fields = [
        'guilty_high_ranking_gov_employee_likely_prosecuted',
        'accept_or_refuse_administrative_procedures_speed_up_bribe',
        'high_ranking_gov_employee_accepts_well_paid_private_sector_job',
        'accept_or_refuse_public_procurement_tender_allocation_bribe'
    ]


class Survey14(Page):

    form_model = models.Player
    form_fields = [
        'social_minority_citizen_likely_to_be_treated_equally'
    ]


class Survey15(Page):

    form_model = models.Player
    form_fields = [
        'expenditure_general_public_services_and_public_debt',
        'expenditure_defense_and_public_order',
        'expenditure_infrastucture_and_economic_affair',
        'expenditure_health_and_environmental_protection',
        'expenditure_education_and_culture',
        'expenditure_social_protection_and_housing'
    ]


class Survey16(Page):

    form_model = models.Player
    form_fields = [
        'resources_top_1_percent',
        'resources_next_9_percent',
        'resources_next_40_percent',
        'resources_bottom_50_percent'
    ]


class Survey17(Page):

    form_model = models.Player
    form_fields = [
        'how_many_children_part_of_the_richest_segment',
        'not_much_or_plenty_of_opportunity'
    ]


class Survey18(Page):

    form_model = models.Player
    form_fields = [
        'household_expectations_for_the_12_months_to_come',
        'likely_to_still_have_a_job_in_6_months',
        'likely_to_find_a_job_with_similar_salary_in_6_months'
    ]


class Survey19(Page):

    form_model = models.Player
    form_fields = [
        'government_should_encourage_or_discourage_international_trade'
    ]


class Survey20(Page):

    form_model = models.Player
    form_fields = [
        'how_much_info_from_tv',
        'how_much_info_from_internet',
        'how_much_info_from_family_friends_coworkers',
        'how_much_info_from_social_networks',
        'how_much_info_from_print_media'
    ]


class Survey21(Page):

    form_model = models.Player
    form_fields = [
        'most_likely_threatening_privacy_hackers',
        'most_likely_threatening_privacy_domestic_gov_agencies',
        'most_likely_threatening_privacy_foreign_gov_agencies',
        'most_likely_threatening_privacy_corporations'
    ]


class Survey22(Page):

    form_model = models.Player
    form_fields = [
        'estimation_of_foreigners_in_neighborhood'
    ]


class Survey23(Page):

    form_model = models.Player
    form_fields = [
        'statement_agreement_immigrants_are_not_integrated',
        'statement_agreement_culture_is_undermined_by_immigrants'
    ]


class Survey24(Page):

    form_model = models.Player
    form_fields = [
        'how_often_do_you_get_together_with_friends',
        'how_often_do_you_participate_in_voluntary_activities'
    ]


class Survey25(Page):

    form_model = models.Player
    form_fields = [
        'how_strongly_do_you_feel_connected_to_your_neighborhood'
    ]


class Survey26(Page):

    form_model = models.Player
    form_fields = [
        'voting_can_or_cannot_make_a_difference',
        'political_left_center_right'
    ]


class Survey27(Page):

    form_model = models.Player
    form_fields = [
        'date_of_birth',
        'gender'
    ]


class Survey28(Page):

    form_model = models.Player
    form_fields = [
        'how_many_people_in_your_household'
    ]


class Survey29(Page):

    form_model = models.Player
    form_fields = [
        'which_country_were_you_born',
        'what_is_your_nationality',
        'when_did_you_arrive_in_country',
        'were_your_parents_born_in_country'
    ]


class Survey30(Page):

    form_model = models.Player
    form_fields = [
        'do_you_live_in_a'
    ]


class Survey31(Page):

    form_model = models.Player
    form_fields = [
        'highest_level_of_education_you_have_completed'
    ]


class Survey32(Page):

    form_model = models.Player
    form_fields = [
        'highest_level_of_education_your_parent_has_completed',
    ]


class Survey33(Page):

    form_model = models.Player
    form_fields = [
        'what_best_describes_your_situation',
        'do_you_currently_work_in_the'
    ]


class Survey34(Page):

    form_model = models.Player
    form_fields = [
        'i_assume_that_people_have_only_the_best_intentions'
    ]


class Survey35(Page):

    form_model = models.Player
    form_fields = [
        'individual_income_in_the_last_12_months',
        'individual_income_confirmation'
    ]


class Survey36(Page):

    form_model = models.Player
    form_fields = [
        'household_income_in_the_last_12_months',
        'household_income_confirmation'
    ]

    def vars_for_template(self):
        """Calculate dynamic ranges based on previous household size answer."""
        round_to = 1000

        values = {
            'sl': {
                'A': 9000,
                'B': 12500,
                'C': 15000,
                'D': 20000,
            },
            'fr': {
                'A': 15000,
                'B': 20000,
                'C': 25000,
                'D': 32000
            },
            'en': {
                'A': 15000,
                'B': 20000,
                'C': 25000,
                'D': 32000
            },
            'ko': {
                'A': 13000000,
                'B': 20000000,
                'C': 25000000,
                'D': 34000000
            }
        }

        try:
            n = math.sqrt(int(self.player.how_many_people_in_your_household))
        except:
            n = math.sqrt(10)

        v = values[self.session.vars['lang']]

        a = round(int(v['A'] * n) / round_to) * round_to
        b = round(int(v['B'] * n) / round_to) * round_to
        c = round(int(v['C'] * n) / round_to) * round_to
        d = round(int(v['D'] * n) / round_to) * round_to

        return {
            'choices': [
                _(u"€{0} - €{1}".format('0', str(a))),
                _(u"€{0} - €{1}".format(str(a + 1), str(b))),
                _(u"€{0} - €{1}".format(str(b + 1), str(c))),
                _(u"€{0} - €{1}".format(str(c + 1), str(d))),
                _(u"> €{0}".format(str(d + 1)))
            ]
        }


class Survey37(Page):

    form_model = models.Player
    form_fields = [
        'how_important_is_religion'
    ]


class Survey38(Page):

    form_model = models.Player
    form_fields = [
        'open_comment'
    ]


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
    Survey10_5,
    Survey11,
    Survey12,
    Survey13,
    Survey14,
    Survey15,
    Survey16,
    Survey17,
    Survey18,
    Survey19,
    Survey20,
    Survey21,
    Survey22,
    Survey23,
    Survey24,
    Survey25,
    Survey26,
    Survey27,
    Survey28,
    Survey29,
    Survey30,
    Survey31,
    Survey32,
    Survey33,
    Survey34,
    Survey35,
    Survey36,
    Survey37,
    Survey38
]
