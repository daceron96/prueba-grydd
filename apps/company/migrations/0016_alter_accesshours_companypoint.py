# Generated by Django 4.1.2 on 2022-11-01 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0015_rename_endttime_accesshours_endtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesshours',
            name='companyPoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.companypoint'),
        ),
    ]
