# Generated by Django 5.0.7 on 2024-08-05 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0004_rename_relocation_assistance_amount_preferences__relocation_assistance_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preferences',
            name='end_search_date',
        ),
        migrations.RemoveField(
            model_name='preferences',
            name='start_search_date',
        ),
    ]
