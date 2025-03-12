# Generated by Django 5.1.7 on 2025-03-12 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0048_rename_customer_id_insurance_master_insurance_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='enquiry_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquiry_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('vehicle_no', models.CharField(max_length=50)),
                ('reference_of_enquiry', models.CharField(max_length=50)),
                ('vehicle_model', models.DateField()),
                ('manufacturing_year', models.DateField()),
                ('previous_policy_no', models.IntegerField()),
                ('insurance_name', models.CharField(max_length=50)),
                ('expiry_date', models.DateField()),
                ('vehicle_type', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='add_enquiry',
        ),
    ]
