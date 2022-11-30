# Generated by Django 3.2 on 2022-11-18 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_auto_20221031_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='friends_with',
        ),
        migrations.AddField(
            model_name='friends',
            name='friends',
            field=models.ManyToManyField(related_name='friends', to='backend.Account'),
        ),
        migrations.AlterField(
            model_name='friends',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_account', to='backend.account'),
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('from_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='backend.account')),
                ('to_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='backend.account')),
            ],
        ),
    ]
