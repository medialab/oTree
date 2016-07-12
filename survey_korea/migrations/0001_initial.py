# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields
import otree_save_the_change.mixins
import otree.db.models


class Migration(migrations.Migration):

    # dependencies = [
    #     ('otree', '0002_auto_20160602_0734'),
    # ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('_is_missing_players', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, db_index=True)),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('round_number', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('session', otree.db.models.ForeignKey(related_name='survey_group', to='otree.Session')),
            ],
            options={
                'db_table': 'survey_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('_index_in_game_pages', otree.db.models.PositiveIntegerField(null=True, default=0)),
                ('round_number', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('id_in_group', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('payoff', otree.db.models.CurrencyField(max_digits=12, null=True)),
                ('total_time', otree.db.models.CharField(max_length=500, null=True, blank=True)),
                ('_01_how_satisfied_are_you_with_life_as_a_whole', otree.db.models.CharField(choices=[('0', '0 - Not at all satisfied'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - Completely satisfied'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='Overall, how satisfied are you with life as a whole these days?')),
                ('_01_would_you_say_that_most_people_can_be_trusted', otree.db.models.CharField(choices=[('0', "0 -You can't be too careful"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - Most people can be trusted'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name="Generally speaking, would you say that most people can be trusted, or that you can't be too careful in dealing with people?")),
                ('_01_are_you_a_person_fully_prepared_to_take_risks', otree.db.models.CharField(choices=[('0', '0 - Generally unwilling to take risks'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - Fully prepared to take risks'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='How do you see yourself: are you generally a person who is fully prepared to take risks or do you try to avoid taking risks?')),
                ('_02_people_are_only_looking_out_for_themselves', otree.db.models.CharField(choices=[('0', '0 - People are only looking out for themselves'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - People mostly try to help each other'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='Would you say that most of the time people are only looking out for themselves or that they mostly try to help each other?')),
                ('_02_people_would_try_to_take_advantage_of_you', otree.db.models.CharField(choices=[('0', '0 - Most people would try to take advantage of me'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - Most people would try to be fair'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='Do you think most people would try to take advantage of you if they got a chance, or would they try to be fair?')),
                ('_02_the_following_action_can_always_be_justified', otree.db.models.CharField(choices=[('0', '0 - This action is never justifiable'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - This action is always justifiable'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='Receiving social allowances to which you are not entitled.')),
                ('_03_your_family', otree.db.models.CharField(choices=[('0', "0 - I don't trust them at all"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - I fully trust them'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='Your family.')),
                ('_03_people_in_your_neighborhood', otree.db.models.CharField(choices=[('0', "0 - I don't trust them at all"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - I fully trust them'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='People in your neighborhood.')),
                ('_03_people_you_know_personally', otree.db.models.CharField(choices=[('0', "0 - I don't trust them at all"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - I fully trust them'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='People you know personally.')),
                ('_03_people_you_meet_for_the_first_time', otree.db.models.CharField(choices=[('0', "0 - I don't trust them at all"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - I fully trust them'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='People you meet for the first time.')),
                ('_03_people_of_another_religion', otree.db.models.CharField(choices=[('0', "0 - I don't trust them at all"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - I fully trust them'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='People of another religion.')),
                ('_03_people_of_another_nationality', otree.db.models.CharField(choices=[('0', "0 - I don't trust them at all"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - I fully trust them'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='People of another nationality.')),
                ('_04_you_lost_a_wallet_or_a_purse', otree.db.models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='If you lost a wallet or a purse that contained items of great value to you, and it was found by a stranger, do you think it would be returned with its contents, or not?')),
                ('_04_you_vote_in_the_last_national_election', otree.db.models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('I could not vote', 'I could not vote'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='Did you vote in the last national election in France?')),
                ('_05_your_government', otree.db.models.CharField(choices=[('0', "0 - I don't trust them at all"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - I fully trust them'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='Your government.')),
                ('_05_the_police', otree.db.models.CharField(choices=[('0', "0 - I don't trust them at all"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - I fully trust them'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='The judicial system.')),
                ('_05_the_media', otree.db.models.CharField(choices=[('0', "0 - I don't trust them at all"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - I fully trust them'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='The media.')),
                ('_06_public_institutions_deliver_services_in_the_best_way', otree.db.models.CharField(choices=[('0', "0 - I don't agree at all"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - I fully agree'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='Public institutions deliver public services in the best possible way.')),
                ('_06_public_institutions_pursue_long_term_objectives', otree.db.models.CharField(choices=[('0', "0 - I don't agree at all"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - I fully agree'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='Public institutions pursue long term objectives.')),
                ('_06_people_working_in_public_institutions_ethical', otree.db.models.CharField(choices=[('0', "0 - I don't agree at all"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - I fully agree'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='People working in public institutions behave according to ethical standards aimed at avoiding corruption.')),
                ('_06_public_institutions_are_transparent', otree.db.models.CharField(choices=[('0', "0 - I don't agree at all"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - I fully agree'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='Public institutions are transparent.')),
                ('_06_public_institutions_treat_all_citizens_fairly', otree.db.models.CharField(choices=[('0', "0 - I don't agree at all"), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10 - I fully agree'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='Public institutions treat all citizens fairly regardless of their gender, race, age or economic condition equally.')),
                ('_07_what_is_your_date_of_birth', otree.db.models.CharField(max_length=500, null=True, verbose_name='What is your date of birth?')),
                ('_07_what_is_your_gender', otree.db.models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=500, null=True, verbose_name='What is your gender?')),
                ('_07_all_the_people_who_live_in_the_same_household_as_you', otree.db.models.CharField(max_length=500, null=True)),
                ('_07_which_country_were_you_born', django_countries.fields.CountryField(max_length=2, verbose_name='In which country were you born?')),
                ('_07_what_year_did_you_arrive_in_France', otree.db.models.CharField(choices=[('I was born here', 'I was born here'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014'), ('2013', '2013'), ('2012', '2012'), ('2011', '2011'), ('2010', '2010'), ('2009', '2009'), ('2008', '2008'), ('2007', '2007'), ('2006', '2006'), ('2005', '2005'), ('2004', '2004'), ('2003', '2003'), ('2002', '2002'), ('2001', '2001'), ('2000', '2000'), ('1999', '1999'), ('1998', '1998'), ('1997', '1997'), ('1996', '1996'), ('1995', '1995'), ('1994', '1994'), ('1993', '1993'), ('1992', '1992'), ('1991', '1991'), ('1990', '1990'), ('1989', '1989'), ('1988', '1988'), ('1987', '1987'), ('1986', '1986'), ('1985', '1985'), ('1984', '1984'), ('1983', '1983'), ('1982', '1982'), ('1981', '1981'), ('1980', '1980'), ('1979', '1979'), ('1978', '1978'), ('1977', '1977'), ('1976', '1976'), ('1975', '1975'), ('1974', '1974'), ('1973', '1973'), ('1972', '1972'), ('1971', '1971'), ('1970', '1970'), ('1969', '1969'), ('1968', '1968'), ('1967', '1967'), ('1966', '1966'), ('1965', '1965'), ('1964', '1964'), ('1963', '1963'), ('1962', '1962'), ('1961', '1961'), ('1960', '1960'), ('1959', '1959'), ('1958', '1958'), ('1957', '1957'), ('1956', '1956'), ('1955', '1955'), ('1954', '1954'), ('1953', '1953'), ('1952', '1952'), ('1951', '1951'), ('1950', '1950'), ('1949', '1949'), ('1948', '1948'), ('1947', '1947'), ('1946', '1946'), ('1945', '1945'), ('1944', '1944'), ('1943', '1943'), ('1942', '1942'), ('1941', '1941')], max_length=500, null=True, verbose_name='In what year did you arrive in France?')),
                ('_08_highest_level_of_education_that_you_have_completed', otree.db.models.CharField(choices=[('Less than high school', 'Less than high school'), ('High school', 'High school'), ('Some college', 'Some college'), ('Diploma, trades certificate or other post school qualification other than university', 'Diploma, trades certificate or other post school qualification other than university'), ('Undergraduate degree (e.g. BA, BS)', 'Undergraduate degree (e.g. BA, BS)'), ('Post-graduate degree', 'Post-graduate degree'), ("Don't know", "Don't know"), ('I prefer not to answer', 'I prefer not to answer')], max_length=500, null=True, verbose_name='What is the highest level of education that you have completed?')),
                ('_08_which_of_these_best_describes_your_situation', otree.db.models.CharField(choices=[('At work as an employee', 'At work as an employee'), ('Employer/self-employed', 'Employer/self-employed'), ('Employed, on child-care leave or other leave', 'Employed, on child-care leave or other leave'), ('At work as relative assisting on family farm or business', 'At work as relative assisting on family farm or business'), ('Unemployed less than 12 months', 'Unemployed less than 12 months'), ('Unemployed 12 months or more', 'Unemployed 12 months or more'), ('Unable to work due to long-term illness or disability', 'Unable to work due to long-term illness or disability'), ('Retired', 'Retired'), ('Full-time homemaker', 'Full-time homemaker'), ('In education (at school, university, etc) / student', 'In education (at school, university, etc) / student'), ('Other', 'Other'), ('I prefer not to answer', 'I prefer not to answer')], max_length=500, null=True, verbose_name='Which of these best describes your situation?')),
                ('_09_do_you_work_in_the', otree.db.models.CharField(choices=[('Central, regional or local government administration', 'Central, regional or local government administration'), ('Public sector, other', 'Public sector, other'), ('Private (for profit) sector', 'Private (for profit) sector'), ('Not for profit sector', 'Not for profit sector'), ('Other', 'Other'), ("Don't know", "Don't know"), ('I prefer not to answer', 'I prefer not to answer'), ('Not applicable', 'Not applicable')], max_length=500, null=True, verbose_name='Do you work in the...?')),
                ('_09_would_you_say_that_most_people_can_be_trusted', otree.db.models.CharField(choices=[('Most people can be trusted', 'Most people can be trusted'), ('Need to be vary careful', 'Need to be vary careful'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='Generally speaking, would you say that most people can be trusted or that you need to be very careful in dealing with people?')),
                ('_09_got_income_in_the_last_12_months_ending_today', otree.db.models.CharField(max_length=500, null=True)),
                ('_10_what_was_your_total_income', otree.db.models.CharField(choices=[('Loss', 'Loss'), ('Zero income', 'Zero income'), ('1 to 6,000', '€1 to €6,000'), ('6,000 to 12,000', '€6,000 to €12,000'), ('12,001 to 24,000', '€12,001 to €24,000'), ('24,001 to 36,000', '€24,001 to €36,000'), ('36,001 to 48,000', '€36,001 to €48,000'), ('48,001 to 60,000', '€48,001 to €60,000'), ('60,001 to 90,000', '€60,001 to €90,000'), ('90,001 to 120,000', '€90,001 to €120,000'), ('120,001 or more', '€120,001 or more'), ("Don't know", "Don't know"), ('I prefer not to answer', 'I prefer not to answer')], max_length=500, null=True, verbose_name='In the last 12 months what was your personal total income, before tax or anything else was taken out, and before any social benefit was added?')),
                ('_10_are_you', otree.db.models.CharField(choices=[('Christian - Roman Catholic', 'Christian - Roman Catholic'), ('Christian - Protestant', 'Christian - Protestant'), ('Muslim', 'Muslim'), ('Jewish', 'Jewish'), ('Other', 'Other'), ('I prefer not to answer', 'I prefer not to answer')], max_length=500, null=True, verbose_name='Are you:')),
                ('_11_other_participants_are_real_persons', otree.db.models.CharField(choices=[('No trust at all', 'No trust at all'), ('Little trust', 'Little trust'), ('Quite a bit of trust', 'Quite a bit of trust'), ('A lot of trust', 'A lot of trust'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='The other participants in the first tasks are real persons who participated in the same study.')),
                ('_11_earnings_will_be_calculated_in_euro', otree.db.models.CharField(choices=[('No trust at all', 'No trust at all'), ('Little trust', 'Little trust'), ('Quite a bit of trust', 'Quite a bit of trust'), ('A lot of trust', 'A lot of trust'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='My final earnings will be calculated in € according to the rules stated in the description of the study and will be paid to me (or donated if I choose not to keep the at the end of the study).')),
                ('_11_you_read_the_descriptions_associated', otree.db.models.CharField(choices=[('With very little care', 'With very little care'), ('With little care', 'With little care'), ('With care', 'With care'), ('With a lot of care', 'With a lot of care'), ('With extreme care', 'With extreme care'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='At the end of this study, how would you say that you read the descriptions associated with each of the 3 sections?')),
                ('_11_were_you_in_a_calm_environment', otree.db.models.CharField(choices=[('Not calm at all', 'Not calm at all'), ('Not very calm', 'Not very calm'), ('Fairly calm', 'Fairly calm'), ('Very calm', 'Very calm'), ("Don't know", "Don't know")], max_length=500, null=True, verbose_name='Were you in a calm environment when you answered the questions?')),
                ('_11_have_you_ever_participated_in_another_study', otree.db.models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=500, null=True, verbose_name='Have you ever participated in another study that seemed close to this one?')),
                ('_11_which_device_did_you_take_this_study', otree.db.models.CharField(choices=[('Desktop', 'Desktop'), ('Laptop (non-touchscreen)', 'Laptop (non-touchscreen)'), ('Laptop (touchscreen)', 'Laptop (touchscreen)'), ('Tablet', 'Tablet'), ('Other', 'Other')], max_length=500, null=True, verbose_name='Which device did you take this study on?')),
                ('group', otree.db.models.ForeignKey(to='survey.Group', null=True)),
                ('participant', otree.db.models.ForeignKey(related_name='survey_player', to='otree.Participant')),
                ('session', otree.db.models.ForeignKey(related_name='survey_player', to='otree.Session')),
            ],
            options={
                'db_table': 'survey_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('round_number', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('session', otree.db.models.ForeignKey(to='otree.Session', null=True, related_name='survey_subsession')),
            ],
            options={
                'db_table': 'survey_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=otree.db.models.ForeignKey(to='survey.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=otree.db.models.ForeignKey(to='survey.Subsession'),
        ),
    ]
