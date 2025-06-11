from django.db import models
from user.models import UserProfile

class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    
    class Meta:
           db_table = 'userPosts'
    def __str__(self):
        return self.title