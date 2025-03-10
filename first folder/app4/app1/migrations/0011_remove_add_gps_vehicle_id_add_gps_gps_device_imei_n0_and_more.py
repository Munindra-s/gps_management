# Generated by Django 5.1.6 on 2025-03-07 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_add_insurance_customer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_gps',
            name='vehicle_id',
        ),
        migrations.AddField(
            model_name='add_gps',
            name='Gps_device_IMEI_n0',
            field=models.IntegerField(default=98765),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='add_gps',
            name='install_date',
            field=models.DateField(default='10-10-2002'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='add_gps',
            name='reminder_date',
            field=models.DateField(default='10-10-2009'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='add_gps',
            name='renew_date',
            field=models.DateField(default='09-08-2006'),
            preserve_default=False,
        ),
    ]
