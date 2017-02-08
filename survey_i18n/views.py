# -*- coding: utf-8 -*-$
"""Views for Survey."""
from __future__ import division
from ._builtin import Page
from . import models
import math
from django.utils.translation import ugettext_lazy as _


def vars_for_all_templates(self):
    """Provide global template variables."""
    return {
        'lang': self.session.vars['lang']
    }


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
        'satisfied_with_cultural_facilities',
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
        'your_nationality',
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
        'what_best_describes_your_situation'
    ]


class Survey33(Page):
    form_model = models.Player
    form_fields = [
        'do_you_currently_work_in_the'
    ]


class Survey34(Page):
    form_model = models.Player
    form_fields = [
        'i_assume_that_people_have_only_the_best_intentions'
    ]


#TODO: Get country quintiles for Slovenia
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


class Survey37(Page):
    form_model = models.Player
    form_fields = [
        'how_important_is_religion'
    ]


class Survey38(Page):
    form_model = models.Player
    form_fields = [
        'which_device_did_you_take_this_study_on',
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





# class Survey01(Page):
#     """Page 1 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_01_how_satisfied_are_you_with_life_as_a_whole',
#         '_01_would_you_say_that_most_people_can_be_trusted',
#         '_01_are_you_a_person_fully_prepared_to_take_risks'
#     ]


# class Survey02(Page):
#     """Page 2 of survey."""

#     form_model = models.Player
#     form_fields = [
#         # '_02_treats_you_unfairly',
#         '_02_treats_others_unfairly',
#         '_02_give_to_good_causes'
#     ]


# class Survey02A(Page):
#     """Page 2A of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_02A_altruism'
#     ]

#     def vars_for_template(self):
#         label = {
#             'fr': _(u'Imagine the following situation: you won 1000 euros \
# in a lottery. Considering your current situation, how much would you donate \
# to a good cause?'),
#             'en': _(u'Imagine the following situation: you won $1000 \
# in a lottery. Considering your current situation, how much would you donate \
# to a good cause?'),
#             'ko': _(u'Imagine the following situation: you won 1000 Won \
# in a lottery. Considering your current situation, how much would you donate \
# to a good cause?')
#         }

#         money = {
#             'fr': {
#                 'max': 1000,
#                 'currency': _(u'€')
#             },
#             'en': {
#                 'max': 1000,
#                 'currency': _(u'$')
#             },
#             'ko': {
#                 'max': 1200000,
#                 'currency': _(u'Won')
#             }
#         }

#         return {
#             'label': label[self.session.vars['lang']],
#             'money': money[self.session.vars['lang']]
#         }


# class Survey03(Page):
#     """Page 3 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_03_does_me_a_favor'
#     ]


# class Survey04(Page):
#     """Page 4 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_04_thank_you_gift'
#     ]

#     def vars_for_template(self):
#         labels = {
#             'fr': {
#                 'present_00': _(u'no present'),
#                 'present_05': _(u'the present worth 5 euros'),
#                 'present_10': _(u'the present worth 10 euros'),
#                 'present_15': _(u'the present worth 15 euros'),
#                 'present_20': _(u'the present worth 20 euros'),
#                 'present_25': _(u'the present worth 25 euros'),
#                 'present_30': _(u'the present worth 30 euros'),
#             },
#             'en': {
#                 'present_00': _(u'no present'),
#                 'present_05': _(u'the present worth $5'),
#                 'present_10': _(u'the present worth $10'),
#                 'present_15': _(u'the present worth $15'),
#                 'present_20': _(u'the present worth $20'),
#                 'present_25': _(u'the present worth $25'),
#                 'present_30': _(u'the present worth $30'),
#             },
#             'ko': {
#                 'present_00': _(u'no present'),
#                 'present_05': _(u'the present worth 5.000 Won'),
#                 'present_10': _(u'the present worth 10.000 Won'),
#                 'present_15': _(u'the present worth 15.000 Won'),
#                 'present_20': _(u'the present worth 20.000 Won'),
#                 'present_25': _(u'the present worth 25.000 Won'),
#                 'present_30': _(u'the present worth 30.000 Won'),
#             }
#         }
#         return {
#             'labels': labels[self.session.vars['lang']]
#         }


# class Survey04A(Page):
#     """Page 4 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_04A_try_to_help_each_other',
#         '_04A_try_to_take_advantage_of_you',
#         '_04A_can_be_justified'
#     ]


# class Survey04B(Page):
#     """Page 4 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_04B_your_family',
#         '_04B_your_neighbourhood',
#         '_04B_personally',
#         '_04B_meet_for_the_first_time',
#         '_04B_another_religion',
#         '_04B_another_nationality',
#     ]


# class Survey04C(Page):
#     """Page 4 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_04C_wallet',
#         '_04C_you_vote_in_the_last_national_election',
#         '_04C_good_at_math',
#     ]


# class Survey05(Page):
#     """Page 5 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_05_your_government',
#         '_05_the_parliament',
#         '_05_the_police',
#         '_05_the_media',
#         '_05_the_judicial_system',
#         '_05_financial_institutions'
#     ]

#     def vars_for_template(self):
#         instructions = {
#             'fr': _(u'When answering the following questions, please think about French institutions.'),
#             'en': _(u'When answering the following questions, please think about the US institutions.'),
#             'ko': _(u'When answering the following questions, please think about Korean institutions.'),
#         }
#         return {
#             'instructions': instructions[self.session.vars['lang']]
#         }


# class Survey06(Page):
#     """Page 6 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_06_public_institutions_deliver_services',
#         '_06_public_institutions_pursue_long_term_objectives',
#         '_06_people_working_in_public_institutions_ethical',
#         '_06_public_institutions_are_transparent',
#         '_06_public_institutions_treat_all_citizens_fairly'
#     ]


# class Survey07(Page):
#     """Page 7 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_07_what_is_your_date_of_birth',
#         '_07_what_is_your_gender',
#         '_07_all_the_people_who_live_in_the_same_household',
#         '_07_how_many_people_adults',
#         '_07_how_many_people_children',
#         '_07_which_country_were_you_born',
#         '_07_what_year_did_you_arrive_in_country',
#         '_07_do_you_live_in'
#     ]

#     def vars_for_template(self):
#         label_what_year = {
#             'fr': _(u'In what year did you arrive in France?'),
#             'en': _(u'In what year did you arrive in the US?'),
#             'ko': _(u'In what year did you arrive in Korea?'),
#         }

#         return {
#             'label_what_year': label_what_year[self.session.vars['lang']]
#         }


# class Survey08(Page):
#     """Page 8 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_08_highest_level_of_education_that_you_have_completed',
#     ]

#     def vars_for_template(self):
#         fields = {
#             'fr': {
#                 'f01': _(u'Aucun diplôme'),
#                 'f02': _(u'Brevet des collèges'),
#                 'f03': _(u'CAP BEP ou équivalent'),
#                 'f04': _(u'Baccalauréat'),
#                 'f05': _(u'Diplômé du supérieur court (BTS, DUT, etc.)'),
#                 'f06': _(u'Licence (Bac + 3)'),
#                 'f07': _(u'Master (Bac + 5) ou Doctorat')
#             },
#             'ko': {
#                 'f01': _(u'Less than high school'),
#                 'f02': _(u'High school'),
#                 'f03': _(u'Some college'),
#                 'f04': _(u'Diploma, trades certificate or other post school qualification other than university'),
#                 'f05': _(u'Undergraduate degree (e.g. BA, BS)'),
#                 'f06': _(u'Post-graduate degree'),
#                 'f07': ''
#             },
#             'en': {
#                 'f01': _(u'Less than high school'),
#                 'f02': _(u'High school'),
#                 'f03': _(u'Some college'),
#                 'f04': _(u'Diploma, trades certificate or other post school qualification other than university'),
#                 'f05': _(u'Undergraduate degree (e.g. BA, BS)'),
#                 'f06': _(u'Post-graduate degree'),
#                 'f07': ''
#             }
#         }

#         return {
#             'lang': self.session.vars['lang'],
#             'fields': fields[self.session.vars['lang']]
#         }


# class Survey09(Page):
#     """Page 9 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_09_which_of_these_best_describes_your_situation',
#         '_09_do_you_work_in_the',
#         '_09_people_only_have_the_best_intentions'
#     ]


# class Survey10(Page):
#     """Page 10 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_10_household_income'
#     ]


# class Survey10A(Page):
#     """Page 10 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_10A_household_income'
#     ]

#     def vars_for_template(self):
#         currency = {
#             'fr': _(u'€'),
#             'en': _(u'$'),
#             'ko': _(u'Won')
#         }

#         return {
#             'currency': currency[self.session.vars['lang']],
#             'dont_know': _(u"Don't know")
#         }


# class Survey10B(Page):
#     """Page 10 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_10B_household_income'
#     ]


# class Survey10C(Page):
#     """Page 10 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_10C_income'
#     ]

#     def vars_for_template(self):
#         currency = {
#             'fr': _(u'€'),
#             'en': _(u'$'),
#             'ko': _(u'Won')
#         }

#         return {
#             'currency': currency[self.session.vars['lang']],
#             'dont_know': _(u"Don't know")
#         }


# class Survey10D(Page):
#     """Page 10 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_10D_income'
#     ]

#     def vars_for_template(self):
#         round_to = 1000
#         values = {
#             'fr': {
#                 'A': 15000,
#                 'B': 20000,
#                 'C': 25000,
#                 'D': 32000
#             },
#             'en': {
#                 'A': 15000,
#                 'B': 20000,
#                 'C': 25000,
#                 'D': 32000
#             },
#             'ko': {
#                 'A': 13000000,
#                 'B': 20000000,
#                 'C': 25000000,
#                 'D': 34000000
#             }
#         }
#         value_adults = int(self.player._07_how_many_people_adults)
#         value_children = int(self.player._07_how_many_people_children)
#         household_size = math.sqrt(value_adults + value_children)
#         value_a = int(values[self.session.vars['lang']]['A'] * household_size)
#         value_b = int(values[self.session.vars['lang']]['B'] * household_size)
#         value_c = int(values[self.session.vars['lang']]['C'] * household_size)
#         value_d = int(values[self.session.vars['lang']]['D'] * household_size)
#         return {
#             'household_size': household_size,
#             'value_a': round((value_a) / round_to) * round_to,
#             'value_b': round((value_b) / round_to) * round_to,
#             'value_c': round((value_c) / round_to) * round_to,
#             'value_d': round((value_d) / round_to) * round_to
#         }


# class Survey10G(Page):
#     """Page 10 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_10G_religion',
#         '_10G_religion_B',
#         '_10G_income'
#     ]


# class Survey11(Page):
#     """Page 11 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_11_other_participants_are_real_persons',
#         '_11_earnings_will_be_calculated_in_euro',
#         '_11_you_read_the_descriptions_associated',
#         '_11_were_you_in_a_calm_environment',
#         '_11_have_you_ever_participated_in_another_study',
#         '_11_which_device_did_you_take_this_study',
#         '_11_which_browser'
#     ]


# class Survey12(Page):
#     """Page 12 of survey."""

#     form_model = models.Player
#     form_fields = [
#         '_12_final_comments'
#     ]


# class EndGame(Page):
#     """End of survey."""

#     pass


# page_sequence = [
#     Survey01,
#     Survey02,
#     # Survey02A,
#     Survey03,
#     # Survey04,
#     Survey04A,
#     Survey04B,
#     Survey04C,
#     Survey05,
#     Survey06,
#     Survey07,
#     Survey08,
#     Survey09,
#     Survey10,
#     Survey10A,
#     Survey10B,
#     Survey10C,
#     Survey10D,
#     Survey10G,
#     Survey11,
#     Survey12,
# ]
