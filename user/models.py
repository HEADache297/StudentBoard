from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class CustomUserManger(BaseUserManager):
    def create_user(self, email, password=None,  **extra_field):
        if not email :
            raise ValueError('User must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            **extra_field,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_field):
        user = self.create_user(
            email = self.normalize_email(email),
            **extra_field,
            password = password,
            is_superuser=True,
        )
        
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        
        user.save(using=self._db)
        return user
    


class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_parents = models.BooleanField(default=False)

    username = models.CharField(max_length=50, default='user')
    email=models.EmailField(null=False, blank=False, unique=True)
    name=models.CharField(null=False, max_length=50)
    surname=models.CharField(null=False, max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','surname']
    objects = CustomUserManger()


    def save(self, *args, **kwargs):
        if not self.username:
            self.username = f'{self.name} {self.surname}'
        super().save(*args, **kwargs)

    def  __str__(self):
        return f'{self.name} {self.surname} {self.email}'

    def __repr__(self):
        return f'{self.name} {self.surname} {self.email}'