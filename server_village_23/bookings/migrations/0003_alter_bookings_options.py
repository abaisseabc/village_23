# Generated by Django 4.2.11 on 2024-04-01 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_alter_bookings_check_in_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookings',
            options={'ordering': ('-check_in_date',), 'verbose_name': 'Бронь', 'verbose_name_plural': 'Брони'},
        ),
    ]