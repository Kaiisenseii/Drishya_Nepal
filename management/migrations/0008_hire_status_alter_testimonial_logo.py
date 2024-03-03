# Generated by Django 5.0.1 on 2024-02-02 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hire',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Hired', 'Hired'), ('Not Hired', 'Not Hired'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='logo',
            field=models.ImageField(upload_to='testimonial/'),
        ),
    ]