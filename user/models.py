
from django.db import models


class UserProfile(models.Model):
    ROLE_CHOICES=[
        ('employee','Employee'),
        ('owner','Owner')
    ]
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50, default='employee',choices= ROLE_CHOICES)

    class Meta:
        db_table = 'userProfiles'

    def __str__(self):
        return self.username
    
    @property
    def is_authenticated(self):
        return True

