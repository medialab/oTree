# -*- coding: utf-8 -*-
"""Models for Survey."""
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
from otree import widgets
from django.forms import extras
from datetime import date
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language
from django_countries.fields import countries


doc = """
An internationalized version of the survey, with varying questions depending
on either on the locale or some elements based on previous answers.
"""


class Constants(BaseConstants):

    name_in_url = 'survey_i18n'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):

    def before_session_starts(self):
        """Get language data before session starts."""
        self.session.vars['lang'] = get_language()


class Group(BaseGroup):

    pass


class Player(BasePlayer):

    overall_how_satisfied_are_you_with_life = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(
            u"The following question asks how satisfied you feel on a scale from 0 to 10. Zero means you feel \"not at all satisfied\" and 10 means \"completely satisfied\". Overall, how satisfied are you with life as a whole these days?"
        ),
        choices=(
            ('0', _(u"0 - Not at all satisfied")),
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
            ("Don't know", _(u"Don't know"))
        )
    )

    would_you_say_that_most_people_can_be_trusted = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Generally speaking, would you say that most people can be trusted, or that you can’t be too careful in dealing with people?"),
        choices=(
            ('0', _(u"0 - You can't be too careful")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Most people can be trusted")),
            ("Don't know", _(u"Don't know"))
        )
    )

    to_punish_someone_who_treats_others_unfairly = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"How willing are you to punish someone who treats others unfairly, even if there may be costs for you?"),
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
            ('10', _(u"10 - Very willing to do so")),
            ("Don't know", _(u"Don't know"))
        )
    )

    to_give_to_good_causes = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"How willing are you to give to good causes without expecting anything in return?"),
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
            ('10', _(u"10 - Very willing to do so")),
            ("Don't know", _(u"Don't know"))
        )
    )

    fully_prepared_or_avoid_to_take_risks = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"How do you see yourself: are you generally a person who is fully prepared to take risks or do you try to avoid taking risks?"),
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
            ('10', _(u"10 - Fully prepared to take risks")),
            ("Don't know", _(u"Don't know"))
        )
    )

    when_someone_does_me_a_favor = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"When someone does me a favour I am willing to return it. How well does this statement describe you as a person?"),
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
            ('10', _(u"10 - Describes me perfectly")),
            ("Don't know", _(u"Don't know"))
        )
    )

    people_are_looking_for_themselves_or_try_to_help_others = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Would you say that most of the time people are only looking out for themselves or that they mostly try to help each other?"),
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
            ('10', _(u"10 - People mostly try to help each other")),
            ("Don't know", _(u"Don't know"))
        )
    )

    people_would_take_advantage_of_you_or_be_fair = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Do you think most people would try to take advantage of you if they got a chance, or would they try to be fair?"),
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
            ('10', _(u"10 - Most people would try to be fair")),
            ("Don't know", _(u"Don't know"))
        )
    )

    receiving_government_benefits_to_which_you_are_not_entitled = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Receiving government benefits to which you are not entitled"),
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
            ('10', _(u"10 - This action is always wrong")),
            ("Don't know", _(u"Don't know"))
        )
    )

    cheating_on_taxes_if_you_have_a_chance = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Cheating on taxes if you have a chance"),
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
            ('10', _(u"10 - This action is always wrong")),
            ("Don't know", _(u"Don't know"))
        )
    )

    how_much_do_you_trust_your_family = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Your family"),
        choices=(
            ('0', _(u"0 - I don’t trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully trust them")),
            ("Don't know", _(u"Don't know"))
        )
    )

    how_much_do_you_trust_people_in_your_neighborhood = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"People in your neighborhood"),
        choices=(
            ('0', _(u"0 - I don’t trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully trust them")),
            ("Don't know", _(u"Don't know"))
        )
    )

    how_much_do_you_trust_people_you_know_personally = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"People you know personally"),
        choices=(
            ('0', _(u"0 - I don’t trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully trust them")),
            ("Don't know", _(u"Don't know"))
        )
    )

    how_much_do_you_trust_people_you_meet_for_the_first_time = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"People you meet for the first time"),
        choices=(
            ('0', _(u"0 - I don’t trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully trust them")),
            ("Don't know", _(u"Don't know"))
        )
    )

    how_much_do_you_trust_people_of_another_religion = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"People of another religion"),
        choices=(
            ('0', _(u"0 - I don’t trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully trust them")),
            ("Don't know", _(u"Don't know"))
        )
    )

    how_much_do_you_trust_people_of_another_nationality = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"People of another nationality"),
        choices=(
            ('0', _(u"0 - I don’t trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully trust them")),
            ("Don't know", _(u"Don't know"))
        )
    )

    how_much_do_you_trust_people_who_immigrated = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"People who immigrated to [country]"),
        choices=(
            ('0', _(u"0 - I don’t trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully trust them")),
            ("Don't know", _(u"Don't know"))
        )
    )

    how_much_do_you_trust_people_who_seek_refuge = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"People who come to [country] to seek refuge"),
        choices=(
            ('0', _(u"0 - I don’t trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully trust them")),
            ("Don't know", _(u"Don't know"))
        )
    )

    i_am_good_at_math = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"I am good at math"),
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
            ('10', _(u"10 - Describes me perfectly")),
            ("Don't know", _(u"Don't know"))
        )
    )

    lost_your_wallet = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"If you lost a wallet or a purse that contained items of great value to you, and it was found by a stranger, do you think it would be returned with its contents, or not?"),
        choices=(
            ('Yes', _(u"Yes")),
            ('No', _(u"No")),
            ("Don't know", _(u"Don't know"))
        )
    )

    did_you_vote = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Did you vote in the last general elections?"),
        choices=(
            ('Yes', _(u"Yes")),
            ('No', _(u"No")),
            ('Could not', _(u"I couldn't vote"))
        )
    )

    how_much_do_you_trust_most_people_in_your_country = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"And now a general question about trust. On a scale from zero to ten, where zero is not at all and ten is completely, in general how much do you trust most people?"),
        choices=(
            ('0', _(u"0 - Not at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Completely")),
            ("Don't know", _(u"Don't know"))
        )
    )

    trust_the_government = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"The government"),
        choices=(
            ('0', _(u"0 - I don’t trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully trust them")),
            ("Don't know", _(u"Don't know"))
        )
    )

    trust_the_civil_service = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"The civil service"),
        choices=(
            ('0', _(u"0 - I don’t trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully trust them")),
            ("Don't know", _(u"Don't know"))
        )
    )

    trust_the_parliament = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"The parliament"),
        choices=(
            ('0', _(u"0 - I don’t trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully trust them")),
            ("Don't know", _(u"Don't know"))
        )
    )

    trust_the_judicial_system = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"The judicial system"),
        choices=(
            ('0', _(u"0 - I don’t trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully trust them")),
            ("Don't know", _(u"Don't know"))
        )
    )

    trust_the_police = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"The police"),
        choices=(
            ('0', _(u"0 - I don’t trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully trust them")),
            ("Don't know", _(u"Don't know"))
        )
    )

    trust_the_media = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"The media"),
        choices=(
            ('0', _(u"0 - I don’t trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully trust them")),
            ("Don't know", _(u"Don't know"))
        )
    )

    trust_financial_institutions = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Financial institutions (e.g. banks)"),
        choices=(
            ('0', _(u"0 - I don’t trust them at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully trust them")),
            ("Don't know", _(u"Don't know"))
        )
    )

    public_institutions_deliver_service_in_the_best_way = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Public institutions deliver public services in the best possible way"),
        choices=(
            ('0', _(u"0 - I don’t agree at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully agree")),
            ("Don't know", _(u"Don't know"))
        )
    )

    public_institutions_pursue_long_term_objectives = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Public institutions pursue long term objectives"),
        choices=(
            ('0', _(u"0 - I don’t agree at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully agree")),
            ("Don't know", _(u"Don't know"))
        )
    )

    people_in_public_institutions_are_ethical_and_not_corrupt = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"People working in public institutions are ethical and not corrupt"),
        choices=(
            ('0', _(u"0 - I don’t agree at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully agree")),
            ("Don't know", _(u"Don't know"))
        )
    )

    public_institutions_are_transparent = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Public institutions are transparent"),
        choices=(
            ('0', _(u"0 - I don’t agree at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully agree")),
            ("Don't know", _(u"Don't know"))
        )
    )

    public_institutions_treat_all_citizens_fairly = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Public institutions treat all citizens fairly regardless of their gender, race, age or economic condition"),
        choices=(
            ('0', _(u"0 - I don’t agree at all")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - I fully agree")),
            ("Don't know", _(u"Don't know"))
        )
    )

    satisfied_with_the_education_system = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"the Education system"),
        choices=(
            ('0', _(u"0 -  Not at all satisfied")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Completely satisfied")),
            ("Don't know", _(u"Don't know"))
        )
    )

    satisfied_with_the_health_care_system = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"the Health care system"),
        choices=(
            ('0', _(u"0 -  Not at all satisfied")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Completely satisfied")),
            ("Don't know", _(u"Don't know"))
        )
    )

    satisfied_with_public_transport = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Public Transport"),
        choices=(
            ('0', _(u"0 -  Not at all satisfied")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Completely satisfied")),
            ("Don't know", _(u"Don't know"))
        )
    )

    satisfied_with_child_care_services = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Child care services"),
        choices=(
            ('0', _(u"0 -  Not at all satisfied")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Completely satisfied")),
            ("Don't know", _(u"Don't know"))
        )
    )

    satisfied_with_welfare_benefits = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Welfare benefits (unemployment benefits, disability benefits, income support)"),
        choices=(
            ('0', _(u"0 -  Not at all satisfied")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Completely satisfied")),
            ("Don't know", _(u"Don't know"))
        )
    )

    satisfied_with_public_housing = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Public housing"),
        choices=(
            ('0', _(u"0 -  Not at all satisfied")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Completely satisfied")),
            ("Don't know", _(u"Don't know"))
        )
    )

    satisfied_with_security_and_crime_prevention = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Security and crime prevention (police)"),
        choices=(
            ('0', _(u"0 -  Not at all satisfied")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Completely satisfied")),
            ("Don't know", _(u"Don't know"))
        )
    )

    satisfied_with_environmental_issues = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Environmental services (air and water quality, parks and green spaces)"),
        choices=(
            ('0', _(u"0 -  Not at all satisfied")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Completely satisfied")),
            ("Don't know", _(u"Don't know"))
        )
    )

    satisfied_with_cultural_facilities = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Cultural facilities (theaters, cinemas, libraries, museums, public social spaces)"),
        choices=(
            ('0', _(u"0 -  Not at all satisfied")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Completely satisfied")),
            ("Don't know", _(u"Don't know"))
        )
    )

    complaint_about_quality_of_public_service_likely_resolved = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"If you complain about bad quality of a public service, how likely is that the problem will be easily resolved?"),
        choices=(
            ('0', _(u"0 - Very unlikely")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Very likely")),
            ("Don't know", _(u"Don't know"))
        )
    )

    technology_speed_up_likely_to_be_adopted = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"If a technology could speed up administrative procedures, how likely is it that a government agency will quickly adopt the new technology?"),
        choices=(
            ('0', _(u"0 - Very unlikely")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Very likely")),
            ("Don't know", _(u"Don't know"))
        )
    )

    information_about_administrative_producedure_easy_to_find = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"If you need information about an administrative procedure, do you think it will be easy to find?"),
        choices=(
            ('0', _(u"0 - Very unlikely")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Very likely")),
            ("Don't know", _(u"Don't know"))
        )
    )

    decision_affecting_community_likely_to_be_consulted_upon = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"If a decision affecting your community is to be taken by the local or regional government, how likely is it that you would be consulted upon?"),
        choices=(
            ('0', _(u"0 - Very unlikely")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Very likely")),
            ("Don't know", _(u"Don't know"))
        )
    )

    start_a_business_conditions_stability = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"If you start a business today, do you think that the conditions under which you operate (taxes, regulations, etc.) will remain stable enough so that unexpected changes do not threaten your business?"),
        choices=(
            ('0', _(u"0 - Very unlikely")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Very likely")),
            ("Don't know", _(u"Don't know"))
        )
    )

    natural_disaster_shelter_and_clothing_availability = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"If a natural disaster occurs do you think that the provision by government of adequate food, shelter and clothing will be available to people who are affected?"),
        choices=(
            ('0', _(u"0 - Very unlikely")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Very likely")),
            ("Don't know", _(u"Don't know"))
        )
    )

    guilty_high_ranking_gov_employee_likely_prosecuted = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"If a high ranking government employee was guilty of misusing taxpayers’ money, do you think that he/she would be prosecuted?"),
        choices=(
            ('0', _(u"0 - Very unlikely")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Very likely")),
            ("Don't know", _(u"Don't know"))
        )
    )

    accept_or_refuse_administrative_procedures_speed_up_bribe = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"If money is offered by citizens to government employees in order to speed up administrative procedures, do you think that they will accept or refuse the bribe?"),
        choices=(
            ('0', _(u"0 -  Most likely to accept the bribe")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Most likely to refuse the bribe")),
            ("Don't know", _(u"Don't know"))
        )
    )

    high_ranking_gov_employee_accepts_well_paid_private_sector_job = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"If a high level politician would be offered a well-paid job in the private sector in exchange for political influence, do you think that he/she will accept reject the job?"),
        choices=(
            ('0', _(u"0 -  Most likely to accept the job")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Most likely to refuse the job")),
            ("Don't know", _(u"Don't know"))
        )
    )

    accept_or_refuse_public_procurement_tender_allocation_bribe = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"If a parliamentarian could influence the allocation of a public procurement tender and receive a bribe in return, do you think that he/she will accept or reject the bribe?"),
        choices=(
            ('0', _(u"0 - Most likely to accept the bribe")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Most likely to refuse the bribe")),
            ("Don't know", _(u"Don't know"))
        )
    )

    social_minority_citizen_likely_to_be_treated_equally = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"If a citizen belongs to a social minority (e.g. sexual, racial/ethnic and/or based on nationality), how likely is it that he or she will be treated equally by a government agency?"),
        choices=(
            ('0', _(u"0 - Very unlikely")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Very likely")),
            ("Don't know", _(u"Don't know"))
        )
    )

    expenditure_general_public_services_and_public_debt = models.CharField(
        initial=None,
        widget=widgets.NumberInput(),
    )

    expenditure_defense_and_public_order = models.CharField(
        initial=None,
        widget=widgets.NumberInput(),
    )

    expenditure_infrastucture_and_economic_affair = models.CharField(
        initial=None,
        widget=widgets.NumberInput(),
    )

    expenditure_health_and_environmental_protection = models.CharField(
        initial=None,
        widget=widgets.NumberInput(),
    )

    expenditure_education_and_culture = models.CharField(
        initial=None,
        widget=widgets.NumberInput(),
    )

    expenditure_social_protection_and_housing = models.CharField(
        initial=None,
        widget=widgets.NumberInput(),
    )

    resources_top_1_percent = models.CharField()

    resources_next_9_percent = models.CharField()

    resources_next_40_percent = models.CharField()

    resources_bottom_50_percent = models.CharField()

    revenue_raised = models.CharField(
        initial=0,
        widget=widgets.NumberInput(attrs={'min': '0', 'max': '100', 'step': '1'})
    )

    how_many_children_part_of_the_richest_segment = models.CharField(
        initial=None,
        widget=widgets.NumberInput(attrs={'min': '0', 'max': '100', 'step': '1'}),
        verbose_name=_(u"Consider 100 children growing up in the poorest segment of society. How many children do you believe are able to become part of the richest segment of society when they are older?")
    )

    not_much_or_plenty_of_opportunity = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Some people say there is not much opportunity to get ahead today for the average person. Others say anyone who works hard can climb up the ladder. Which one comes closer to the way you feel about this?"),
        choices=(
            ('0', _(u"0 - There is not much opportunity")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - There is plenty of opportunity")),
            ("Don't know", _(u"Don't know"))
        )
    )

    household_expectations_for_the_12_months_to_come = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"When it comes to the financial situation of your household, what are your expectations for the 12 months to come, will the next 12 months be better, worse, or the same?"),
        choices=(
            ('0', _(u"0 - Worse")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', _(u"5 - The same")),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Better")),
            ("Don't know", _(u"Don't know"))
        )
    )

    likely_to_still_have_a_job_in_6_months = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"How likely do you think it is that you will still have a job in 6 months (if you have one now)?"),
        choices=(
            ('0', _(u"0 - Very unlikely")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Very likely")),
            ('N/A', _(u"N/A"))
        )
    )

    likely_to_find_a_job_with_similar_salary_in_6_months = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"If you were to lose your job, how likely is it that you would find a job with a similar salary within 6 months?"),
        choices=(
            ('0', _(u"0 - Very unlikely")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Very likely")),
            ('N/A', _(u"N/A"))
        )
    )

    government_should_encourage_or_discourage_international_trade = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"As you may know, international trade has increased substantially in recent years. Do you think government should try to encourage international trade or to discourage international trade?"),
        choices=(
            ('0', _(u"0 - Fully discourage international trade")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - Fully encourage international trade")),
            ("Don't know", _(u"Don't know"))
        )
    )

    how_much_info_from_tv = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Television"),
        choices=(
            ('a lot', _(u"A lot")),
            ('some', _(u"Some")),
            ('little', _(u"Little")),
            ('none', _(u"None"))
        )
    )

    how_much_info_from_internet = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"the Internet"),
        choices=(
            ('a lot', _(u"A lot")),
            ('some', _(u"Some")),
            ('little', _(u"Little")),
            ('none', _(u"None"))
        )
    )

    how_much_info_from_family_friends_coworkers = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Family members, friends, co-workers"),
        choices=(
            ('a lot', _(u"A lot")),
            ('some', _(u"Some")),
            ('little', _(u"Little")),
            ('none', _(u"None"))
        )
    )

    how_much_info_from_social_networks = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Social networks (twitter, facebook, etc…)"),
        choices=(
            ('a lot', _(u"A lot")),
            ('some', _(u"Some")),
            ('little', _(u"Little")),
            ('none', _(u"None"))
        )
    )

    how_much_info_from_print_media = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Print media (newspapers, magazines)"),
        choices=(
            ('a lot', _(u"A lot")),
            ('some', _(u"Some")),
            ('little', _(u"Little")),
            ('none', _(u"None"))
        )
    )

    # TODO: Not sure about scale setup...
    most_likely_threatening_privacy_hackers = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Independent hackers"),
        choices=(
            ('0', _(u"0 - No threat")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - A large threat")),
            ("Don't know", _(u"Don't know"))
        )
    )

    most_likely_threatening_privacy_domestic_gov_agencies = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Domestic government agencies"),
        choices=(
            ('0', _(u"0 - No threat")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - A large threat")),
            ("Don't know", _(u"Don't know"))
        )
    )

    most_likely_threatening_privacy_foreign_gov_agencies = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Foreign government agencies"),
        choices=(
            ('0', _(u"0 - No threat")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - A large threat")),
            ("Don't know", _(u"Don't know"))
        )
    )

    most_likely_threatening_privacy_corporations = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"Corporations"),
        choices=(
            ('0', _(u"0 - No threat")),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u"10 - A large threat")),
            ("Don't know", _(u"Don't know"))
        )
    )

    estimation_of_foreigners_in_neighborhood = models.CharField(
        initial=0,
        widget=widgets.NumberInput(attrs={'min': 0, 'max': 100, 'step': 1}),
        verbose_name=_(
            u"How high do you estimate the percentage of people of non-[country] origin in your neighborhood to be? With non-[country] origin we mean people who were not born in [country] or of whom at least one parent was not born in [country]. Please give a percentage between 0 and 100."
        )
    )

    statement_agreement_immigrants_are_not_integrated = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        choices=(
            ('0', _(u'0 - Immigrants are not integrated in our society')),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - Immigrants are well integrated in our society')),
            ("Don't know", _(u"Don't know"))
        )
    )

    statement_agreement_culture_is_undermined_by_immigrants = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        choices=(
            ('0', _(u'0 - Our culture is undermined by immigrants')),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - Our culture is enriched by immigrants')),
            ("Don't know", _(u"Don't know"))
        )
    )

    how_often_do_you_get_together_with_friends = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"How often do you get together with friends?"),
        choices=(
            ('daily', _(u"Daily")),
            ('several days a week', _(u"Several days a week")),
            ('once a week', _(u"Once a week")),
            ('less than once a week', _(u"Less than once a week")),
            ('never', _(u"Never"))
        )
    )

    how_often_do_you_participate_in_voluntary_activities = models.CharField(
        initial=None,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name=_(u"How often do you participate in voluntary activities to help people other than your direct relatives, friends or colleagues?"),
        choices=(
            ('daily', _(u"Daily")),
            ('several days a week', _(u"Several days a week")),
            ('once a week', _(u"Once a week")),
            ('less than once a week', _(u"Less than once a week")),
            ('never', _(u"Never"))
        )
    )

    how_strongly_do_you_feel_connected_to_your_neighborhood = models.CharField(
        initial=None,
        verbose_name=_(u"How strongly do you feel connected to other people in your neighborhood?"),
        widget=widgets.RadioSelectHorizontal(),
        choices=(
            ('0', _(u'0 - Not at all')),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - Very connected')),
            ("Don't know", _(u"Don't know"))
        )
    )

    voting_can_or_cannot_make_a_difference = models.CharField(
        initial=None,
        verbose_name=_(u"Some people say that who people vote for does not make any difference to what happens. Others say that who people vote for can make a difference to what happens. Where would you place yourself?"),
        widget=widgets.RadioSelectHorizontal(),
        choices=(
            ('0', _(u'0 - Voting does not make a difference')),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - Voting can make a difference')),
            ("Don't know", _(u"Don't know"))
        )
    )

    political_left_center_right = models.CharField(
        initial=None,
        verbose_name=_(u"In political matters, people often talk of “the left” and “the right.” How would you place your views on this scale, generally speaking?"),
        widget=widgets.RadioSelectHorizontal(),
        choices=(
            ('0', _(u'0 - Left')),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', _(u'5 - Center')),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', _(u'10 - Right')),
            ("Don't know", _(u"Don't know"))
        )
    )

    date_of_birth = models.CharField(
        verbose_name=_(u'What is your date of birth?'),
        widget=extras.SelectDateWidget(years=range(1940, 2005, 1))
    )

    gender = models.CharField(
        initial=None,
        choices=[_(u'Male'), _(u'Female'), _(u'Other')],
        verbose_name=_(u'What is your gender?'),
        widget=widgets.RadioSelectHorizontal()
    )

    how_many_people_in_your_household = models.CharField(
        verbose_name=_(u'How many people live in your household (including yourself?)'),
        widget=widgets.Select(),
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10'),
            ('more than 10', _(u"More than 10"))
        )
    )

    which_country_were_you_born = models.CharField(
        verbose_name=_(u'In which country were you born?'),
        widget=widgets.Select(),
        choices=tuple(
            [(code, _(name)) for code, name in list(countries)]
        )
    )

    what_is_your_nationality = models.CharField(
        verbose_name=_(u'What is your nationality?'),
        widget=widgets.Select(),
        choices=tuple(
            [("Other", _(u"Other"))] +
            [(code, _(name)) for code, name in list(countries)]
        )
    )

    # TODO: "i was born there" missing?
    when_did_you_arrive_in_country = models.CharField(
        verbose_name=_(u'In what year did you arrive in [country]?'),
        choices=[_(u'I was born here')] + [str(x) for x in range(date.today().year, 1940, -1)],
        initial=None
    )

    were_your_parents_born_in_country = models.CharField(
        verbose_name=_(u'Were your parents born in [country]?'),
        widget=widgets.RadioSelectHorizontal(),
        choices=(
            ('both', _(u"Yes, both parents")),
            ('only 1', _(u"Only 1 parent")),
            ('neither', _(u"Neither was born here"))
        )
    )

    do_you_live_in_a = models.CharField(
        verbose_name=_(u'Do you live in a...?'),
        widget=widgets.RadioSelect(),
        choices=(
            # ('large metropolitan area', _(u"Large Metropolitan area (More than 1,5 million inhabitants)")),
            # ('medium metropolitan area', _(u"Medium-sized metropolitan area (500.000 to 1,5 million inhabitants)")),
            ('small metropolitan area', _(u"Small metropolitan area (200.000 to 500.000 inhabitants)")),
            ('town', _(u"Town (50.000 to 200.000 inhabitants)")),
            ('village', _(u"Village (Less than 50,000 inhabitants)")),
            ('rural area', _(u"Rural area")),
        )
    )

    highest_level_of_education_you_have_completed = models.CharField(
        verbose_name=_(u'What is the highest level of education you have completed?'),
        widget=widgets.RadioSelect(),
        choices=(
            ('less than high school', _(u"Less than high school")),
            ('high school', _(u"High school")),
            ('some college', _(u"Some college")),
            ('diploma, trades certificate or other post school qualification other than university', _(u"Diploma, trades certificate or other post school qualification other than university")),
            ('undergraduate degree', _(u"Undergraduate degree (e.g. BA, BS)")),
            ('post-graduate degree', _(u"Post-graduate degree")),
        )
    )

    highest_level_of_education_your_parent_has_completed = models.CharField(
        verbose_name=_(u'What is the highest level of education that <strong>one of your parents</strong> has completed? (either one, or both have completed this level of education)'),
        widget=widgets.RadioSelect(),
        choices=(
            ('less than high school', _(u"Less than high school")),
            ('high school', _(u"High school")),
            ('some college', _(u"Some college")),
            ('diploma, trades certificate or other post school qualification other than university', _(u"Diploma, trades certificate or other post school qualification other than university")),
            ('undergraduate degree', _(u"Undergraduate degree (e.g. BA, BS)")),
            ('post-graduate degree', _(u"Post-graduate degree")),
        )
    )

    what_best_describes_your_situation = models.CharField(
        verbose_name=_(u'Which of these best describes your situation?'),
        widget=widgets.RadioSelect(),
        choices=(
            ('employee', _(u"Employee")),
            ('employer/self-employed', _(u"Employer/self-employed")),
            ('unemployed', _(u"Unemployed")),
            ('outside the labour force (e.g. homemaker, student, retired, unable to work)', _(u"Outside the labour force (e.g. homemaker, student, retired, unable to work)")),
        )
    )

    do_you_currently_work_in_the = models.CharField(
        verbose_name=_(u'Do you currently work in the…?'),
        widget=widgets.RadioSelect(),
        choices=(
            ('central, regional or local government administration', _(u"Central, regional or local government administration")),
            ('public sector', _(u"Public sector")),
            ('private (for profit) sector', _(u"Private (for profit) sector")),
            ('not for profit sector', _(u"Not for profit sector")),
            ('N/A', _(u"N/A")),
        )
    )

    i_assume_that_people_have_only_the_best_intentions = models.CharField(
        verbose_name=_(u'How well does the following statement describe you as a person? As long as I am not convinced otherwise, I assume that people have only the best intentions?'),
        widget=widgets.RadioSelectHorizontal(),
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
            ('10', _(u"10 - Describes me perfectly")),
            ("Don't know", _(u"Don't know"))
        )
    )

    individual_income_in_the_last_12_months = models.CharField(
        blank=True,
        verbose_name=_(u"In the last 12 months, what was your total income, the income that you received as an individual, after taxes have been deducted? (Income can come salaries and wages, profit from self-employment, interest, rent, pension, social insurance payments and other benefits, among others)"),
        widget=widgets.NumberInput(attrs={'min': -1}),
    )

    individual_income_confirmation = models.CharField(
        verbose_name=_(u'Just to confirm, which of these income bands corresponds best to your personal income? Remember, we are asking for your individual income, after taxes have been deducted.'),
        widget=widgets.RadioSelect(),
        choices=(
            ('0 to 5500 (1st quintile)', _(u"€0 to €5,500.00")),
            ('5501 to 7500 (2nd quintile)', _(u"€5,501.00 to €7,500.00")),
            ('7501 to 9000 (3rd quintile)', _(u"€7,501.00 to €9,000.00")),
            ('9001 to 11000 (4th quintile)', _(u"€9,001.00 to €11,000.00")),
            ('11001 > (5th quintile)', _(u"> €11,001.00"))
        )
    )

    household_income_in_the_last_12_months = models.CharField(
        initial=0,
        verbose_name=_(u"In the last 12 months, what was the total income of your household after taxes have been deducted? (Income can come salaries and wages, profit from self-employment, interest, rent, pension, social insurance payments and other benefits, among others)"),
        widget=widgets.NumberInput(attrs={'min': -1})
    )

    # "Just to confirm, which of these income bands corresponds best to your household income?
    # Remember, we are asking for your household income, after taxes have been deducted."
    household_income_confirmation = models.CharField(
        widget=widgets.RadioSelect()
    )

    how_important_is_religion = models.CharField(
        verbose_name=_(u'How important would you say religion is in your own life?'),
        widget=widgets.RadioSelectHorizontal(),
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
            ('10', _(u"10 - Very important")),
            ("Don't know", _(u"Don't know"))
        )
    )

    people_like_me_dont_have_a_say = models.CharField(
        verbose_name=_(u"People like me don’t have any say about what the government does"),
        widget=widgets.RadioSelectHorizontal(),
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
            ('10', _(u"10 - I fully agree")),
            ("Don't know", _(u"Don't know"))
        )
    )

    which_device_did_you_take_this_study_on = models.CharField(
        verbose_name=_(u'Which device are you taking this study on?'),
        widget=widgets.RadioSelect(),
        choices=(
            ('desktop', _(u"Desktop")),
            ('laptop non-touchscreen', _(u"Laptop (non-touchscreen)")),
            ('laptop touchscreen', _(u"Laptop (touchscreen)")),
            ('tablet', _(u"Tablet")),
            ('other', _(u"Other"))
        )
    )

    open_comment = models.CharField(
        blank=True,
        verbose_name=_(u'If you have any comments about your experience taking this survey, with regard to the functionality of the platform, or the content of the tasks and questions, please provide us with relevant feedback'),
    )
