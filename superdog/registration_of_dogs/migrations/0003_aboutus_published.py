# Generated by Django 3.2.7 on 2021-09-16 15:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registration_of_dogs', '0002_auto_20210916_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
