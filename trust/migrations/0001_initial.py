# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import otree_save_the_change.mixins
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('otree', '0002_auto_20160602_0734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('_is_missing_players', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, db_index=True)),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('round_number', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('session', otree.db.models.ForeignKey(related_name='trust_group', to='otree.Session')),
            ],
            options={
                'db_table': 'trust_group',
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
                ('sent_amount', otree.db.models.CurrencyField(max_digits=12, null=True)),
                ('sent_back_amount_0', otree.db.models.CurrencyField(max_digits=12, null=True)),
                ('sent_back_amount_1', otree.db.models.CurrencyField(max_digits=12, null=True)),
                ('sent_back_amount_2', otree.db.models.CurrencyField(max_digits=12, null=True)),
                ('sent_back_amount_3', otree.db.models.CurrencyField(max_digits=12, null=True)),
                ('sent_back_amount_4', otree.db.models.CurrencyField(max_digits=12, null=True)),
                ('sent_back_amount_5', otree.db.models.CurrencyField(max_digits=12, null=True)),
                ('sent_back_amount_6', otree.db.models.CurrencyField(max_digits=12, null=True)),
                ('sent_back_amount_7', otree.db.models.CurrencyField(max_digits=12, null=True)),
                ('sent_back_amount_8', otree.db.models.CurrencyField(max_digits=12, null=True)),
                ('sent_back_amount_9', otree.db.models.CurrencyField(max_digits=12, null=True)),
                ('sent_back_amount_10', otree.db.models.CurrencyField(max_digits=12, null=True)),
                ('group', otree.db.models.ForeignKey(to='trust.Group', null=True)),
                ('participant', otree.db.models.ForeignKey(related_name='trust_player', to='otree.Participant')),
                ('session', otree.db.models.ForeignKey(related_name='trust_player', to='otree.Session')),
            ],
            options={
                'db_table': 'trust_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('round_number', otree.db.models.PositiveIntegerField(null=True, db_index=True)),
                ('session', otree.db.models.ForeignKey(to='otree.Session', null=True, related_name='trust_subsession')),
            ],
            options={
                'db_table': 'trust_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=otree.db.models.ForeignKey(to='trust.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=otree.db.models.ForeignKey(to='trust.Subsession'),
        ),
    ]
