# Generated by Django 4.0.8 on 2023-07-02 15:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0009_container_no_of_alter_booking_date_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='No_of',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_booked',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 2, 21, 28, 37, 182129)),
        ),
    ]