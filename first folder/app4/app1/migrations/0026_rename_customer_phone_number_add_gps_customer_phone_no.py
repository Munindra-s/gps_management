# Generated by Django 5.1.7 on 2025-03-10 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_alter_add_gps_customer_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_gps',
            old_name='customer_phone_number',
            new_name='customer_phone_no',
        ),
    ]
