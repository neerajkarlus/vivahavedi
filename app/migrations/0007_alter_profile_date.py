# Generated by Django 3.2.4 on 2021-07-26 12:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_profile_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 7, 26, 12, 3, 59, 637851)),
        ),
    ]
