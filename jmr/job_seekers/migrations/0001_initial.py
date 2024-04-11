# Generated by Django 5.0.3 on 2024-04-11 16:11

import datetime
import django.db.models.deletion
import job_seekers.models.preferences
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField()),
                ('city', models.CharField()),
                ('county', models.CharField(null=True)),
                ('state', models.CharField(null=True)),
                ('country', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='CareerField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('hard', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CareerSubfield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('career_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_seekers.careerfield')),
            ],
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remote', models.BooleanField(default=False)),
                ('relocate', models.BooleanField(default=False)),
                ('relocation_distance', models.SmallIntegerField(null=True)),
                ('distance_measurement', models.CharField(choices=[('mi', 'mi'), ('km', 'km')], max_length=2, null=True)),
                ('relocation_assistance_needed', models.BooleanField(default=False)),
                ('relocation_assistance_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('preferred_locations', models.JSONField(null=True)),
                ('non_preferred_locations', models.JSONField(null=True)),
                ('preferred_pay_low', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('preferred_pay_high', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('days_and_hours_available', models.JSONField(default=job_seekers.models.preferences.Preferences.default_days_and_hours_available)),
                ('start_date_available', models.DateField(default=datetime.date.today)),
                ('start_search_date', models.DateField(default=datetime.date.today)),
                ('end_search_date', models.DateField(null=True)),
                ('non_preferred_career_fields', models.ManyToManyField(related_name='career_non_preferred_by', to='job_seekers.careerfield')),
                ('non_preferred_career_subfields', models.ManyToManyField(related_name='career_non_preferred_by', to='job_seekers.careersubfield')),
                ('non_preferred_company_fields', models.ManyToManyField(related_name='company_non_preferred_by', to='job_seekers.companyfield')),
                ('preferred_career_fields', models.ManyToManyField(related_name='career_preferred_by', to='job_seekers.careerfield')),
                ('preferred_career_subfields', models.ManyToManyField(related_name='career_preferred_by', to='job_seekers.careersubfield')),
                ('preferred_company_fields', models.ManyToManyField(related_name='company_preferred_by', to='job_seekers.companyfield')),
                ('preferred_work_tasks', models.ManyToManyField(to='job_seekers.worktask')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name_original', models.CharField()),
                ('full_name_latinized', models.CharField(null=True)),
                ('sort_by', models.JSONField()),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='job_seekers.address')),
                ('preferences', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='job_seekers.preferences')),
                ('skills', models.ManyToManyField(to='job_seekers.skill')),
                ('traits', models.ManyToManyField(to='job_seekers.trait')),
            ],
        ),
    ]
