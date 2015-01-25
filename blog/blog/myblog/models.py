from django.db import models
#from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=250)
    author=models.ForeignKey(User)
    up_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content=models.CharField(max_length=250)
    article=models.ForeignKey(Article)
    by=models.ForeignKey(User)
    is_approved=models.BooleanField(default=False)
    up_date=models.DateTimeField(auto_now_add=True)
    #my_field = tinymce_models.HTMLField()
    modified_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content[:30]