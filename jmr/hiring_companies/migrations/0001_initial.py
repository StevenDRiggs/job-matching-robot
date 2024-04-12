# Generated by Django 5.0.4 on 2024-04-11 20:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job_seekers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('skill_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='job_seekers.skill')),
            ],
            bases=('job_seekers.skill',),
        ),
    ]