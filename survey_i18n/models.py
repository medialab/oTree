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

    name_in_url = 'survey_i18n'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    """Subsession for Survey."""

    def before_session_starts(self):
        if 'language_code' in self.session.config:
            self.session.vars['lang'] = (
                self.session.config['language_code'][3:]
            )


class Group(BaseGroup):
    """Group for Survey."""

    pass


class Player(BasePlayer):
    """Player for Survey."""

    total_time = models.CharField(blank=True, null=True)
    donation = models.CharField(blank=True, null=True)

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
            ('0', _(u"0 - Completely unwilling to take risks")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - Very willing to take risks')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _02_treats_you_unfairly = models.CharField(
        verbose_name=_(u'How willing are you to punish someone who treats you \
unfairly, even if there may be costs for you?'),
        choices=(
            ('0', _(u"0 - Completely unwilling to do so")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - Very willing to do so')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _02_treats_others_unfairly = models.CharField(
        verbose_name=_(u'How willing are you to punish someone who treats \
others unfairly, even if there may be costs for you?'),
        choices=(
            ('0', _(u"0 - Completely unwilling to do so")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - Very willing to do so')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _02_give_to_good_causes = models.CharField(
        verbose_name=_(u'How willing are you to give to good causes without \
expecting anything in return? '),
        choices=(
            ('0', _(u"0 - Completely unwilling to do so")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - Very willing to do so')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _02A_altruism = models.CurrencyField(
        initial=0,
        min=0,
        max=1000,
    )

    _03_does_me_a_favor = models.CharField(
        verbose_name=_(u"When someone does me a favour \
I am willing to return it."),
        choices=(
            ('0', _(u"0 - Does not describe me at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - Describes me perfectly')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _03_treated_injustly = models.CharField(
        verbose_name=_(u"If I am treated very unjustly, I will take revenge \
    at the first occasion, even if there is a cost to do so."),
        choices=(
            ('0', _(u"0 - Does not describe me at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - Describes me perfectly')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _04_thank_you_gift = models.CharField()

    _04A_try_to_help_each_other = models.CharField(
        verbose_name=_(u"Would you say that most of the time people are only \
    looking out for themselves or that they mostly try to help each other?"),
        choices=(
            ('0', _(u"0 - People are only looking out for themselves ")),
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

    _04A_try_to_take_advantage_of_you = models.CharField(
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

    _04A_can_be_justified = models.CharField(
        verbose_name=_(u"Can you tell us whether you think the following \
    action can always be justified, never be justified, or something in \
    between"),
        choices=(
            ('0', _(u"0 - This action is never wrong")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - This action is always wrong')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _04B_your_family = models.CharField(
        verbose_name=_(u"Your family:"),
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

    _04B_your_neighbourhood = models.CharField(
        verbose_name=_(u"People in your neighbourhood:"),
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

    _04B_personally = models.CharField(
        verbose_name=_(u"People you know personally:"),
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

    _04B_meet_for_the_first_time = models.CharField(
        verbose_name=_(u"People you meet for the first time:"),
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

    _04B_another_religion = models.CharField(
        verbose_name=_(u"People of another religion:"),
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

    _04B_another_nationality = models.CharField(
        verbose_name=_(u"People of another nationality:"),
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

    _04C_wallet = models.CharField(
        verbose_name=_(u"If you lost a wallet or a purse that contained items \
of great value to you, and it was found by a stranger, do you think it would \
be returned with its contents, or not?"),
        choices=(
            ('Yes', _(u'Yes')),
            ('No', _(u'No')),
            ("Don't know", _(u"Don't know"))
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _04C_you_vote_in_the_last_national_election = models.CharField(
        verbose_name=_(u"Did you vote in the last national \
election?"),
        choices=(
            ('Yes', _(u'Yes')),
            ('No', _(u'No')),
            ("I could not vote", _(u"I could not vote")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _04C_good_at_math = models.CharField(
        verbose_name=_(u"I am good at math."),
        choices=(
            ('0', _(u"0 - Does not describe me at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - Describes me perfectly')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _05_your_government = models.CharField(
        verbose_name=_(u"Your government:"),
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

    _05_the_parliament = models.CharField(
        verbose_name=_(u"The parliament:"),
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

    _05_the_judicial_system = models.CharField(
        verbose_name=_(u"The judicial system:"),
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
        verbose_name=_(u"The media:"),
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

    _05_financial_institutions = models.CharField(
        verbose_name=_(u"Financial Institutions (e.g. banks):"),
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
        verbose_name=_(u"The police:"),
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

    _06_public_institutions_deliver_services = models.CharField(
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

    _07_all_the_people_who_live_in_the_same_household = models.CharField(
        widget=django_widgets.SelectMultiple()
    )

    _07_how_many_people_adults = models.CharField(
        verbose_name=_(u'How many people live in your household \
(including yourself)?'),
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')
        )
    )

    _07_how_many_people_children = models.CharField(
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')
        )
    )

    _07_which_country_were_you_born = CountryField(
        verbose_name=_(u'In which country were you born?')
    )

    _07_what_year_did_you_arrive_in_country = models.CharField(
        choices=[_(u'I was born here')] + [
            str(x) for x in range(date.today().year, 1940, -1)
        ],
        initial=None
    )

    _07_do_you_live_in = models.CharField(
        verbose_name=_(u'Do you live in a:'),
        choices=(
            ('Large Metropolitan area', _(u"Large Metropolitan area \
(More than 1,5 million inhabitants)")),
            ('Medium-sized metropolitan area', _(u"Medium-sized metropolitan \
area (500.000 to 1,5 million inhabitants)")),
            ('Small metropolitan area', _(u"  Small metropolitan area \
(200.000 to 500.000 inhabitants)")),
            ('Town', _(u"Town (50.000 to 200.000 inhabitants)")),
            ('Village', _(u"Village (Less than 50.000 inhabitants)")),
            ('Rural area', _(u"Rural area")),
        ),
        widget=widgets.RadioSelect(),
        initial=None
    )

    _08_highest_level_of_education_that_you_have_completed = models.CharField(
        verbose_name=_(u'What is the highest level of education that \
you have completed?'),
        choices=(
            ('Aucun diplôme', _(u'Aucun diplôme')),
            ('Brevet des collèges', _(u'Brevet des collèges')),
            ('CAP BEP ou équivalent', _(u'CAP BEP ou équivalent')),
            ('Baccalauréat', _(u'Baccalauréat')),
            ('Diplômé du supérieur court (BTS, DUT, etc.)', _(u'Diplômé du \
supérieur court (BTS, DUT, etc.)')),
            ('Licence (Bac + 3)', _(u'Licence (Bac + 3)')),
            ("Master (Bac + 5) ou Doctorat", _(u"Master (Bac + 5) ou \
Doctorat")),
        ),
        widget=widgets.RadioSelect()
    )

    _09_which_of_these_best_describes_your_situation = models.CharField(
        verbose_name=_(u'Which of these best describes your situation?'),
        choices=(
            ('At work as an employee', _(u'At work as an employee')),
            ('Employer/self-employed', _(u'Employer/self-employed')),
            ('Unemployed', _(u'Unemployed')),
            ('Outside the labour force (e.g. homemaker, student, retired, \
unable to work)', _(u'Outside the labour force (e.g. homemaker, student, \
retired, unable to work)')),
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
            ("Not applicable", _(u"Not applicable"))
        ),
        widget=widgets.RadioSelect()
    )

    _09_people_only_have_the_best_intentions = models.CharField(
        verbose_name=_(u'As long as I am not convinced otherwise, I assume \
that people have only the best intentions.'),
        choices=(
            ('0', _(u"0 - Does not describe me at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - Describes me perfectly')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect()
    )

    _10_main_ways_income = models.CharField()
    _10_household_income = models.CharField()

    _10A_household_income = models.CharField()

    _10B_household_income = models.CharField(
        verbose_name=_(u'Just to confirm, which of these income bands \
corresponds best to your personal income? Remember, we are asking for \
your individual income, after taxes have been deducted.'),
    )

    _10C_income = models.CharField()

    _10D_income = models.CharField()

    _10G_income = models.CharField(
        verbose_name=_(u'Did you or your household save any money in the \
previous year?'),
        choices=(
            ('Yes', _(u"Yes")),
            ('No', _(u'No')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect()
    )

    _10H_income = models.CharField(
        verbose_name=_(u'How important would you say religion is in your \
own life?'),
        choices=(
            ('0', _(u"0 - Not important at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - Very important')),
            ("Don't know", _(u"Don't know")),
        ),
        widget=widgets.RadioSelect()
    )

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
        verbose_name=_(u'My final earnings will be calculated according to \
the rules stated in the description of the study and will be paid to me.'),
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
read the descriptions associated with each of the sections?'),
        choices=(
            ('With very little care', _(u'With very little care')),
            ('With little care', _(u'With little care')),
            ('With care', _(u'With care')),
            ('With a lot of care', _(u'With a lot of care')),
            ('With extreme care', _(u'With extreme care')),
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

    _11_which_browser = models.CharField(
        verbose_name=_(u'Which browser did you take this survey on?'),
        choices=(
            ('Google Chrome', _(u'Google Chrome')),
            ('Firefox', _(u'Firefox')),
            ('Internet Explorer', _(u'Internet Explorer')),
            ('Other', _(u'Other')),
        ),
        widget=widgets.RadioSelect()
    )

    _12_final_comments = models.CharField(
        verbose_name=_(u'If you have any comments about your experience \
taking this survey, with regard to the functionality of the platform, or the \
content of the tasks and questions, please provide us with relevant \
feedback:'),
    )
