# Generated by Django 4.0.8 on 2023-07-10 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0022_userdetails_fullname_alter_booking_date_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='forget_password_token',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='date_booked',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 10, 12, 19, 27, 2528)),
        ),
    ]
