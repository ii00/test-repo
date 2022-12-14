# Generated by Django 4.0.5 on 2022-08-14 01:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_user_book_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='diagnosis',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to=settings.AUTH_USER_MODEL),
        ),
    ]
