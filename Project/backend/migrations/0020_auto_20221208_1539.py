# Generated by Django 3.2 on 2022-12-08 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_rename_file_content_material_file_content_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(default='first', max_length=26),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(default='last', max_length=26),
        ),
        migrations.AlterField(
            model_name='material',
            name='file_content_upload',
            field=models.FileField(blank=True, null=True, upload_to='content/'),
        ),
    ]
