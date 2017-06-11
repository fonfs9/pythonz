# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-11 10:49
from __future__ import unicode_literals

import apps.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0041_auto_20170423_0536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('time_published', models.DateTimeField(editable=False, null=True, verbose_name='Дата публикации')),
                ('time_modified', models.DateTimeField(editable=False, null=True, verbose_name='Дата редактирования')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Черновик'), (2, 'Опубликован'), (5, 'К отложенной публикации'), (3, 'Удален'), (4, 'В архиве')], default=1, verbose_name='Статус')),
                ('supporters_num', models.PositiveIntegerField(default=0, verbose_name='Поддержка')),
                ('data_items', models.TextField(verbose_name='Элементы сводки')),
                ('data_result', models.TextField(verbose_name='Результат компоновки сводки')),
                ('last_editor', models.ForeignKey(blank=True, help_text='Пользователь, последним отредактировавший объект.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='summary_editors', to=settings.AUTH_USER_MODEL, verbose_name='Редактор')),
                ('submitter', models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, related_name='summary_submitters', to=settings.AUTH_USER_MODEL, verbose_name='Добавил')),
            ],
            options={
                'ordering': ('-time_created',),
                'verbose_name_plural': 'Сводки',
                'verbose_name': 'Сводка',
            },
            bases=(apps.models.UtmReady, models.Model),
        ),
    ]
