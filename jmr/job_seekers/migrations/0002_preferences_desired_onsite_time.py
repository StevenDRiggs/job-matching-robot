# Generated by Django 5.0.4 on 2024-04-11 20:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferences',
            name='desired_onsite_time',
            field=models.DurationField(default=datetime.timedelta(days=5)),
        ),
    ]