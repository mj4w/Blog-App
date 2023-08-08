from django.db import models
from django.contrib.auth.models import User
# Create your models here.


    
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    id_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True)
    title = models.CharField(max_length=100)
    image = models.ImageField()
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    
    
    def __str__(self):
        return self.title