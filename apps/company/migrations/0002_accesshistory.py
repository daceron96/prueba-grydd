# Generated by Django 4.1.2 on 2022-11-03 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_person_qrcode'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkIn', models.DateTimeField(auto_now_add=True)),
                ('checkOut', models.DateField(auto_now=True)),
                ('state', models.BooleanField(default=True)),
                ('accessHour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.accesshours')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.person')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]