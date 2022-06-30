from datetime import timezone
from turtle import title
from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(unique = True,null = True)
    c_time = models.DateTimeField(auto_now_add=True,null = True)
    m_time = models.DateTimeField(auto_now=True,null = True)
    email = models.EmailField(unique = True,null = True)
    password = models.CharField(max_length=256,null = True)

    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ["-c_time"]
        verbose_name = "user"
        verbose_name_plural = "user"

class giftcard(models.Model):
    giftcard_id = models.IntegerField(unique = True, default=0)
    user_id = models.IntegerField(default=0)
    c_time = models.DateTimeField(auto_now_add=True,null = True)
    m_time = models.DateTimeField(auto_now=True,null = True)
    title = models.CharField(max_length=256,default = 'DEFAULT VALUE')
    email = models.EmailField(unique = True,null = True)
    content = models.TextField(null = True)

    def __str__(self):
        return self.title

