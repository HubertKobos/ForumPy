# Generated by Django 3.2.15 on 2022-09-01 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_room_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='short_about_me',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
