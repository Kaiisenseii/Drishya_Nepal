# Generated by Django 5.0.1 on 2024-01-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_provider', '0006_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='photo',
            field=models.ImageField(upload_to='equipment/'),
        ),
    ]
