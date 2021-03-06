from django.db import models

# Create your models here.
from django.urls import reverse

class Comment(models.Model):
    name = models.CharField(max_length=100);
    email = models.EmailField(max_length=100);
    url = models.URLField(blank=True)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:10]

class Contact (models.Model):
    name = models.CharField(max_length=100);
    email = models.EmailField(max_length=100);
    subject = models.CharField(max_length=500);
    text = models.TextField(max_length=1000);

    def __str__(self):
        return self.text[:10]