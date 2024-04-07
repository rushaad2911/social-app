from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid 

class Post(models.Model):
    
    GERENS =(
        ('P','Photography'),
        ('F','Food'),
        ('A','Art'),
    )
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    post_title = models.CharField(max_length=30,blank=True,null=True)
    post_image = models.ImageField(upload_to = 'photo/',blank=True,null=True)
    gerens = models.CharField(max_length=50,choices=GERENS,null=True,blank=True)
    post_user = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
        blank=True,
        null=True
                                  )
    
    def get_absolute_url(self):
        return reverse('detailpostview',args=[str(self.id)])
    
    def delete(self,*args,**kwargs):
        self.post_image.delete()
        return super().delete(*args,**kwargs)
    
    