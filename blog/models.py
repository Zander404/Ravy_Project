from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
import uuid, os
from .tools import post_banner_directory_path


# Create your models here.
class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('Não foi definido um email, por favor adicione um email!')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        def create_user(self, username=None, email=None, password=None, **extra_fields):
            extra_fields.setdefault('is_staff', False)
            extra_fields.setdefault('is_superuser', False)
            return self._create_user(username, email, password, **extra_fields)

        def create_superuser(self, username=None, email=None, password=None, **extra_fields):
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to='uploads/avatars', default='')

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def avatar_url(self):
        if self.avatar:
            return f'{settings.WEBSITE_URL}/{self.avatar_url}'
        else:
            return ''

    def __str__(self):
        return self.username


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    content = models.TextField(blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    banner = models.ImageField(upload_to=post_banner_directory_path)

    def delete(self, *args, **kwargs):
        # Deleta o arquivo de imagem associado ao post
        if self.banner:
            if os.path.isfile(self.banner.path):
                os.remove(self.banner.path)
        # Chama o método delete do modelo para deletar o objeto
        super().delete(*args, **kwargs)

    def banner_url(self):
        if self.banner:
            return f'{self.banner.url}'


def __str__(self):
    return self.title
