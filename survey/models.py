# -*- coding: utf-8 -*-
"""Models for Survey."""
# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
from otree import widgets
from django.forms import extras
from django.forms import widgets as django_widgets
from datetime import date
from django.utils.translation import ugettext_lazy as _
# </standard imports>

from django_countries.fields import CountryField


class Constants(BaseConstants):
    """Constants for Survey."""

    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    """Subsession for Survey."""

    pass


class Group(BaseGroup):
    """Group for Survey."""

    pass


class Player(BasePlayer):
    """Player for Survey."""

    total_time = models.CharField(blank=True, null=True)

    _01_how_satisfied_are_you_with_life_as_a_whole = models.CharField(
        verbose_name=_(u"Overall, how satisfied are you with life as a whole \
these days?"),
        choices=(
            ('0', _(u'0 - Not at all satisfied')),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - Completely satisfied')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _01_would_you_say_that_most_people_can_be_trusted = models.CharField(
        verbose_name=_(u"Generally speaking, would you say that most people \
can be trusted, or that you can't be too careful in dealing with people?"),
        choices=(
            ('0', _(u"0 -You can't be too careful")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - Most people can be trusted')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _01_are_you_a_person_fully_prepared_to_take_risks = models.CharField(
        verbose_name=_(u"How do you see yourself: are you generally a person \
who is fully prepared to take risks or do you try to avoid taking risks?"),
        choices=(
            ('0', _(u"0 - Generally unwilling to take risks")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - Fully prepared to take risks')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _02_people_are_only_looking_out_for_themselves = models.CharField(
        verbose_name=_(u"Would you say that most of the time people are only \
looking out for themselves or that they mostly try to help each other?"),
        choices=(
            ('0', _(u"0 - People are only looking out for themselves")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - People mostly try to help each other')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _02_people_would_try_to_take_advantage_of_you = models.CharField(
        verbose_name=_(u"Do you think most people would try to take advantage \
of you if they got a chance, or would they try to be fair?"),
        choices=(
            ('0', _(u"0 - Most people would try to take advantage of me")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - Most people would try to be fair')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _02_the_following_action_can_always_be_justified = models.CharField(
        verbose_name=_(u"Receiving social allowances to which you are not \
entitled."),
        choices=(
            ('0', _(u"0 - This action is never justifiable")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - This action is always justifiable')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _03_your_family = models.CharField(
        verbose_name=_(u"Your family."),
        choices=(
            ('0', _(u"0 - I don't trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - I fully trust them')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _03_people_in_your_neighborhood = models.CharField(
        verbose_name=_(u"People in your neighborhood."),
        choices=(
            ('0', _(u"0 - I don't trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - I fully trust them')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _03_people_you_know_personally = models.CharField(
        verbose_name=_(u"People you know personally."),
        choices=(
            ('0', _(u"0 - I don't trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - I fully trust them')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _03_people_you_meet_for_the_first_time = models.CharField(
        verbose_name=_(u"People you meet for the first time."),
        choices=(
            ('0', _(u"0 - I don't trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - I fully trust them')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _03_people_of_another_religion = models.CharField(
        verbose_name=_(u"People of another religion."),
        choices=(
            ('0', _(u"0 - I don't trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - I fully trust them')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _03_people_of_another_nationality = models.CharField(
        verbose_name=_(u"People of another nationality."),
        choices=(
            ('0', _(u"0 - I don't trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - I fully trust them')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _04_you_lost_a_wallet_or_a_purse = models.CharField(
        verbose_name=_(u"If you lost a wallet or a purse that contained items of \
great value to you, and it was found by a stranger, do you think it would be \
returned with its contents, or not?"),
        choices=(
            ('Yes', _(u'Yes')),
            ('No', _(u'No')),
            ("Don't know", _(u"Don't know"))
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _04_you_vote_in_the_last_national_election = models.CharField(
        verbose_name=_(u"Did you vote in the last national \
election?"),
        choices=(
            ('Yes', _(u'Yes')),
            ('No', _(u'No')),
            ("I could not vote", _(u"I could not vote")),
            ("Don't know", _(u"Don't know"))
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _05_your_government = models.CharField(
        verbose_name=_(u"Your government."),
        choices=(
            ('0', _(u"0 - I don't trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - I fully trust them')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _05_the_police = models.CharField(
        verbose_name=_(u"The judicial system."),
        choices=(
            ('0', _(u"0 - I don't trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - I fully trust them')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _05_the_media = models.CharField(
        verbose_name=_(u"The media."),
        choices=(
            ('0', _(u"0 - I don't trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - I fully trust them')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _06_public_institutions_deliver_services_in_the_best_way = models.CharField(
        verbose_name=_(u'Public institutions deliver public services in the \
best possible way.'),
        choices=(
            ('0', _(u"0 - I don't agree at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - I fully agree')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _06_public_institutions_pursue_long_term_objectives = models.CharField(
        verbose_name=_(u'Public institutions pursue long term objectives.'),
        choices=(
            ('0', _(u"0 - I don't agree at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - I fully agree')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _06_people_working_in_public_institutions_ethical = models.CharField(
        verbose_name=_(u'People working in public institutions behave \
according to ethical standards aimed at avoiding corruption.'),
        choices=(
            ('0', _(u"0 - I don't agree at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - I fully agree')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _06_public_institutions_are_transparent = models.CharField(
        verbose_name=_(u'Public institutions are transparent.'),
        choices=(
            ('0', _(u"0 - I don't agree at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - I fully agree')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _06_public_institutions_treat_all_citizens_fairly = models.CharField(
        verbose_name=_(u'Public institutions treat all citizens fairly \
regardless of their gender, race, age or economic condition equally.'),
        choices=(
            ('0', _(u"0 - I don't agree at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - I fully agree')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _07_what_is_your_date_of_birth = models.CharField(
        verbose_name=_(u'What is your date of birth?'),
        widget=extras.SelectDateWidget(years=range(1940, 2005, 1))
    )

    _07_what_is_your_gender = models.CharField(
        initial=None,
        choices=[_(u'Male'), _(u'Female'), _(u'Other')],
        verbose_name=_(u'What is your gender?'),
        widget=widgets.RadioSelect()
    )

    _07_all_the_people_who_live_in_the_same_household_as_you = models.CharField(
#         initial=None,
#         choices=[
#             _(u'My legal husband or wife'),
#             _(u'My civil union partner'),
#             _(u'My de-facto partner, boyfriend or girlfriend'),
#             _(u'My mother and/or father'),
#             _(u'My children'),
#             _(u'My brothers and/or sisters'),
#             _(u'My flatmates'),
#             _(u'Other')
#         ],
#         verbose_name=_(u'Mark as many spaces as you need to show all \
# the people who live in the same household as you'),
        widget=django_widgets.SelectMultiple()
    )

    _07_which_country_were_you_born = CountryField(
        verbose_name=_(u'In which country were you born?')
    )

    _07_what_year_did_you_arrive_in_France = models.CharField(
        verbose_name=_(u'In what year did you arrive in the US?'),
        choices=[_(u'I was born here')] + [
            str(x) for x in range(date.today().year, 1940, -1)
        ],
        initial=None
    )

    _08_highest_level_of_education_that_you_have_completed = models.CharField(
        verbose_name=_(u'What is the highest level of education that \
you have completed?'),
        choices=(
            ('Less than high school', _(u'Less than high school')),
            ('High school', _(u'High school')),
            ('Some college', _(u'Some college')),
            ('Diploma, trades certificate or \
other post school qualification other than university', _(u'Diploma, trades \
certificate or other post school qualification other than university')),
            ('Undergraduate degree (e.g. BA, BS)', _(u'Undergraduate \
degree (e.g. BA, BS)')),
            ('Post-graduate degree', _(u'Post-graduate degree')),
            ("Don't know", _(u"Don't know")),
            ("I prefer not to answer", _(u"I prefer not to answer")),
        ),
        widget=widgets.RadioSelect()
    )

    _08_which_of_these_best_describes_your_situation = models.CharField(
        verbose_name=_(u'Which of these best describes your situation?'),
        choices=(
            ('At work as an employee', _(u'At work as an employee')),
            ('Employer/self-employed', _(u'Employer/self-employed')),
            ('Employed, on child-care leave or other leave', _(u'Employed, on \
child-care leave or other leave')),
            ('At work as relative assisting on family farm or business', _(u'At \
work as relative assisting on family farm or business')),
            ('Unemployed less than 12 months', _(u'Unemployed less than 12 \
months')),
            ('Unemployed 12 months or more',
                _(u'Unemployed 12 months or more')),
            ('Unable to work due to long-term illness or disability', _(u'Unable \
to work due to long-term illness or disability')),
            ('Retired', _(u'Retired')),
            ('Full-time homemaker', _(u'Full-time homemaker')),
            ('In education (at school, university, etc) / student', _(u'In \
education (at school, university, etc) / student')),
            ('Other', _(u'Other')),
            ('I prefer not to answer', _(u'I prefer not to answer')),
        ),
        widget=widgets.RadioSelect()
    )

    _09_do_you_work_in_the = models.CharField(
        verbose_name=_(u'Do you work in the...?'),
        choices=(
            ('Central, regional or local government administration', _(u'Central, \
regional or local government administration')),
            ('Public sector, other', _(u'Public sector, other')),
            ('Private (for profit) sector', _(u'Private (for profit) sector')),
            ('Not for profit sector', _(u'Not for profit sector')),
            ('Other', _(u'Other')),
            ("Don't know", _(u"Don't know")),
            ("I prefer not to answer", _(u"I prefer not to answer")),
            ("Not applicable", _(u"Not applicable"))
        ),
        widget=widgets.RadioSelect()
    )

    _09_would_you_say_that_most_people_can_be_trusted = models.CharField(
        verbose_name=_(u'Generally speaking, would you say that most people \
can be trusted or that you need to be very careful in dealing with people?'),
        choices=(
            ('Most people can be trusted', _(u'Most people can be trusted')),
            ('Need to be vary careful', _(u'Need to be vary careful')),
            ("Don't know", _(u"Don't know"))
        ),
        widget=widgets.RadioSelect()
    )

    _09_got_income_in_the_last_12_months_ending_today = models.CharField(
#         verbose_name=_(u'What are all the ways that you got income in the \
# last 12 months ending today? You can choose as many as you need. Please do \
# not count loans as income.'),
        # choices=[_(u'Wages, salary, commissions, bonuses etc paid by employer'),
        #  _(u'Self-employment or business'),
        #  _(u'Interest, dividends, rent, other investments'),
        #  _(u'Regular payments from a workplace accident insurer'),
        #  _(u'Pension'),
        #  _(u'Social insurance payments, state benefits'),
        #  _(u'Other sources of income'),
        #  _(u'No source of income during that time'),
        #  _(u"Don't know")],
        widget=django_widgets.SelectMultiple()
    )

    _10_what_was_your_total_income = models.CharField(
        verbose_name=_(u'In the last 12 months what was your personal \
total income, before tax or anything else was taken out, and before any \
social benefit was added?'),
        choices=(
            ('Loss', _(u'Loss')),
            ('Zero income', _(u'Zero income')),
            ('1 to 6,000', _(u'$1 to $6,000')),
            ('6,000 to 12,000', _(u'$6,000 to $12,000')),
            ('12,001 to 24,000', _(u'$12,001 to $24,000')),
            ('24,001 to 36,000', _(u'$24,001 to $36,000')),
            ('36,001 to 48,000', _(u'$36,001 to $48,000')),
            ('48,001 to 60,000', _(u'$48,001 to $60,000')),
            ('60,001 to 90,000', _(u'$60,001 to $90,000')),
            ('90,001 to 120,000', _(u'$90,001 to $120,000')),
            ('120,001 or more', _(u'$120,001 or more')),
            ("Don't know", _(u"Don't know")),
            ("I prefer not to answer", _(u"I prefer not to answer"))
        ),
        widget=widgets.RadioSelect()
    )

    _10_are_you = models.CharField(
        verbose_name='Are you:',
        choices=(
            ('Christian - Roman Catholic', _(u'Christian - Roman Catholic')),
            ('Christian - Protestant', _(u'Christian - Protestant')),
            ('Muslim', _(u'Muslim')),
            ('Jewish', _(u'Jewish')),
            ('Other', _(u'Other')),
            ('I prefer not to answer', _(u'I prefer not to answer'))
        ),
        widget=widgets.RadioSelect()
    )

    # q_jewish = models.CharField(
    #     verbose_name=_(u'Do you consider yourself as being:'),
    #     choices=(
    #         ('N/A', _(u'N/A')),
    #         ('Ultra-religious', _(u'Ultra-religious (“Haredi”)')),
    #         ('Religious', _(u'Religious')),
    #         ('Traditional but religious', _(u'Traditional but religious')),
    #         ('Traditional but not so religious',
    #             _(u'Traditional but not so religious')),
    #         ('Non-religious, secular', _(u'Non-religious, secular'))
    #     ),
    #     widget=widgets.RadioSelect()
    # )

    _11_other_participants_are_real_persons = models.CharField(
        verbose_name=_(u'The other participants in the first tasks are real \
persons who participated in the same study.'),
        choices=(
            ('No trust at all', _(u'No trust at all')),
            ('Little trust', _(u'Little trust')),
            ('Quite a bit of trust', _(u'Quite a bit of trust')),
            ('A lot of trust', _(u'A lot of trust')),
            ("Don't know", _(u"Don't know"))
        ),
        widget=widgets.RadioSelect()
    )

    _11_earnings_will_be_calculated_in_euro = models.CharField(
        verbose_name=_(u'My final earnings will be calculated in $ \
according to the rules stated in the description of the study \
and will be paid to me (or donated if I choose not to keep the \
at the end of the study).'),
        choices=(
            ('No trust at all', _(u'No trust at all')),
            ('Little trust', _(u'Little trust')),
            ('Quite a bit of trust', _(u'Quite a bit of trust')),
            ('A lot of trust', _(u'A lot of trust')),
            ("Don't know", _(u"Don't know"))
        ),
        widget=widgets.RadioSelect()
    )

    _11_you_read_the_descriptions_associated = models.CharField(
        verbose_name=_(u'At the end of this study, how would you say that you \
read the descriptions associated with each of the 3 sections?'),
        choices=(
            ('With very little care', _(u'With very little care')),
            ('With little care', _(u'With little care')),
            ('With care', _(u'With care')),
            ('With a lot of care', _(u'With a lot of care')),
            ('With extreme care', _(u'With extreme care')),
            ("Don't know", _(u"Don't know"))
        ),
        widget=widgets.RadioSelect()
    )

    _11_were_you_in_a_calm_environment = models.CharField(
        verbose_name=_(u'Were you in a calm environment when you answered \
the questions?'),
        choices=(
            ('Not calm at all', _(u'Not calm at all')),
            ('Not very calm', _(u'Not very calm')),
            ('Fairly calm', _(u'Fairly calm')),
            ('Very calm', _(u'Very calm')),
            ("Don't know", _(u"Don't know"))
        ),
        widget=widgets.RadioSelect()
    )

    _11_have_you_ever_participated_in_another_study = models.CharField(
        verbose_name=_(u'Have you ever participated in another study that \
seemed close to this one?'),
        choices=(
            ('Yes', _(u'Yes')),
            ('No', _(u'No')),
        ),
        widget=widgets.RadioSelect()
    )

    _11_which_device_did_you_take_this_study = models.CharField(
        verbose_name=_(u'Which device did you take this study on?'),
        choices=(
            ('Desktop', _(u'Desktop')),
            ('Laptop (non-touchscreen)', _(u'Laptop (non-touchscreen)')),
            ('Laptop (touchscreen)', _(u'Laptop (touchscreen)')),
            ('Tablet', _(u'Tablet')),
            ('Other', _(u'Other')),
        ),
        widget=widgets.RadioSelect()
    )
