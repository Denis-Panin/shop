from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    first_name = models.CharField("Ім'я", max_length=32)
    last_name = models.CharField("Прізвище", max_length=32)
    email = models.EmailField("Email")
    age = models.IntegerField("Вік")
    phone_number = PhoneNumberField("Номер телефону", null=True, blank=True, unique=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
