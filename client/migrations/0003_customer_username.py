# Generated by Django 5.0.1 on 2024-01-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_customer_photographer_feedback_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
