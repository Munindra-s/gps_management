# Generated by Django 5.1.7 on 2025-03-10 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0032_add_gps_panan_phone_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_gps',
            name='ganesh',
        ),
        migrations.RemoveField(
            model_name='add_gps',
            name='munindra',
        ),
        migrations.RemoveField(
            model_name='add_gps',
            name='panan_phone_no',
        ),
    ]
