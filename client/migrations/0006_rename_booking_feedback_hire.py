# Generated by Django 5.0.1 on 2024-03-03 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_feedback_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='booking',
            new_name='hire',
        ),
    ]