# Generated by Django 3.2 on 2022-10-17 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_account_somenewfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='somenewField',
        ),
    ]
