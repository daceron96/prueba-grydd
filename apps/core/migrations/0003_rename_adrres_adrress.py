# Generated by Django 4.1.2 on 2022-10-26 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_rename_status_companypoint_state'),
        ('core', '0002_adrres_district'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Adrres',
            new_name='Adrress',
        ),
    ]
