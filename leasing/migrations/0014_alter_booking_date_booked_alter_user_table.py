# Generated by Django 4.0.8 on 2023-07-03 06:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0013_user_alter_booking_date_booked_alter_booking_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_booked',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 12, 0, 23, 205686)),
        ),
        migrations.AlterModelTable(
            name='user',
            table='existing_table_name',
        ),
    ]