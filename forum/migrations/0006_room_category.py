# Generated by Django 3.2.15 on 2022-09-01 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20220901_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]