# Generated by Django 4.0.8 on 2023-07-02 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0003_rename_confirm_booking_confirm_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]