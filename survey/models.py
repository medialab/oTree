# -*- coding: utf-8 -*-
"""Models for Survey."""
# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
from otree import widgets
from django.forms import extras
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

    # Trust and trusting behaviour
    q_1_1 = models.CharField(
        verbose_name=_(u"Overall, how satisfied are you with life as a whole \
these days? Please respond in a scale from 0 to 10. 0 means you feel not \
at all satisfied and 10 means you feel completely satisfied."),
        choices=(
            ('0', _(u'0 - not at all satisfied')),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - completely satisfied')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_1_2 = models.CharField(
        verbose_name=_(u"Generally speaking, would you say that most people \
can be trusted, or that you can't be too careful in dealing with people? \
Please tell me on a scale of 0 to 10, where 0 means that you can't be too \
careful and 10 means that most people can be trusted."),
        choices=(
            ('0', _(u"0 - you can't be too careful")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - most people can be trusted')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_1_3 = models.CharField(
        verbose_name=_(u"How do you see yourself: are you generally a person \
who is fully prepared to take risks or do you try to avoid taking risks? \
Please choose one number on this scale, where 0 means that you are \
generally \"unwilling to take risks\" and 10 means that you are generally \
\"fully prepared to take risks\"."),
        choices=(
            ('0', _(u"0 - unwilling to take risks")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - fully prepared to take risks')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_1_4 = models.CharField(
        verbose_name=_(u"Would you say that most of the time people are only \
looking out for themselves or that they mostly try to help each other? \
Please choose one number on this scale, where 0 means that \"people are only \
looking out for themselves\" and 10 means that \"people mostly try to help \
each other\"."),
        choices=(
            ('0', _(u"0 - people are only looking out for themselves")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - people mostly try to help each other')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_1_5 = models.CharField(
        verbose_name=_(u"Do you think most people would try to take advantage \
of you if they got a chance, or would they try to be fair? \
Please choose one number on this scale, where 0 means that \"most people \
would try to take advantage of me\", and 10 means that \"most people would \
try to be fair\"."),
        choices=(
            ('0', _(u"0 - most people would try to take advantage of me")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - most people would try to be fair')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_1_6 = models.CharField(
        verbose_name=_(u"Can you tell us whether you think the following action \
can always be justified, never be justified, or something in between: \
Receiving social allowances to which you are not entitled. \
Please choose one number on this scale where 0 means that \"this action is \
never justifiable\" and 10 means that \"this action is always justifiable\"."),
        choices=(
            ('0', _(u"0 - this action is never justifiable")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - this action is always justifiable')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_1_7_1 = models.CharField(
        verbose_name=_(u"Your family"),
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

    q_1_7_2 = models.CharField(
        verbose_name=_(u"People in your neighborhood"),
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

    q_1_7_3 = models.CharField(
        verbose_name=_(u"People you know personally"),
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

    q_1_7_4 = models.CharField(
        verbose_name=_(u"People you meet for the first time"),
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

    q_1_7_5 = models.CharField(
        verbose_name=_(u"People of another religion"),
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

    q_1_7_6 = models.CharField(
        verbose_name=_(u"People of another nationality"),
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

    q_1_8 = models.CharField(
        verbose_name=_(u"If you lost a wallet or a purse that contained items of \
great value to you, and it was found by a stranger, do you think it would be \
returned with its contents, or not?"),
        choices=(
            ('Yes', _(u'Yes')),
            ('No', _(u'No')),
            ("Don't know", _(u"Don't know"))
        )
    )

    q_1_9 = models.CharField(
        verbose_name=_(u"Did you vote in the last national election?"),
        choices=(
            ('Yes', _(u'Yes')),
            ('No', _(u'No')),
            ("Don't know", _(u"Don't know"))
        )
    )

    q_2_1_1 = models.CharField(
        verbose_name=_(u"Your government"),
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

    q_2_1_2 = models.CharField(
        verbose_name=_(u"The police"),
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

    q_2_1_3 = models.CharField(
        verbose_name=_(u"The media"),
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

    q_2_2_1 = models.CharField(
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

    q_2_2_2 = models.CharField(
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

    q_2_2_3 = models.CharField(
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

    q_2_2_4 = models.CharField(
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

    q_2_2_5 = models.CharField(
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

    q_birthdate = models.CharField(
        verbose_name=_(u'What was your date of birth?'),
        widget=extras.SelectDateWidget(years=range(2016, 1900, -1))
    )

    q_gender = models.CharField(
        initial=None,
        choices=[_(u'Male'), _(u'Female')],
        verbose_name=_(u'What is your gender?'),
        widget=widgets.RadioSelect()
    )

    q_household = models.CharField(
        initial=None,
        choices=[
            _(u'My legal husband or wife'),
            _(u'My civil union partner'),
            _(u'My de-facto partner, boyfriend or girlfriend'),
            _(u'My mother and/or father'),
            _(u'My children'),
            _(u'My brothers and/or sisters'),
            _(u'My flatmates'),
            _(u'Other')
        ],
        verbose_name=_(u'Mark as many spaces as you need to show all \
the people who live in the same household as you'),
        widget=widgets.RadioSelect()
    )

    q_country = CountryField(
        verbose_name=_(u'In which country were you born?')
    )

    q_country_year = models.PositiveIntegerField(
        verbose_name=_(u'In what year did you arrive in this country'),
        choices=range(date.today().year, 1900, -1),
        initial=None
    )

    q_country_citizenship = models.CharField(
        verbose_name=_(u'Are you a citizen of this country?'),
        choices=(
            ('Yes', _(u'Yes, I am a citizen of this country.')),
            ('No', _(u'I am not a citizen of this country.'))
        ),
        widget=widgets.RadioSelect()
    )

    q_education = models.CharField(
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
        ),
        widget=widgets.RadioSelect()
    )

    q_situation = models.CharField(
        verbose_name=_(u'Which of these best describes your situation?'),
        choices=(
            ('At work as an employee or employer/self-employed', _(u'At work \
as an employee or employer/self-employed')),
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
            ('Full-time homemaker/responsible for ordinary shopping and \
looking after the home', _(u'Full-time homemaker/responsible for ordinary \
shopping and looking after the home')),
            ('In education (at school, university, etc) / student', _(u'In \
education (at school, university, etc) / student')),
            ('Other', _(u'Other')),
        )
    )

    q_work_sector = models.CharField(
        verbose_name=_(u'Do you work in the...?'),
        choices=(
            ('Central, regional or local government administration', _(u'Central, \
regional or local government administration')),
            ('Other public sector', _(u'Other public sector')),
            ('Private (for profit) sector', _(u'Private (for profit) sector')),
            ('Not for profit sector', _(u'Not for profit sector')),
            ('Other', _(u'Other')),
            ("Don't know", _(u"Don't know"))
        ),
        widget=widgets.RadioSelect()
    )

    q_trust = models.CharField(
        verbose_name=_(u'Generally speaking, would you say that most people \
can be trusted or that you need to be very careful in dealing with people?'),
        choices=(
            ('Most people can be trusted', _(u'Most people can be trusted')),
            ('Need to be vary careful', _(u'Need to be vary careful')),
            ("Don't know", _(u"Don't know"))
        ),
        widget=widgets.RadioSelect()
    )

    q_income_sources = models.CharField(
        verbose_name=_(u'What are all the ways that you got income in the \
last 12 months ending today? You can choose as many as you need. Please do \
not count loans as income.'),
        choices=(
            ('Wages, salary, commissions, bonuses etc paid by employer',
                _(u'Wages, salary, commissions, \
bonuses etc paid by employer')),
            ('Self-employment or business', _(u'Self-employment or business')),
            ('Interest, dividends, rent, other investments',
                _(u'Interest, dividends, rent, other investments')),
            ('Regular payments from a workplace accident insurer',
                _(u'Regular payments from a workplace accident insurer')),
            ('Pension', _(u'Pension')),
            ('Social insurance payments, state benefits',
                _(u'Social insurance payments, state benefits')),
            ('Other sources of income', _(u'Other sources of income')),
            ('No source of income during that time',
                _(u'No source of income during that time')),
            ("Don't know", _(u"Don't know"))
        ),
        widget=widgets.RadioSelect()
    )

    q_income_total = models.CharField(
        verbose_name=_(u'In the last 12 months what was your total income, \
before tax or anything else was taken out?'),
        choices=(
            ('Loss', _(u'Loss')),
            ('Zero income', _(u'Zero income')),
            ('$1 to $6,000', _(u'$1 to $6,000')),
            ('$6,000 to $12,000', _(u'$6,000 to $12,000')),
            ('$12,001 to $24,000', _(u'$12,001 to $24,000')),
            ('$24,001 to $36,000', _(u'$24,001 to $36,000')),
            ('$36,001 to $48,000', _(u'$36,001 to $48,000')),
            ('$48,001 to $60,000', _(u'$48,001 to $60,000')),
            ('$60,001 to $90,000', _(u'$60,001 to $90,000')),
            ('$90,001 to $120,000', _(u'$90,001 to $120,000')),
            ('$120,000 or more', _(u'$120,000 or more')),
            ("Don't know", _(u"Don't know"))
        ),
        widget=widgets.RadioSelect()
    )

    q_religion = models.CharField(
        verbose_name='Are you:',
        choices=(
            ('Jewish', _(u'Jewish')),
            ('Moslem', _(u'Moslem')),
            ('Christian', _(u'Christian')),
            ('Druze', _(u'Druze')),
            ('Other', _(u'Other'))
        ),
        widget=widgets.RadioSelect()
    )

    q_jewish = models.CharField(
        verbose_name=_(u'Do you consider yourself as being:'),
        choices=(
            ('N/A', _(u'N/A')),
            ('Ultra-religious (“Haredi”)', _(u'Ultra-religious (“Haredi”)')),
            ('Religious', _(u'Religious')),
            ('Traditional but religious', _(u'Traditional but religious')),
            ('Traditional but not so religious',
                _(u'Traditional but not so religious')),
            ('Non-religious, secular', _(u'Non-religious, secular'))
        ),
        widget=widgets.RadioSelect()
    )

    q_4_1 = models.CharField(
        verbose_name=_(u'For information purposes, could you tell us to what \
extent you trusted the following two statements when you made your decisions: \
The other participants in my group or pair are real persons who participated \
in the same study'),
        choices=(
            ('No trust at all', _(u'No trust at all')),
            ('Little trust', _(u'Little trust')),
            ('Quite a bit of trust', _(u'Quite a bit of trust')),
            ('A lot of trust', _(u'A lot of trust')),
            ("Don't know", _(u"Don't know"))
        ),
        widget=widgets.RadioSelect()
    )

    q_4_2 = models.CharField(
        verbose_name=_(u'My final earnings will be calculated in dollars \
according to the rules stated in the description of the study \
and will be paid to me (or donated if I choose not to keep the \
at the end of the study)'),
        choices=(
            ('No trust at all', _(u'No trust at all')),
            ('Little trust', _(u'Little trust')),
            ('Quite a bit of trust', _(u'Quite a bit of trust')),
            ('A lot of trust', _(u'A lot of trust')),
            ("Don't know", _(u"Don't know"))
        ),
        widget=widgets.RadioSelect()
    )

    q_4_3 = models.CharField(
        verbose_name=_(u'At the end of this study, how would you say that you \
read the descriptions associated with each of the 4 sections?'),
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

    q_4_4 = models.CharField(
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

    q_4_5 = models.CharField(
        verbose_name=_(u'Were you in a calm environment when you answered \
the questions?'),
        choices=(
            ('Yes', _(u'Yes')),
            ('No', _(u'No')),
        ),
        widget=widgets.RadioSelect()
    )
