from re import T
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class AddUser(AbstractUser):
    # manzil = models.CharField(max_length=100, null=True, blank=True)
    # nomi = models.CharField(max_length=50, null=True, blank=True)
    # tugilgan_kun = models.DateField(null=True, blank=True)
    # shahar = models.CharField(max_length=50, null=True, blank=True)
    telefon = models.CharField(max_length=30, null=True, blank=True)
    # lavozim = models.CharField(max_length=150, null=True, blank=True)
    # yunalish = models.CharField(max_length=150, null=True, blank=True)
    # maosh = models.PositiveBigIntegerField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='images/', null=True, blank=True)
    # til = models.CharField(max_length=300, null=True, blank=True)
    # ishchilar_soni = models.PositiveBigIntegerField(null=True, blank=True)
    # otasining_ismi = models.CharField(max_length=50, null=True, blank=True)
    