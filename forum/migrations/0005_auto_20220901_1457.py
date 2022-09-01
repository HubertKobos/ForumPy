# Generated by Django 3.2.15 on 2022-09-01 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_room_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='number_of_answers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]