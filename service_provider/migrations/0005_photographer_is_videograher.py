# Generated by Django 5.0.1 on 2024-01-18 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_provider', '0004_photographer_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographer',
            name='is_videograher',
            field=models.BooleanField(default=False),
        ),
    ]