from django.db import models


class Admin(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField('Usuario', max_length=20, unique=True)
    email = models.EmailField('Email', max_length=100)
    password = models.CharField('Password', max_length= 256)