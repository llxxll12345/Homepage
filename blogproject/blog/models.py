from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.html import strip_tags
import markdown
from comments.models import Comment
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField();

    create_time = models.DateTimeField();
    modified_time = models.DateTimeField();

    exerpt = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)


    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views  = models.PositiveIntegerField(default=0)

    def inc_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk' : self.pk})

    def save(self, *args, **kwargs):
        if not self.exerpt:
            md = markdown.Markdown(extensions=['markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc'
                                  ])
            self.exerpt = strip_tags(md.convert(self.body))[:54] + '...'
        super(Post, self).save(*args, **kwargs)
