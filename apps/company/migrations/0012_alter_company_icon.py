# Generated by Django 4.1.2 on 2022-10-26 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_alter_company_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='icon',
            field=models.ImageField(upload_to='icons/'),
        ),
    ]