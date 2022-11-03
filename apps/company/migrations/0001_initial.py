# Generated by Django 4.1.2 on 2022-11-02 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('nit', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('icon', models.ImageField(blank=True, upload_to='icons/')),
                ('companyName', models.CharField(max_length=100)),
                ('tradeName', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('webSite', models.URLField(max_length=100)),
                ('state', models.BooleanField(default=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.address')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.location')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('geolocation', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.BooleanField(default=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.address')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='AccessHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('companyPoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.companypoint')),
            ],
        ),
    ]
