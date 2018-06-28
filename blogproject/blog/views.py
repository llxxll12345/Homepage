import markdown
from django.shortcuts import render, get_object_or_404

from .models import Post, Category, Tag
from comments.forms import commentForm
# Create your views here.

'''
def index(request):
    return HttpResponse("<h3>Welcome!</h3>")
'''

def make_zip(request, post_list, len=0, lenName=""):
    len_list = []
    for post in post_list:
        len_list.append(len(post.comment_set.all()))
    return render(request, 'blog/index.html', context={'post_list': zip(post_list, len_list), lenName: len})

def _index(request):
    return render(request, 'blog/index.html', context={'title':'My homepage', 'welcome': 'Hello!'})

def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return make_zip(request, post_list)

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body, extensions=['markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc'
                                  ])
    post.inc_views()
    form = commentForm(request.POST)
    comment_list= post.comment_set.all()
    cm_len = len(comment_list)
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list,
        'cm_len': cm_len
    }
    return render(request, 'blog/detail.html', context=context)



def archives(request, year, month):
    post_list = Post.objects.filter(create_time__year=year, create_time__month=month).order_by('-create_time')
    return make_zip(request, post_list)

def categories(request, pk):
    cate = get_object_or_404(Category, pk = pk)
    post_list = cate.post_set.all().order_by('-create_time')
    cate_len = len(post_list)
    return make_zip(request, post_list, cate_len, 'cate_len')

def tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    post_list = tag.post_set.all().order_by('-create_time')
    return make_zip(request, post_list)