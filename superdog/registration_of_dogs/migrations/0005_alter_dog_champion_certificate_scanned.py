# Generated by Django 3.2.7 on 2021-10-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_of_dogs', '0004_auto_20211003_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='champion_certificate_scanned',
            field=models.ImageField(blank=True, null=True, upload_to='files/download/champion_certificate', verbose_name='Сертификат чемпиона'),
        ),
    ]
