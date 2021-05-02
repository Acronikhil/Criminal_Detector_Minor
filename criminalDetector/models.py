from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# from django.contrib.auth.models import

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, email, name, password, gender, image, idCardImg, position, contact):
        if not email:
            raise ValueError('Police user must have an Email Address')
        if not name:
            raise ValueError('Police user must have name')

        users = self.model(email=self.normalize_email(email),
                           name=name, password=password, gender=gender, image=image, idCardImg=idCardImg, contact=contact, position=position)

        # user.set_password(password)
        users.save(using=self._db)
        return users

    # def create_superuser(self, email, name, password, gender):
    #     user = self.model(email=self.normalize_email(email),
    #                       name=name, password=password, gender=gender)

    #     # user.set_password(password)
    #     user.is_admin = True
    #     user.is_superuser = True
    #     user.is_staff = True
    #     user.save(user=self._db)
    #     return user


class MyAccountManagers(BaseUserManager):
    def create_user(self, name, gender, image, relativeContact, crimeDetail, address, contact):
        if not name:
            raise ValueError('Criminal must have Name')

        users = self.model(name=name, gender=gender, image=image,
                           contact=contact, relativeContact=relativeContact, crimeDetail=crimeDetail, address=address)

        # user.set_password(password)
        users.save(using=self._db)
        return users

    # def create_superuser(self, email, name, password, gender):
    #     user = self.model(email=self.normalize_email(email),
    #                       name=name, password=password, gender=gender)

    #     # user.set_password(password)
    #     user.is_admin = True
    #     user.is_superuser = True
    #     user.is_staff = True
    #     user.save(user=self._db)
    #     return user


class police(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    position = models.CharField(max_length=100)
    contact = PhoneNumberField(unique=True)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    image = models.ImageField(upload_to='pics')
    idCardImg = models.ImageField(upload_to='idCard')
    date_joined = models.DateTimeField(
        verbose_name='date joined',  auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    def __str__(self):
        return self.name + ', Email: ' + self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lebel):
        return True


class criminal(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Criminal_Images')
    # idCardImg = models.ImageField(upload_to='idCard')
    crimeDetail = models.CharField(max_length=5000)
    contact = PhoneNumberField(unique=True)
    relativeContact = PhoneNumberField(unique=True)
    # email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=500)

    objects = MyAccountManagers()

    def has_module_perms(self, app_lebel):
        return True
