# Generated by Django 5.0.7 on 2024-10-22 19:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='benefitavailable',
            options={'verbose_name_plural': 'benefits available'},
        ),
        migrations.AlterField(
            model_name='benefitavailable',
            name='available',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='position',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='company.company'),
        ),
    ]
