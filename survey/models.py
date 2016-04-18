# -*- coding: utf-8 -*-
"""Models for Survey."""
# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
from otree import widgets
from django.forms import MultiWidget
from datetime import date
# </standard imports>

from django_countries.fields import CountryField


class DataSelectorWidget(MultiWidget):
    """Form widget for birth date."""

    def __init__(self, attrs=None):
        """Create choices for days, months, years."""
        years = [(year, year) for year in range(2014, 1900, -1)]
        months = [(month, month) for month in (
            '01', '02', '03', '04', '05', '06',
            '07', '08', '09', '10', '11', '12'
        )]
        days = [(day, day) for day in range(1, 31)]
        wid = (
            widgets.Select(attrs=attrs, choices=days),
            widgets.Select(attrs=attrs, choices=months),
            widgets.Select(attrs=attrs, choices=years),
        )
        super(DataSelectorWidget, self).__init__(wid, attrs)

    def decompress(self, value):
        """Return a decompressed form of the date."""
        # TODO: display depending on current locale
        if value:
            return [value.day, value.month, value.year]
        return None

    def format_output(self, rendered_widgets):
        """Return formatted output."""
        return ''.join(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        """Return value from inner datadict."""
        datelist = [
            widget.value_from_datadict(data, files, name + '_%s' % i)
            for i, widget in enumerate(self.widgets)
        ]
        try:
            d = date(
                day=int(datelist[0]),
                month=int(datelist[1]),
                year=int(datelist[2]),
            )
        except ValueError:
            return ''
        else:
            return str(d)


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
        verbose_name="Overall, how satisfied are you with life as a whole \
these days? Please respond in a scale from 0 to 10. 0 means you feel not \
at all satisfied and 10 means you feel completely satisfied.",
        choices=(
            ('0', '0 - not at all satisfied'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - completely satisfied'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_1_2 = models.CharField(
        verbose_name="Generally speaking, would you say that most people \
can be trusted, or that you can't be too careful in dealing with people? \
Please tell me on a scale of 0 to 10, where 0 means that you can't be too \
careful and 10 means that most people can be trusted.",
        choices=(
            ('0', "0 - you can't be too careful"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - most people can be trusted'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_1_3 = models.CharField(
        verbose_name="How do you see yourself: are you generally a person \
who is fully prepared to take risks or do you try to avoid taking risks? \
Please choose one number on this scale, where 0 means that you are \
generally \"unwilling to take risks\" and 10 means that you are generally \
\"fully prepared to take risks\".",
        choices=(
            ('0', "0 - unwilling to take risks"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - fully prepared to take risks'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_1_4 = models.CharField(
        verbose_name="Would you say that most of the time people are only \
looking out for themselves or that they mostly try to help each other? \
Please choose one number on this scale, where 0 means that \"people are only \
looking out for themselves\" and 10 means that \"people mostly try to help \
each other\".",
        choices=(
            ('0', "0 - people are only looking out for themselves"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - people mostly try to help each other'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_1_5 = models.CharField(
        verbose_name="Do you think most people would try to take advantage \
of you if they got a chance, or would they try to be fair? \
Please choose one number on this scale, where 0 means that \"most people \
would try to take advantage of me\", and 10 means that \"most people would \
try to be fair\".",
        choices=(
            ('0', "0 - most people would try to take advantage of me"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - most people would try to be fair'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_1_6 = models.CharField(
        verbose_name="Can you tell us whether you think the following action \
can always be justified, never be justified, or something in between: \
Receiving social allowances to which you are not entitled. \
Please choose one number on this scale where 0 means that \"this action is \
never justifiable\" and 10 means that \"this action is always justifiable\".",
        choices=(
            ('0', "0 - this action is never justifiable"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - this action is always justifiable'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_1_7_1 = models.CharField(
        verbose_name="I‘d like to ask you how much you trust people from \
various groups. Could you tell me for each of these groups how much you \
trust them? Please tell me on a scale of 0 to 10, where 0 means that you \
don't trust them at all and 10 means that you fully trust them.",
        choices=(
            ('0', "0 - I don't trust them at all"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - I fully trust them'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_1_7_2 = models.CharField(
        verbose_name="I‘d like to ask you how much you trust people from \
various groups. Could you tell me for each of these groups how much you \
trust them? Please tell me on a scale of 0 to 10, where 0 means that you \
don't trust them at all and 10 means that you fully trust them.",
        choices=(
            ('0', "0 - I don't trust them at all"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - I fully trust them'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_1_7_3 = models.CharField(
        verbose_name="I‘d like to ask you how much you trust people from \
various groups. Could you tell me for each of these groups how much you \
trust them? Please tell me on a scale of 0 to 10, where 0 means that you \
don't trust them at all and 10 means that you fully trust them.",
        choices=(
            ('0', "0 - I don't trust them at all"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - I fully trust them'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_1_7_4 = models.CharField(
        verbose_name="I‘d like to ask you how much you trust people from \
various groups. Could you tell me for each of these groups how much you \
trust them? Please tell me on a scale of 0 to 10, where 0 means that you \
don't trust them at all and 10 means that you fully trust them.",
        choices=(
            ('0', "0 - I don't trust them at all"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - I fully trust them'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_1_7_5 = models.CharField(
        verbose_name="I‘d like to ask you how much you trust people from \
various groups. Could you tell me for each of these groups how much you \
trust them? Please tell me on a scale of 0 to 10, where 0 means that you \
don't trust them at all and 10 means that you fully trust them.",
        choices=(
            ('0', "0 - I don't trust them at all"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - I fully trust them'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_1_7_6 = models.CharField(
        verbose_name="I‘d like to ask you how much you trust people from \
various groups. Could you tell me for each of these groups how much you \
trust them? Please tell me on a scale of 0 to 10, where 0 means that you \
don't trust them at all and 10 means that you fully trust them.",
        choices=(
            ('0', "0 - I don't trust them at all"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - I fully trust them'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_1_8 = models.CharField(
        verbose_name="If you lost a wallet or a purse that contained items of \
great value to you, and it was found by a stranger, do you think it would be \
returned with its contents, or not?",
        choices=(
            ('Yes', 'Yes'),
            ('No', 'No'),
            ("Don't know", "Don't know")
        )
    )

    q_1_9 = models.CharField(
        verbose_name="Did you vote in the last national election?",
        choices=(
            ('Yes', 'Yes'),
            ('No', 'No'),
            ("Don't know", "Don't know")
        )
    )

    q_2_1_1 = models.CharField(
        verbose_name="I‘d like to ask you how much you trust different \
public institutions. How much trust do you have in the following to act \
in the best interest of society? Please tell me on a scale of 0 to 10, \
where 0 means that you don't trust them at all and 10 means \
that you fully trust them.",
        choices=(
            ('0', "0 - I don't trust them at all"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - I fully trust them'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_2_1_2 = models.CharField(
        verbose_name="I‘d like to ask you how much you trust different \
public institutions. How much trust do you have in the following to act \
in the best interest of society? Please tell me on a scale of 0 to 10, \
where 0 means that you don't trust them at all and 10 means \
that you fully trust them.",
        choices=(
            ('0', "0 - I don't trust them at all"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - I fully trust them'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_2_1_3 = models.CharField(
        verbose_name="I‘d like to ask you how much you trust different \
public institutions. How much trust do you have in the following to act \
in the best interest of society? Please tell me on a scale of 0 to 10, \
where 0 means that you don't trust them at all and 10 means \
that you fully trust them.",
        choices=(
            ('0', "0 - I don't trust them at all"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - I fully trust them'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_2_2_1 = models.CharField(
        verbose_name="Do you agree with the following statements?",
        choices=(
            ('0', "0 - I don't agree at all"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - I fully agree'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_2_2_2 = models.CharField(
        verbose_name="Do you agree with the following statements?",
        choices=(
            ('0', "0 - I don't agree at all"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - I fully agree'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_2_2_3 = models.CharField(
        verbose_name="Do you agree with the following statements?",
        choices=(
            ('0', "0 - I don't agree at all"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - I fully agree'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_2_2_4 = models.CharField(
        verbose_name="Do you agree with the following statements?",
        choices=(
            ('0', "0 - I don't agree at all"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - I fully agree'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_2_2_5 = models.CharField(
        verbose_name="Do you agree with the following statements?",
        choices=(
            ('0', "0 - I don't agree at all"),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10 - I fully agree'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.Select(),
        initial=None
    )

    q_birthdate = models.CharField(
        verbose_name='What was your date of birth?',
        widget=DataSelectorWidget()
    )

    q_gender = models.CharField(
        initial=None,
        choices=['Male', 'Female'],
        verbose_name='What is your gender?',
        widget=widgets.RadioSelect()
    )

    q_household = models.CharField(
        initial=None,
        choices=[
            'My legal husband or wife',
            'My civil union partner',
            'My de-facto partner, boyfriend or girlfriend',
            'My mother and/or father',
            'My children',
            'My brothers and/or sisters',
            'My flatmates',
            'Other'
        ],
        verbose_name='Mark as many spaces as you need to show all \
the people who live in the same household as you',
        widget=widgets.RadioSelect()
    )

    q_country = CountryField(
        verbose_name='In which country were you born?'
    )

    q_country_year = models.PositiveIntegerField(
        verbose_name='In what year did you arrive in this country',
        choices=range(1900, 2016),
        initial=None
    )

    q_country_citizenship = models.CharField(
        verbose_name='Are you a citizen of this country?',
        choices=(
            ('Yes', 'Yes, I am a citizen of this country.'),
            ('No', 'I am not a citizen of this country.')
        ),
        widget=widgets.RadioSelect()
    )

    q_education = models.CharField(
        verbose_name='What is the highest level of education that \
you have completed?',
        choices=(
            ('Less than high school', 'Less than high school'),
            ('High school', 'High school'),
            ('Some college', 'Some college'),
            ('Diploma, trades certificate or \
other post school qualification other than university', 'Diploma, trades \
certificate or other post school qualification other than university'),
            ('Undergraduate degree (e.g. BA, BS', 'Undergraduate \
degree (e.g. BA, BS'),
            ('Post-graduate degree', 'Post-graduate degree'),
            ("Don't know", "Don't know"),
        ),
        widget=widgets.RadioSelect()
    )

    q_situation = models.CharField(
        verbose_name='Which of these best describes your situation?',
        choices=(
            ('At work as an employee or employer/self-employed', 'At work \
as an employee or employer/self-employed'),
            ('Employed, on child-care leave or other leave', 'Employed, on \
child-care leave or other leave'),
            ('At work as relative assisting on family farm or business', 'At \
work as relative assisting on family farm or business'),
            ('Unemployed less than 12 months', 'Unemployed less than 12 \
months'),
            ('Unemployed 12 months or more', 'Unemployed 12 months or more'),
            ('Unable to work due to long-term illness or disability', 'Unable \
to work due to long-term illness or disability'),
            ('Retired', 'Retired'),
            ('Full-time homemaker/responsible for ordinary shopping and \
looking after the home', 'Full-time homemaker/responsible for ordinary \
shopping and looking after the home'),
            ('In education (at school, university, etc) / student', 'In \
education (at school, university, etc) / student'),
            ('Other', 'Other'),
        )
    )

    q_work_sector = models.CharField(
        verbose_name='Do you work in the...?',
        choices=(
            ('Central, regional or local government administration', 'Central, \
regional or local government administration'),
            ('Other public sector', 'Other public sector'),
            ('Private (for profit) sector', 'Private (for profit) sector'),
            ('Not for profit sector', 'Not for profit sector'),
            ('Other', 'Other'),
            ("Don't know", "Don't know")
        ),
        widget=widgets.RadioSelect()
    )

    q_trust = models.CharField(
        verbose_name='Generally speaking, would you say that most people \
can be trusted or that you need to be very careful in dealing with people?',
        choices=(
            ('Most people can be trusted', 'Most people can be trusted'),
            ('Need to be vary careful', 'Need to be vary careful'),
            ("Don't know", "Don't know")
        ),
        widget=widgets.RadioSelect()
    )

    q_income_sources = models.CharField(
        verbose_name='What are all the ways that you got income in the \
last 12 months ending today? You can choose as many as you need. Please do \
not count loans as income.',
        choices=(
            ('Wages, salary, commissions, bonuses etc paid by employer',
                'Wages, salary, commissions, bonuses etc paid by employer'),
            ('Self-employment or business', 'Self-employment or business'),
            ('Interest, dividends, rent, other investments',
                'Interest, dividends, rent, other investments'),
            ('Regular payments from a workplace accident insurer',
                'Regular payments from a workplace accident insurer'),
            ('Pension', 'Pension'),
            ('Social insurance payments, state benefits',
                'Social insurance payments, state benefits'),
            ('Other sources of income', 'Other sources of income'),
            ('No source of income during that time',
                'No source of income during that time'),
            ("Don't know", "Don't know")
        ),
        widget=widgets.RadioSelect()
    )

    q_income_total = models.CharField(
        verbose_name='In the last 12 months what was your total income, \
before tax or anything else was taken out?',
        choices=(
            ('Loss', 'Loss'),
            ('Zero income', 'Zero income'),
            ('$1 to $6,000', '$1 to $6,000'),
            ('$6,000 to $12,000', '$6,000 to $12,000'),
            ('$12,001 to $24,000', '$12,001 to $24,000'),
            ('$24,001 to $36,000', '$24,001 to $36,000'),
            ('$36,001 to $48,000', '$36,001 to $48,000'),
            ('$48,001 to $60,000', '$48,001 to $60,000'),
            ('$60,001 to $90,000', '$60,001 to $90,000'),
            ('$90,001 to $120,000', '$90,001 to $120,000'),
            ('$120,000 or more', '$120,000 or more'),
            ("Don't know", "Don't know")
        ),
        widget=widgets.RadioSelect()
    )

    q_religion = models.CharField(
        verbose_name='Are you:',
        choices=(
            ('Jewish', 'Jewish'),
            ('Moslem', 'Moslem'),
            ('Christian', 'Christian'),
            ('Druze', 'Druze'),
            ('Other', 'Other')
        ),
        widget=widgets.RadioSelect()
    )

    q_4_1 = models.CharField(
        verbose_name='For information purposes, could you tell us to what \
extent you trusted the following two statements when you made your decisions: \
The other participants in my group or pair are real persons who participated \
in the same study',
        choices=(
            ('No trust at all', 'No trust at all'),
            ('Little trust', 'Little trust'),
            ('Quite a bit of trust', 'Quite a bit of trust'),
            ('A lot of trust', 'A lot of trust'),
            ("Don't know", "Don't know")
        ),
        widget=widgets.RadioSelect()
    )

    q_4_2 = models.CharField(
        verbose_name='My final earnings will be calculated in dollars \
according to the rules stated in the description of the study \
and will be paid to me (or donated if I choose not to keep the \
at the end of the study)',
        choices=(
            ('No trust at all', 'No trust at all'),
            ('Little trust', 'Little trust'),
            ('Quite a bit of trust', 'Quite a bit of trust'),
            ('A lot of trust', 'A lot of trust'),
            ("Don't know", "Don't know")
        ),
        widget=widgets.RadioSelect()
    )

    q_4_3 = models.CharField(
        verbose_name='At the end of this study, how would you say that you \
read the descriptions associated with each of the 4 sections?',
        choices=(
            ('With very little care', 'With very little care'),
            ('With little care', 'With little care'),
            ('With care', 'With care'),
            ('With a lot of care', 'With a lot of care'),
            ('With extreme care', 'With extreme care'),
            ("Don't know", "Don't know")
        ),
        widget=widgets.RadioSelect()
    )

    q_4_4 = models.CharField(
        verbose_name='Were you in a calm environment when you answered \
the questions?',
        choices=(
            ('Not calm at all', 'Not calm at all'),
            ('Not very calm', 'Not very calm'),
            ('Fairly calm', 'Fairly calm'),
            ('Very calm', 'Very calm'),
            ("Don't know", "Don't know")
        ),
        widget=widgets.RadioSelect()
    )

    q_4_5 = models.CharField(
        verbose_name='Were you in a calm environment when you answered \
the questions?',
        choices=(
            ('Yes', 'Yes'),
            ('No', 'No'),
        ),
        widget=widgets.RadioSelect()
    )
