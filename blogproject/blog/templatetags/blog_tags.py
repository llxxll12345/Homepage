from ..models import Post, Category, Tag
from django import template

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def get_archives():
    return Post.objects.dates('create_time', 'month', order='DESC')

@register.simple_tag
def get_category():
    return Category.objects.all()

@register.simple_tag
def get_tag():
    return Tag.objects.all().order_by('-name')