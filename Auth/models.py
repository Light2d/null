from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class BaseInfo(models.Model):
    full_name = models.CharField(max_length=255, blank=False, verbose_name='Полное имя')
    email = models.EmailField(unique=True, blank=False, verbose_name='E-mail')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    photo = models.ImageField(upload_to='user_photos', blank=True, null=True, verbose_name='Фото')

    class Meta:
        abstract = True

class Role(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name='Роль')

    def __str__(self):
        return self.title

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        admin_role = Role.objects.get(id=1)
        extra_fields.setdefault('role',admin_role)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin, BaseInfo):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, blank=True, null=True, default='3', verbose_name='Роль', related_name='user_role')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

