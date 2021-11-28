from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password):
        
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Usuario', max_length=20, unique=True)
    email = models.EmailField('Email', max_length=100)
    telefono = models.CharField('Telefono', max_length=10 )
    direccion = models.CharField('Direccion', max_length=25)
    password = models.CharField('Password', max_length=150)
    superuser= models.CharField('superuser', max_length=100)

    
    def save(self, **kwargs):
        some_salt =''
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
        
    objects = UserManager()
    USERNAME_FIELD = 'username'    
        
        