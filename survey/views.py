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


class TrustAndTrustingBehaviour1(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_1', 'total_time']
    template_name = 'survey/TrustAndTrustingBehaviour1.html'


class TrustAndTrustingBehaviour2(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_2']
    template_name = 'survey/TrustAndTrustingBehaviour2.html'


class TrustAndTrustingBehaviour3(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_3']
    template_name = 'survey/TrustAndTrustingBehaviour3.html'


class TrustAndTrustingBehaviour4(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_4']
    template_name = 'survey/TrustAndTrustingBehaviour4.html'


class TrustAndTrustingBehaviour5(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_5']
    template_name = 'survey/TrustAndTrustingBehaviour5.html'


class TrustAndTrustingBehaviour6(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_6']
    template_name = 'survey/TrustAndTrustingBehaviour6.html'


class TrustAndTrustingBehaviour7(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = [
        'q_1_7_1', 'q_1_7_2', 'q_1_7_3', 'q_1_7_4', 'q_1_7_5', 'q_1_7_6'
    ]
    template_name = 'survey/TrustAndTrustingBehaviour7.html'


class TrustAndTrustingBehaviour8(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_8']
    template_name = 'survey/TrustAndTrustingBehaviour8.html'


class TrustAndTrustingBehaviour9(Page):
    """Page for Trust And Trusting Behaviour."""

    form_model = models.Player
    form_fields = ['q_1_9']
    template_name = 'survey/TrustAndTrustingBehaviour9.html'


class TrustInInstitution1(Page):
    """Page for Trust In Institution."""

    form_model = models.Player
    form_fields = ['q_2_1_1', 'q_2_1_2', 'q_2_1_3']
    template_name = 'survey/TrustInInstitution1.html'


class TrustInInstitution2(Page):
    """Page for Trust In Institution."""

    form_model = models.Player
    form_fields = ['q_2_2_1', 'q_2_2_2', 'q_2_2_3']
    template_name = 'survey/TrustInInstitution2.html'


class Demographics1(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_birthdate']
    template_name = 'survey/Demographics1.html'


class Demographics2(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_gender']
    template_name = 'survey/Demographics2.html'


class Demographics3(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_household']
    template_name = 'survey/Demographics3.html'


class Demographics4(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_country']
    template_name = 'survey/Demographics4.html'


class Demographics5(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_country_year']
    template_name = 'survey/Demographics5.html'


class Demographics6(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_country_citizenship']
    template_name = 'survey/Demographics6.html'


class Demographics7(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_education']
    template_name = 'survey/Demographics7.html'


class Demographics8(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_situation']
    template_name = 'survey/Demographics8.html'


class Demographics9(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_work_sector']
    template_name = 'survey/Demographics9.html'


class Demographics10(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_trust']
    template_name = 'survey/Demographics10.html'


class Demographics11(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_income_sources']
    template_name = 'survey/Demographics11.html'


class Demographics12(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_income_total']
    template_name = 'survey/Demographics12.html'


class Demographics13(Page):
    """Page for Demographics."""

    form_model = models.Player
    form_fields = ['q_religion', 'q_jewish']
    template_name = 'survey/Demographics13.html'


class WrapUp1(Page):
    """Survey wrap-up page."""

    form_model = models.Player
    form_fields = ['q_4_1']
    template_name = 'survey/WrapUp1.html'


class WrapUp2(Page):
    """Survey wrap-up page."""

    form_model = models.Player
    form_fields = ['q_4_2']
    template_name = 'survey/WrapUp2.html'


class WrapUp3(Page):
    """Survey wrap-up page."""

    form_model = models.Player
    form_fields = ['q_4_3']
    template_name = 'survey/WrapUp3.html'


class WrapUp4(Page):
    """Survey wrap-up page."""

    form_model = models.Player
    form_fields = ['q_4_4']
    template_name = 'survey/WrapUp4.html'


class WrapUp5(Page):
    """Survey wrap-up page."""

    form_model = models.Player
    form_fields = ['q_4_5']
    template_name = 'survey/WrapUp5.html'


class EndGame(Page):
    """End game page."""

    form_model = models.Player
    form_fields = ['total_time']

    def vars_for_template(self):
        """Make data available in template."""
        return {'start_time': self.player.total_time}


page_sequence = [
    TrustAndTrustingBehaviour1,
    TrustAndTrustingBehaviour2,
    TrustAndTrustingBehaviour3,
    TrustAndTrustingBehaviour4,
    TrustAndTrustingBehaviour5,
    TrustAndTrustingBehaviour6,
    TrustAndTrustingBehaviour7,
    TrustAndTrustingBehaviour8,
    TrustAndTrustingBehaviour9,
    TrustInInstitution1,
    TrustInInstitution2,
    Demographics1,
    Demographics2,
    Demographics3,
    Demographics4,
    Demographics5,
    Demographics6,
    Demographics7,
    Demographics8,
    Demographics9,
    Demographics10,
    Demographics11,
    Demographics12,
    Demographics13,
    WrapUp1,
    WrapUp2,
    WrapUp3,
    WrapUp4,
    WrapUp5,
    EndGame
]
