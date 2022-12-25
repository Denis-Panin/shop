# Generated by Django 4.1.3 on 2022-12-25 15:41

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_seller_alter_user_age_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seller',
            options={'verbose_name': 'Продавець', 'verbose_name_plural': 'Продавці'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Користувач', 'verbose_name_plural': 'Користувачі'},
        ),
        migrations.AlterField(
            model_name='seller',
            name='age',
            field=models.IntegerField(verbose_name='Вік'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='experience',
            field=models.IntegerField(verbose_name='Стаж роботи'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='first_name',
            field=models.CharField(max_length=32, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='seller',
            name='last_name',
            field=models.CharField(max_length=32, verbose_name='Прізвище'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Номер телефону'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='role',
            field=models.CharField(max_length=32, verbose_name='Роль'),
        ),
    ]
