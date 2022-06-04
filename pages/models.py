from django.db import models
from datetime import datetime
# Create your models here.

class Buyurtmachi(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    gmail = models.EmailField()
    parol = models.CharField(max_length=20)
    shahar = models.CharField(max_length=150)
    manzil = models.CharField(max_length=150)

    def __str__(self):
        return self.ism

class Mutaxasis(models.Model):
    ism = models.CharField(max_length=150)
    familya = models.CharField(max_length=150)
    otasining_ismi = models.CharField(max_length=150)
    rasm = models.ImageField(upload_to='images/') 
    tugilgan_sana = models.DateField()
    shahar = models.CharField(max_length=150)
    manzil = models.CharField(max_length=150)
    telefon = models.CharField(max_length=150)
    email = models.EmailField()
    lavozim = models.CharField(max_length=550)
    yonalish = models.CharField(max_length=550)
    maosh = models.PositiveIntegerField()
    portfolio = models.ImageField(upload_to='images/')
    sertifikat = models.ImageField(upload_to='images/')
    til = models.CharField(max_length=200)

    def __str__(self):
        return self.ism


class Firmalar(models.Model):
    nomi = models.CharField(max_length=200)
    yonalish = models.CharField(max_length=200)
    litsenzya = models.ImageField(upload_to='images/', null=True, blank=True)
    ishchi_soni = models.PositiveIntegerField()
    portfolio = models.ImageField(upload_to='images/', null=True, blank=True)
    logotip = models.ImageField(upload_to='images/', null=True, blank=True)
    mobile_number = models.CharField(max_length=50, null=True, blank=False)
    email_address = models.EmailField(max_length=100, null=True, blank=False)
    telegram_address = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.nomi



class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    summery = models.CharField(max_length=200)
    photo = models.ImageField(upload_to= 'images/')
    def __str__(self):
        return self.title

class Buyurtma(models.Model):
    title_buyurtma = models.CharField(max_length=200)
    body_buyurtma = models.TextField()
    summary_buyurtma = models.CharField(max_length=200)
    price_buyurtma = models.PositiveIntegerField()
    # photo_buyurtma = models.ImageField(upload_to='images/')
    muddat = models.DateField()
    telefon_raqam = models.CharField(max_length=50, null=True, blank=False)
    aloqa_uchun_email_manzil = models.EmailField(max_length=100, null=True, blank=False)
    room_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    telegram = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title_buyurtma



class Buyurtmabajarish(models.Model):
    tel_nomer = models.CharField(max_length=20)
    buyurtmachi_name = models.CharField(max_length=20)
    tg_user = models.CharField(max_length=30)
    taklif = models.TextField()
    price = models.PositiveIntegerField()
    
    

#chat models
class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    value = models.CharField(max_length=10000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    room = models.CharField(max_length=1000000)
    user = models.CharField(max_length=1000000)