# Generated by Django 5.0.4 on 2024-06-24 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_seekers', '0003_preferences_maximum_commute'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preferences',
            old_name='relocation_assistance_amount',
            new_name='_relocation_assistance_amount',
        ),
        migrations.RenameField(
            model_name='preferences',
            old_name='relocation_assistance_amount_currency',
            new_name='_relocation_assistance_amount_currency',
        ),
    ]