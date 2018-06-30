from ..models import Post, Category, Tag
from django import template
from django.db.models.aggregates import Count
register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.order_by('-create_time')[:num]

@register.simple_tag
def get_archives():
    return Post.objects.dates('create_time', 'month', order='DESC')

@register.simple_tag
def get_category():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
def get_tag():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0).order_by('-name')