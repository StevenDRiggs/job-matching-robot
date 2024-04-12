# Generated by Django 5.0.4 on 2024-04-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiring_companies', '0002_trait'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField()),
                ('county', models.CharField(null=True)),
                ('state', models.CharField(null=True)),
                ('country', models.CharField()),
            ],
        ),
    ]