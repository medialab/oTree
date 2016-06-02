# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
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
                ('session', otree.db.models.ForeignKey(related_name='dictator_group', to='otree.Session')),
            ],
            options={
                'db_table': 'dictator_group',
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
                ('given', otree.db.models.CurrencyField(max_digits=12, null=True, verbose_name='')),
                ('training_participant1_payoff', otree.db.models.CurrencyField(max_digits=12, null=True, verbose_name="Participant 1's payoff would be")),
                ('training_participant2_payoff', otree.db.models.CurrencyField(max_digits=12, null=True, verbose_name="Participant 2's payoff would be")),
                ('total_time', otree.db.models.CharField(max_length=500, null=True, blank=True)),
                ('group', otree.db.models.ForeignKey(to='dictator.Group', null=True)),
                ('participant', otree.db.models.ForeignKey(related_name='dictator_player', to='otree.Participant')),
                ('session', otree.db.models.ForeignKey(related_name='dictator_player', to='otree.Session')),
            ],
            options={
                'db_table': 'dictator_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('round_number', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('session', otree.db.models.ForeignKey(to='otree.Session', null=True, related_name='dictator_subsession')),
            ],
            options={
                'db_table': 'dictator_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=otree.db.models.ForeignKey(to='dictator.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=otree.db.models.ForeignKey(to='dictator.Subsession'),
        ),
    ]
