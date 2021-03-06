# Generated by Django 3.2.7 on 2021-09-29 17:34

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('registration_of_dogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationexhibition',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='registrationexhibition',
            name='name_of_dog',
        ),
        migrations.RemoveField(
            model_name='registrationexhibition',
            name='name_of_owner',
        ),
        migrations.RemoveField(
            model_name='registrationexhibition',
            name='type_of_exebition',
        ),
        migrations.AddField(
            model_name='registrationexhibition',
            name='additional_classes',
            field=models.ManyToManyField(blank=True, to='registration_of_dogs.AdditionalCategories', verbose_name='Имя хозяина'),
        ),
        migrations.AddField(
            model_name='registrationexhibition',
            name='dog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='dog', to='registration_of_dogs.dog', verbose_name='Кличка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrationexhibition',
            name='exebition',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='exebition', to='registration_of_dogs.exebition', verbose_name='Выставка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrationexhibition',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='owner', to='registration_of_dogs.owner', verbose_name='Имя хозяина'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Телефон владельца'),
        ),
    ]
