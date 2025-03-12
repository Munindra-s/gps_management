# Generated by Django 5.1.7 on 2025-03-12 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_remove_add_gps_vehicle_id_add_gps_customer_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='gps_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gps_id', models.CharField(max_length=50)),
                ('customer_name', models.CharField(max_length=40)),
                ('imei_no', models.IntegerField()),
                ('vehicle_registration_no', models.CharField(max_length=20)),
                ('vehicle_model', models.DateField()),
                ('vehicle_make', models.DateField()),
                ('vehicle_type', models.CharField(max_length=50)),
                ('installation_date', models.DateField()),
                ('reminder_date', models.DateField()),
                ('next_reminder_date', models.DateField()),
                ('plan', models.CharField(max_length=40)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.RenameModel(
            old_name='add_gps',
            new_name='gps_master',
        ),
        migrations.DeleteModel(
            name='add_enquiry',
        ),
        migrations.DeleteModel(
            name='Add_Insurance',
        ),
    ]
