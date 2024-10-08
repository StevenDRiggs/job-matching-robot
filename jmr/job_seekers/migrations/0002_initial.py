# Generated by Django 5.0.4 on 2024-05-01 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hiring_companies', '0001_initial'),
        ('job_seekers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferences',
            name='non_preferred_locations',
            field=models.ManyToManyField(blank=True, related_name='location_non_preferred_by', to='hiring_companies.joblocation'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='preferred_career_fields',
            field=models.ManyToManyField(blank=True, related_name='career_preferred_by', to='job_seekers.careerfield'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='preferred_career_subfields',
            field=models.ManyToManyField(blank=True, related_name='career_preferred_by', to='job_seekers.careersubfield'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='preferred_industries',
            field=models.ManyToManyField(blank=True, related_name='company_preferred_by', to='job_seekers.industry'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='preferred_locations',
            field=models.ManyToManyField(blank=True, related_name='location_preferred_by', to='hiring_companies.joblocation'),
        ),
        migrations.AddField(
            model_name='skilllevel',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_seekers.skill'),
        ),
        migrations.AddField(
            model_name='traitlevel',
            name='trait',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_seekers.trait'),
        ),
        migrations.AddField(
            model_name='user',
            name='preferences',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='job_seekers.preferences'),
        ),
        migrations.AddField(
            model_name='user',
            name='skills',
            field=models.ManyToManyField(through='job_seekers.SkillLevel', to='job_seekers.skill'),
        ),
        migrations.AddField(
            model_name='user',
            name='traits',
            field=models.ManyToManyField(through='job_seekers.TraitLevel', to='job_seekers.trait'),
        ),
        migrations.AddField(
            model_name='traitlevel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_seekers.user'),
        ),
        migrations.AddField(
            model_name='skilllevel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_seekers.user'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='job_seekers.user'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='work_tasks',
            field=models.ManyToManyField(blank=True, to='job_seekers.worktask'),
        ),
    ]
