# Generated by Django 3.2.20 on 2024-03-13 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_auto_20240311_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
    ]