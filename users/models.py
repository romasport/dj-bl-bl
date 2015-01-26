# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email),
            username=username,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email,
                                password=password,
                                username=username
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=255,
        unique=True,
        db_index=True,)
    username = models.CharField(verbose_name='Ник',  max_length=255, unique=True)
    avatar = models.ImageField(verbose_name='Аватар',  upload_to='images/%Y/%m/%d', blank=True, null=True)
    first_name = models.CharField(verbose_name='Имя',  max_length=255, blank=True)
    last_name = models.CharField(verbose_name='Фамилия',  max_length=255, blank=True)
    date_of_birth = models.DateField(verbose_name='День рождения',  blank=True, null=True)
    achievements = models.ManyToManyField('Achievement', verbose_name='Звание', through='UserAchievement')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name,)

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Achievement(models.Model):
    title = models.CharField(verbose_name='Звание',  max_length=500, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    active_icon = models.ImageField(verbose_name='Иконка активного звания', upload_to='uploads/Achievement/')
    inactive_icon = models.ImageField(verbose_name='Иконка не активного звания', upload_to='uploads/Achievement/')

    def __unicode__(self):
        return self.title

class UserAchievement(models.Model):
    user = models.ForeignKey(User, verbose_name=(u'user'))
    achievement = models.ForeignKey('Achievement', verbose_name=(u'achievement'))
    note = models.TextField((u'note'), blank=True)

    class Meta:
        verbose_name = (u'user achievement')
        verbose_name_plural = (u'user achievements')
        unique_together = (('user', 'achievement'),)