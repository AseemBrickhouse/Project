# Generated by Django 3.2 on 2022-10-17 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_alter_material_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='somenewField',
            field=models.TextField(null=True),
        ),
    ]
