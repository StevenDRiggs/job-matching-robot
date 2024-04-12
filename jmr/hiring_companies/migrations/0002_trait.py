# Generated by Django 5.0.4 on 2024-04-11 20:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiring_companies', '0001_initial'),
        ('job_seekers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('trait_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='job_seekers.trait')),
            ],
            bases=('job_seekers.trait',),
        ),
    ]
