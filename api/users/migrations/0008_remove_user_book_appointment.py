# Generated by Django 4.0.5 on 2022-08-10 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_phone_number_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='book_appointment',
        ),
    ]
