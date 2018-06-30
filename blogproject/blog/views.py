import markdown
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Category, Tag
from comments.forms import commentForm
from comments.models import Comment
# Create your views here.

'''
def index(request):
    return HttpResponse("<h3>Welcome!</h3>")
'''

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # get objects and parameters from context
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        #create paginiation data pack
        pagination_data = self.pagination_data(paginator, page, is_paginated)

        #update context
        context.update(pagination_data)
        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}
        #1  ... 10 11 12 ... 19
        left_pgs= []
        right_pgs = []
        l_has_next = False
        r_has_next = False
        reach_head = False
        reach_last = False
        pg_number = page.number
        tot_pgs = paginator.num_pages
        pg_range = paginator.page_range
        if pg_number == 1:
            right_pgs = pg_range[pg_number: pg_number + 2] # 1 pages to the right
            if len(right_pgs) > 0:
                if right_pgs[-1] < tot_pgs - 1:
                    r_has_next = True
                elif right_pgs[-1] == tot_pgs - 1:
                    reach_last = True
                    r_has_next = False
        elif pg_number == tot_pgs:
            l_range = 0
            if pg_number - 2 > 0:
                l_range = pg_number-2
            left_pgs = pg_range[l_range:pg_number-1] # 2 pages to the left
            if len(left_pgs) > 0:
                if left_pgs[0] > 2:
                    l_has_next = True
                elif left_pgs[0] == 2:
                    l_has_next = False
                    reach_head = True
        else:
            l_range = 0
            if pg_number - 2 > 0:
                l_range = pg_number - 2

            left_pgs = pg_range[l_range: pg_number-1]
            right_pgs = pg_range[pg_number: pg_number + 2]
            if right_pgs[-1] < tot_pgs - 1:
                r_has_next = True
            elif right_pgs[-1] == tot_pgs - 1:
                reach_last = True
                r_has_next = False
            if left_pgs[0] > 2:
                l_has_next = True
            elif left_pgs[0] == 2:
                reach_head = True
                l_has_next = False

        print(list(left_pgs), list(right_pgs))
        data = {
            'left': left_pgs,
            'right': right_pgs,
            'left_has_more': l_has_next,
            'right_has_more': r_has_next,
            'first': reach_head,
            'last': reach_last,
        }

        return data

class CategoryView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category = cate)

def make_zip(request, post_list, length=0, lenName=""):
    len_list = []
    for post in post_list:
        len_list.append(len(Comment.objects.all().filter(post = post)))
    return render(request, 'blog/index.html', context={'post_list': zip(post_list, len_list), lenName: str(length)})

def _index(request):
    return render(request, 'blog/index.html', context={'title':'My homepage', 'welcome': 'Hello!'})

def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body, extensions=['markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc'
                                  ])
    post.inc_views()
    post.save()
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

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        # return HttpResponse object
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.inc_views()
        return response

    def get_queryset(self):
        return super(PostDetailView, self).get_queryset().filter(pk = self.kwargs.get('pk'))

    def get_object(self, queryset=None):
        post = super(PostDetailView, self).get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                      extensions=['markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = commentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context

def archives(request, year, month):
    post_list = Post.objects.filter(create_time__year=year, create_time__month=month).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def categories(request, pk):
    cate = get_object_or_404(Category, pk = pk)
    post_list = cate.post_set.all().order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def tags(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    post_list = tag.post_set.all().order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})