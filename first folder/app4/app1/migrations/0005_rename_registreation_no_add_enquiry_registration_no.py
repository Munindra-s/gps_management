# Generated by Django 5.1.6 on 2025-02-26 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_add_enquiry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_enquiry',
            old_name='registreation_no',
            new_name='registration_no',
        ),
    ]
