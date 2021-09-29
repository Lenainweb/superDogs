# Generated by Django 3.2.7 on 2021-09-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_of_dogs', '0002_auto_20210929_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionalcategories',
            name='category',
            field=models.TextField(default=1, max_length=50, verbose_name='Название категории'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='additionalcategories',
            name='discreption',
            field=models.TextField(default=1, max_length=50, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dog',
            name='champion_certificate_scanned',
            field=models.ImageField(blank=True, upload_to='files/download/champion_certificate', verbose_name='Сертификат чемпиона'),
        ),
        migrations.AlterField(
            model_name='registrationexhibition',
            name='additional_classes',
            field=models.ManyToManyField(blank=True, to='registration_of_dogs.AdditionalCategories', verbose_name='Дополнительные котегории'),
        ),
    ]
