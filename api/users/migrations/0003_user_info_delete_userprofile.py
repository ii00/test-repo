# Generated by Django 4.0.5 on 2022-07-09 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userprofile_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='info',
            field=models.CharField(default='', max_length=2500),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
