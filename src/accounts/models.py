from django.db import models
from django.utils.timezone import now
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):

    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"

    first_name = models.CharField("Ім'я", max_length=32)
    last_name = models.CharField("Прізвище", max_length=32)
    email = models.EmailField("Email")
    age = models.IntegerField("Вік")
    phone_number = PhoneNumberField(
            "Номер телефону",
            null=True,
            blank=True,
            unique=True
    )
    create_date = models.DateTimeField(
            "Дата створення",
            blank=True,
            null=True,
            default=now
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Seller(models.Model):

    class Meta:
        verbose_name = "Продавець"
        verbose_name_plural = "Продавці"

    first_name = models.CharField("Ім'я", max_length=32)
    last_name = models.CharField("Прізвище", max_length=32)
    age = models.IntegerField("Вік")
    phone_number = PhoneNumberField(
            "Номер телефону",
            blank=True,
            null=True,
            unique=True
    )
    role = models.CharField("Роль", max_length=32)
    experience = models.IntegerField("Стаж роботи")
    create_date = models.DateTimeField(
            "Дата створення",
            blank=True,
            null=True,
            default=now
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
