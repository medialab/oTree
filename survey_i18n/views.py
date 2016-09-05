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

    def vars_for_template(self):
        label = {
            'fr': _(u'Imagine the following situation: you won 1000 euros \
in a lottery. Considering your current situation, how much would you donate \
to a good cause?'),
            'en': _(u'Imagine the following situation: you won $1000 \
in a lottery. Considering your current situation, how much would you donate \
to a good cause?'),
            'ko': _(u'Imagine the following situation: you won 1000 Won \
in a lottery. Considering your current situation, how much would you donate \
to a good cause?')
        }

        money = {
            'fr': {
                'max': 1000,
                'currency': _(u'€')
            },
            'en': {
                'max': 1000,
                'currency': _(u'$')
            },
            'ko': {
                'max': 1000000,
                'currency': _(u'Won')
            }
        }

        return {
            'label': label[self.session.vars['lang']],
            'money': money[self.session.vars['lang']]
        }


class Survey03(Page):
    """Page 3 of survey."""

    form_model = models.Player
    form_fields = [
        '_03_does_me_a_favor',
        '_03_treated_injustly',
    ]


class Survey04(Page):
    """Page 4 of survey."""

    form_model = models.Player
    form_fields = [
        '_04_thank_you_gift'
    ]

    def vars_for_template(self):
        labels = {
            'fr': {
                'present_00': _(u'no present'),
                'present_05': _(u'the present worth 5 euros'),
                'present_10': _(u'the present worth 10 euros'),
                'present_15': _(u'the present worth 15 euros'),
                'present_20': _(u'the present worth 20 euros'),
                'present_25': _(u'the present worth 25 euros'),
                'present_30': _(u'the present worth 30 euros'),
            },
            'en': {
                'present_00': _(u'no present'),
                'present_05': _(u'the present worth $5'),
                'present_10': _(u'the present worth $10'),
                'present_15': _(u'the present worth $15'),
                'present_20': _(u'the present worth $20'),
                'present_25': _(u'the present worth $25'),
                'present_30': _(u'the present worth $30'),
            },
            'ko': {
                'present_00': _(u'no present'),
                'present_05': _(u'the present worth 5.000 Won'),
                'present_10': _(u'the present worth 10.000 Won'),
                'present_15': _(u'the present worth 15.000 Won'),
                'present_20': _(u'the present worth 20.000 Won'),
                'present_25': _(u'the present worth 25.000 Won'),
                'present_30': _(u'the present worth 30.000 Won'),
            }
        }
        return {
            'labels': labels[self.session.vars['lang']]
        }


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
        '_05_the_parliament',
        '_05_the_police',
        '_05_the_media',
        '_05_the_judicial_system',
        '_05_financial_institutions'
    ]

    def vars_for_template(self):
        instructions = {
            'fr': _(u'When answering the following questions, please think about French institutions.'),
            'en': _(u'When answering the following questions, please think about the US institutions.'),
            'ko': _(u'When answering the following questions, please think about Korean institutions.'),
        }
        return {
            'instructions': instructions[self.session.vars['lang']]
        }


class Survey06(Page):
    """Page 6 of survey."""

    form_model = models.Player
    form_fields = [
        '_06_public_institutions_deliver_services',
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

    def vars_for_template(self):
        label_what_year = {
            'fr': _(u'In what year did you arrive in France?'),
            'en': _(u'In what year did you arrive in the US?'),
            'ko': _(u'In what year did you arrive in Korea?'),
        }

        return {
            'label_what_year': label_what_year[self.session.vars['lang']]
        }


class Survey08(Page):
    """Page 8 of survey."""

    form_model = models.Player
    form_fields = [
        '_08_highest_level_of_education_that_you_have_completed',
    ]

    def vars_for_template(self):
        fields = {
            'fr': {
                'f01': _(u'Aucun diplôme'),
                'f02': _(u'Brevet des collèges'),
                'f03': _(u'CAP BEP ou équivalent'),
                'f04': _(u'Baccalauréat'),
                'f05': _(u'Diplômé du supérieur court (BTS, DUT, etc.)'),
                'f06': _(u'Licence (Bac + 3)'),
                'f07': _(u'Master (Bac + 5) ou Doctorat')
            },
            'ko': {
                'f01': _(u'Less than high school'),
                'f02': _(u'High school'),
                'f03': _(u'Some college'),
                'f04': _(u'Diploma, trades certificate or other post school qualification other than university'),
                'f05': _(u'Undergraduate degree (e.g. BA, BS)'),
                'f06': _(u'Post-graduate degree'),
                'f07': ''
            },
            'en': {
                'f01': _(u'Less than high school'),
                'f02': _(u'High school'),
                'f03': _(u'Some college'),
                'f04': _(u'Diploma, trades certificate or other post school qualification other than university'),
                'f05': _(u'Undergraduate degree (e.g. BA, BS)'),
                'f06': _(u'Post-graduate degree'),
                'f07': ''
            }
        }

        return {
            'lang': self.session.vars['lang'],
            'fields': fields[self.session.vars['lang']]
        }


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
        '_10_main_ways_income',
        '_10_household_income'
    ]


class Survey10A(Page):
    """Page 10 of survey."""

    form_model = models.Player
    form_fields = [
        '_10A_household_income'
    ]

    def vars_for_template(self):
        currency = {
            'fr': _(u'€'),
            'en': _(u'$'),
            'ko': _(u'Won')
        }

        return {
            'currency': currency[self.session.vars['lang']],
            'dont_know': _(u"Don't know")
        }


class Survey10B(Page):
    """Page 10 of survey."""

    form_model = models.Player
    form_fields = [
        '_10B_household_income'
    ]


class Survey10C(Page):
    """Page 10 of survey."""

    form_model = models.Player
    form_fields = [
        '_10C_income'
    ]

    def vars_for_template(self):
        currency = {
            'fr': _(u'€'),
            'en': _(u'$'),
            'ko': _(u'Won')
        }

        return {
            'currency': currency[self.session.vars['lang']],
            'dont_know': _(u"Don't know")
        }


class Survey10D(Page):
    """Page 10 of survey."""

    form_model = models.Player
    form_fields = [
        '_10D_income'
    ]

    def vars_for_template(self):
        round_to = 1000
        values = {
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
        value_adults = int(self.player._07_how_many_people_adults)
        value_children = int(self.player._07_how_many_people_children)
        household_size = math.sqrt(value_adults + value_children)
        value_a = int(values[self.session.vars['lang']]['A'] * household_size)
        value_b = int(values[self.session.vars['lang']]['B'] * household_size)
        value_c = int(values[self.session.vars['lang']]['C'] * household_size)
        value_d = int(values[self.session.vars['lang']]['D'] * household_size)
        return {
            'household_size': household_size,
            'value_a': round((value_a) / round_to) * round_to,
            'value_b': round((value_b) / round_to) * round_to,
            'value_c': round((value_c) / round_to) * round_to,
            'value_d': round((value_d) / round_to) * round_to
        }


class Survey10G(Page):
    """Page 10 of survey."""

    form_model = models.Player
    form_fields = [
        '_10G_religion',
        '_10G_religion_B'
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
        '_11_which_browser'
    ]


class Survey12(Page):
    """Page 12 of survey."""

    form_model = models.Player
    form_fields = [
        '_12_final_comments',
        'total_time'
    ]

    def vars_for_template(self):
        """Make data available in template."""
        return {'start_time': self.player.total_time}


class EndGame(Page):
    """End of survey."""

    pass


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
    Survey10A,
    Survey10B,
    Survey10C,
    Survey10D,
    Survey10G,
    Survey11,
    Survey12,
]
