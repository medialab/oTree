# -*- coding: utf-8 -*-$
"""Views for Survey."""
from __future__ import division
from ._builtin import Page
from . import models
from django.utils.translation import ugettext_lazy as _


def vars_for_all_templates(self):
    """Return variables for all templates."""
    return {
        'idk': _(u'Don\t know'),
        'yes': _(u'Yes'),
        'no': _(u'no'),
        'i_dont_trust_them_at_all': _(u'I don\'t trust them at all'),
        'i_fully_trust_them': _(u'I fully trust them'),
        'q_1_7_label': _("I‘d like to ask you how much you trust people from \
various groups. Could you tell me for each of these groups how much you \
trust them? Please tell me on a scale of 0 to 10, where 0 means that you \
don't trust them at all and 10 means that you fully trust them."),
        'q_1_7_label_1': _('Your family'),
        'q_1_7_label_2': _('People in your neighborhood'),
        'q_1_7_label_3': _('People you know personally'),
        'q_1_7_label_4': _('People you meet for the first time'),
        'q_1_7_label_5': _('People of another religion'),
        'q_1_7_label_6': _('People of another nationality'),
        'q_2_1_label': _("I‘d like to ask you how much you trust different \
public institutions. How much trust do you have in the following to act \
in the best interest of society? Please tell me on a scale of 0 to 10, \
where 0 means that you don't trust them at all and 10 means \
that you fully trust them."),
        'q_2_1_label_1': _('Your government'),
        'q_2_1_label_2': _('The police'),
        'q_2_1_label_3': _('The media'),
        'q_2_2_label': _("Do you agree with the following statements?"),
        'q_2_2_label_1': _('Public institutions deliver public services in the \
best possible way'),
        'q_2_2_label_2': _('Public institutions pursue long term objectives'),
        'q_2_2_label_3': _('People working in public institutions \
behave according to ethical standards aimed at avoiding corruption'),
        'q_2_2_label_4': _('Public institutions are transparent'),
        'q_2_2_label_5': _('Public institutions treat all citizens \
fairly regardless of their gender, race, age or economic condition equally'),
    }


class Survey01(Page):
    """Page 1 of survey."""

    form_model = models.Player
    form_fields = [
        '01_how_satisfied_are_you_with_life_as_a_whole',
        '01_would_you_say_that_most_people_can_be_trusted',
        '01_are_you_a_person_fully_prepared_to_take_risks'
    ]

    def vars_for_template(self):
        """Return labels to use in template."""
        return {
            '01_label_how_satisfied_are_you_with_life_as_a_whole': _(
                u'Overall, how satisfied are you with \
life as a whole these days?'
            ),
            '01_label_how_satisfied_are_you_with_life_as_a_whole_A': _(
                u'Not at all satisfied'
            ),
            '01_label_how_satisfied_are_you_with_life_as_a_whole_B': _(
                u'Completely satisfied'
            ),

            '01_label_would_you_say_that_most_people_can_be_trusted': _(
                u'Generally speaking, would you say that most people can \
be trusted, or that you can\'t be too careful in dealing with people?'
            ),
            '01_label_would_you_say_that_most_people_can_be_trusted_A': _(
                u'You cannot be too careful'
            ),
            '01_label_would_you_say_that_most_people_can_be_trusted_B': _(
                u'Most people can be trusted'
            ),

            '01_label_are_you_a_person_fully_prepared_to_take_risks': _(
                u'How do you see yourself: are you generally a person who is \
fully prepared to take risks or do you try to avoid taking risks?'
            ),
            '01_label_are_you_a_person_fully_prepared_to_take_risks_A': _(
                u'Generally unwilling to take risks'
            ),
            '01_label_are_you_a_person_fully_prepared_to_take_risks_B': _(
                u'Fully prepared to take risks'
            )
        }


class Survey02(Page):
    """Page 2 of survey."""

    form_model = models.Player
    form_fields = [
        '02_people_are_only_looking_out_for_themselves',
        '02_people_would_try_to_take_advantage_of_you',
        '02_the_following_action_can_always_be_justified'
    ]

    def vars_for_template(self):
        """Return labels to use in template."""
        return {
            '02_people_are_only_looking_out_for_themselves': _(
                u'Would you say that most of the time people are only looking \
out for themselves or that they mostly try to help each other?'
            ),
            '02_people_are_only_looking_out_for_themselves_A': _(
                u'People are only looking out for themselves'
            ),
            '02_people_are_only_looking_out_for_themselves_B': _(
                u'People mostly try to help each other'
            ),

            '02_people_would_try_to_take_advantage_of_you': _(
                u'Do you think most people would try to take advantage of \
you if they got a chance, or would they try to be fair?'
            ),
            '02_people_would_try_to_take_advantage_of_you_A': _(
                u'Most people would try to take advantage of me'
            ),
            '02_people_would_try_to_take_advantage_of_you_B': _(
                u'Most people would try to be fair'
            ),

            '02_the_following_action_can_always_be_justified': _(
                u'Can you tell us whether you think the following action can \
always be justified, never be justified, or something in between: \
<br/>Receiving social allowances to which you are not entitled.'
            ),
            '02_the_following_action_can_always_be_justified_A': _(
                u'Never justifiable'
            ),
            '02_the_following_action_can_always_be_justified_B': _(
                u'Always justifiable'
            )
        }


class Survey03(Page):
    """Page 3 of survey."""

    form_model = models.Player
    form_fields = [
        '03_your_family',
        '03_people_in_your_neighborhood',
        '03_people_you_know_personally',
        '03_people_you_meet_for_the_first_time',
        '03_people_of_another_religion',
        '03_people_of_another_nationality',
    ]

    def vars_for_template(self):
        """Return labels to use in template."""
        return {
            '03_label_your_family': _(
                u'Your family'
            ),

            '03_label_people_in_your_neighborhood': _(
                u'People in your neighborhood'
            ),

            '03_label_people_you_know_personally': _(
                u'People you know personally'
            ),

            '03_label_people_you_meet_for_the_first_time': _(
                u'People you meet for the first time'
            ),

            '03_label_people_of_another_religion': _(
                u'People of another religion'
            ),

            '03_label_people_of_another_nationality': _(
                u'People of another nationality'
            )
        }


class Survey04(Page):
    """Page 4 of survey."""

    form_model = models.Player
    form_fields = [
        '04_you_lost_a_wallet_or_a_purse',
        '04_you_vote_in_the_last_national_election'
    ]

    def vars_for_template(self):
        """Return labels for template."""
        return {
            '04_label_you_lost_a_wallet_or_a_purse': _(
                u'If you lost a wallet or a purse that contained items of \
great value to you, and it was found by a stranger, do you think it would \
be returned with its contents, or not?'
            ),
            '04_label_you_vote_in_the_last_national_election': _(
                u'Did you vote in the last national election?'
            )
        }


class Survey05(Page):
    """Page 5 of survey."""

    form_model = models.Player
    form_fields = [
        '05_your_government',
        '05_the_police',
        '05_the_media'
    ]

    def vars_for_template(self):
        """Return labels for template."""
        return {
            '05_label_how_much_trust_do_you_have_in_the_following': _(
                u'How much trust do you have in the following to act in the \
best interest of society?'
            ),
            '05_label_your_government': _(u'Your government'),
            '05_label_the_police': _(u'The police'),
            '05_label_the_media': _(u'The media')
        }


class Survey06(Page):
    """Page 6 of survey."""

    form_model = models.Player
    form_fields = [
        '06_public_institutions_deliver_services_in_the_best_way',
        '06_public_institutions_pursue_long_term_objectives',
        '06_people_working_in_public_institutions_ethical',
        '06_public_institutions_are_transparent',
        '06_public_institutions_treat_all_citizens_fairly'
    ]

    def vars_for_template(self):
        """Return labels for template."""
        return {
            '06_label_public_institutions_deliver_services_in_the_best_way': _(
                u'Public institutions deliver public services in the best \
possible way.'
            ),
            '06_label_public_institutions_pursue_long_term_objectives': _(
                u'Public institutions pursue long term objectives.'
            ),
            '06_label_people_working_in_public_institutions_ethical': _(
                u'People working in public institutions behave according to \
ethical standards aimed at avoiding corruption.'
            ),
            '06_label_public_institutions_are_transparent': _(
                u'Public institutions are transparent.'
            ),
            '06_label_public_institutions_treat_all_citizens_fairly': _(
                u'Public institutions treat all citizens fairly regardless of \
their gender, race, age or economic condition equally.'
            )
        }


class Survey07(Page):
    """Page 7 of survey."""

    form_model = models.Player
    form_fields = [
        '07_what_is_your_date_of_birth',
        '07_what_is_your_gender',
        '07_all_the_people_who_live_in_the_same_household_as_you',
        '07_which_country_were_you_born',
        '07_what_year_did_you_arrive_in_France'
    ]

    def vars_for_template(self):
        """Return labels for template."""
        return {
            '07_label_what_is_your_date_of_birth': _(
                u'What is your date of birth?'
            ),
            '07_label_what_is_your_gender': _(
                u'What is your gender?'
            ),
            '07_label_my_legal_wife_or_husband': _(
                u'My legal wife or husband'
            ),
            '07_label_My_civil_union_partner': _(
                u'My civil union partner'
            ),
            '07_label_my_defacto_girlfriend_or_boyfriend': _(
                u'My de-facto girlfriend or boyfriend'
            ),
            '07_label_my_mother_and_or_father': _(
                u'My mother and/or father'
            ),
            '07_label_my_children': _(
                u'My children'
            ),
            '07_label_my_siblings': _(
                u'My siblings'
            ),
            '07_label_my_flatmates': _(
                u'My flatmates'
            ),
            '07_label_other': _(
                u'Other'
            ),
            '07_label_which_country_were_you_born': _(
                u'In which country were you born?'
            ),
            '07_label_what_year_did_you_arrive_in_France': _(
                u'In what year did you arrive in France?'
            )
        }


class Survey08(Page):
    """Page 8 of survey."""

    form_model = models.Player
    form_fields = [
        '08_highest_level_of_education_that_you_have_completed',
        '08_which_of_these_best_describes_your_situation',
    ]

    def vars_for_template(self):
        """Return labels for template."""
        return {
            '08_label_highest_level_of_education_that_you_have_completed': _(
                u'What is the highest level of education that you \
have completed?'
            ),
            '08_label_which_of_these_best_describes_your_situation': _(
                u'Which of these best describes your situation?'
            ),
            '08_label_less_than_high_school': _(
                u'Less than high school'
            ),
            '08_label_high_school': _(
                u'High school'
            ),
            '08_label_diploma_trade_certificate': _(
                u'Diploma, trade certificate or other post school \
qualification other than university'
            ),
            '08_label_undergraduate_degree': _(
                u'Undergraduate degree (eg BA,BS)'
            ),
            '08_label_postgrad_degree': _(
                u'Post-graduate degree'
            ),
            '08_label_at_work_as_an_employee': _(
                u'At work, as an employee'
            ),
            '08_label_employer_self_employed': _(
                u'Employer/self-employed'
            ),
            '08_label_employed_on_child_care_leave_or_other_leave': _(
                u'Employed, on child-care leave or other leave'
            ),
            '08_label_unemployed_less_than_12_months': _(
                u'Unemployed, less than 12 months'
            ),
            '08_label_at_work_as_relative_assisting_on_family_business': _(
                u'At work, as relative assisting on family business or farm'
            ),
            '08_label_unemployed_12_months_or_more': _(
                u'Unemployed, 12 months or more'
            ),
            '08_label_unable_to_work_due_to_long_term_illness': _(
                u'Unable to work due to long-term illness or disability'
            ),
            '08_label_retired': _(
                u'Retired'
            ),
            '08_label_full_time_homemaker': _(
                u'Full-time homemaker'
            ),
            '08_label_in_education_at_school_university_student': _(
                u'In education (at school, university) /student'
            )
        }


class Survey09(Page):
    """Page 9 of survey."""

    form_model = models.Player
    form_fields = [
        '09_do_you_work_in_the',
        '09_would_you_say_that_most_people_can_be_trusted',
        '09_got_income_in_the_last_12_months_ending_today'
    ]

    def vars_for_template(self):
        """Return labels for templates."""
        return {
            '09_label_do_you_work_in_the': _(
                u'Do you work in the...?'
            ),
            '09_label_would_you_say_that_most_people_can_be_trusted': _(
                u'Generally speaking, would you say that most people can be \
trusted or that you need to be very careful in dealing with people?'
            ),
            '09_label_got_income_in_the_last_12_months_ending_today': _(
                u'What are all the ways that you got income in the last 12 \
months ending today?'
            ),
            '09_label_do_not_count_loans_as_income': _(
                u'You can choose as many as you need. Please do not count \
loans as income.'
            ),
            '09_label_central_regional_or_local_government_administration': _(
                u'Central, regional or local government administration'
            ),
            '09_label_public_sector_other': _(
                u'Public sector, other'
            ),
            '09_label_private_for_profit_sector': _(
                u'Private (for profit) sector'
            ),
            '09_label_not_for_profit_sector': _(
                u'Not for profit sector'
            ),
            '09_label_other': _(
                u'Other'
            ),
            '09_label_most_people_can_be_trusted': _(
                u'Most people can be trusted'
            ),
            '09_label_need_to_be_very_careful': _(
                u'Need to be very careful'
            ),
            '09_label_wages_salary_commissions_bonuses_paid_by_employer': _(
                u'Wages, salary, commissions, bonuses etc paid by employer'
            ),
            '09_label_self_employment_or_business': _(
                u'Self-employment or business'
            ),
            '09_label_interest_dividends_rent_other investments': _(
                u'Interest, dividends, rent, other investments'
            ),
            '09_label_regular_payments_from_a_workplace_accident_insurer': _(
                u'Regular payments from a workplace accident insurer'
            ),
            '09_label_pension': _(
                u'Pension'
            ),
            '09_label_social_insurance_payments_state_benefits': _(
                u'Social insurance payments, state benefits'
            ),
            '09_label_other_sources_of_income': _(
                u'Other sources of income'
            ),
            '09_label_no source of income during the last 12 months': _(
                u'No source of income during the last 12 months'
            ),
        }


class Survey10(Page):
    """Page 10 of survey."""

    form_model = models.Player
    form_fields = [
        '10_what was your total income',
        '10_are_you'
    ]

    def vars_for_template(self):
        """Return labels for templates."""
        return {
            '10_label_what was your total income': _(
                u'<u>In the last 12 months</u> what was your total income, \
before tax or anything else was taken out?'
            ),
            '10_label_are_you': _(
                u'Are you'
            ),
            '10_label_loss': _(
                u'Loss'
            ),
            '10_label_zero_income': _(
                u'Zero income'
            ),
            '10_label_1_to_6000': _(
                u'€1 to €6,000'
            ),
            '10_label_6001_to_12000': _(
                u'€6001 to €12,000'
            ),
            '10_label_12001_to_24000': _(
                u'€12001 to €24.000'
            ),
            '10_label_24001_to_36000': _(
                u'€24.001 to €36,000'
            ),
            '10_label_36001_to_48000': _(
                u'€36.001 to €48,000'
            ),
            '10_label_48001_to_60000': _(
                u'€48.001 to €60,000'
            ),
            '10_label_60001_to_90000': _(
                u'€60.001 to €90,000'
            ),
            '10_label_90001_to_120000': _(
                u'€90.001 to €120,000'
            ),
            '10_label_120000_or_more': _(
                u'€120.000 or more'
            ),
            '10_label_christian_roman_catholic': _(
                u'Christian - Roman Catholic'
            ),
            '10_label_christian_protestant': _(
                u'Christian - Protestant'
            ),
            '10_label_muslim': _(
                u'Muslim'
            ),
            '10_label_jewish': _(
                u'Jewish'
            ),
            '10_label_other': _(
                u'Other'
            )
        }


class Survey11(Page):
    """Page 11 of survey."""

    form_model = models.Player
    form_fields = [
        '11_other_participants_are_real_persons',
        '11_earnings_will_be_calculated_in_euro',
        '11_you_read_the_descriptions_associated',
        '11_were_you_in_a_calm_environment',
        '11_have_you_ever_participated_in_another_study',
        '11_which_device_did_you_take_this_study'
    ]

    def vars_for_template(self):
        """Return labels for template."""
        return {
            '11_label_other_participants_are_real_persons': _(
                u'The other participants in my group or pair are real persons \
who participated in the same study.'
            ),
            '11_label_earnings_will_be_calculated_in_euro': _(
                u'My final earnings will be calculated in Euro according to \
the rules stated in the description of the study and will be paid to me (or \
donated if I choose not to keep the money) at the end of the study. '
            ),
            '11_label_you_read_the_descriptions_associated': _(
                u'How would you say that you read the descriptions associated \
with each of the 4 sections?'
            ),
            '11_label_were_you_in_a_calm_environment': _(
                u'Were you in a calm environment when you answered the \
questions?'
            ),
            '11_label_have_you_ever_participated_in_another_study': _(
                u'Have you ever participated in another study that seemed \
close to this one?'
            ),
            '11_label_which_device_did_you_take_this_study': _(
                u'Which device did you take this study on?'
            ),
            '11_label_no_trust_at_all': _(
                u'No trust at all'
            ),
            '11_label_little_trust': _(
                u'Little trust'
            ),
            '11_label_quite_a_bit_of_trust': _(
                u'Quite a bit of trust'
            ),
            '11_label_a_lot_of_trust': _(
                u'A lot of trust'
            ),
            '11_label_with_very_little_care': _(
                u'With very little care'
            ),
            '11_label_with_little_care': _(
                u'With little care'
            ),
            '11_label_with_care': _(
                u'With care'
            ),
            '11_label_with_a_lot_care': _(
                u'With a lot of care'
            ),
            '11_label_with_extreme_care': _(
                u'With extreme care'
            ),
            '11_label_not_very_calm': _(
                u'Not very calm'
            ),
            '11_label_fairly_calm': _(
                u'Fairly calm'
            ),
            '11_label_very_calm': _(
                u'Very calm'
            ),
            '11_desktop': _(
                u'Desktop'
            ),
            '11_laptop': _(
                u'Laptop'
            ),
            '11_tablet': _(
                u'Tablet'
            ),
            '11_other': _(
                u'Other'
            )
        }


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
