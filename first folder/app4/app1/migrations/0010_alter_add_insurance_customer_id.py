# Generated by Django 5.1.6 on 2025-03-06 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_add_insurance_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_insurance',
            name='customer_id',
            field=models.CharField(max_length=60),
        ),
    ]
