# Generated by Django 5.1.6 on 2025-02-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('vehicle_no', models.CharField(max_length=50)),
                ('insurance_id', models.IntegerField()),
                ('date', models.DateField()),
                ('vehicle_type', models.CharField(max_length=50)),
                ('policy_type', models.CharField(max_length=50)),
                ('policy_amount', models.IntegerField()),
                ('insurance_start_date', models.DateField()),
                ('insurance_end_date', models.IntegerField()),
            ],
        ),
    ]
