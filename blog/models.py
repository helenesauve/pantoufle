from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE,
    )
    body = models.TextField(
        default='SOME STRING'
    )

def __str__(self):
    return self.title