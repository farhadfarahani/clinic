from django.db import models
from django.core.validators import RegexValidator
from django.shortcuts import reverse


class Doctor(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    expertise = models.CharField(max_length=100)
    visiting_days = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    address = models.TextField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="شماره تلفن باید در فرمت صحیح باشد.")
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.lastname, self.firstname

    def get_absolute_url(self):
        return reverse('doctor_detail', args=[self.pk])
