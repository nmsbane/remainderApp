# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('time', models.DateTimeField()),
                ('timezone', timezone_field.fields.TimeZoneField(default=b'Asia/Kolkata')),
            ],
        ),
    ]