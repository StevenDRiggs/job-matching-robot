# Generated by Django 5.0.7 on 2024-08-05 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiring_companies', '0004_rename_relocation_assistance_amount_jobrequirements__relocation_assistance_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobrequirements',
            name='position_availability_end_date',
        ),
        migrations.RemoveField(
            model_name='jobrequirements',
            name='position_availability_start_date',
        ),
        migrations.AddField(
            model_name='jobrequirements',
            name='post_date',
            field=models.DateField(default=datetime.datetime(2024, 8, 5, 22, 54, 48, 782484, tzinfo=datetime.timezone.utc)),
        ),
    ]