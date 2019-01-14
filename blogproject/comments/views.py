from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

import smtplib
from email.mime.text import MIMEText

from .models import Comment
from .forms import commentForm, contactForm

def get_comments(request, post_pk):
    post = get_object_or_404(Post, pk = post_pk)
    comment_list = post.comment_set.all()
    context = {'post': post, 'comment_list': comment_list, 'cm_len': len(comment_list)}
    return render(request, 'blog/detail.html', contex=context)

def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk = post_pk)
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

        else:
            comment_list = post.comment_set.all()
            context = {
                'post': post, 'form': form, 'comment_list': comment_list
            }
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)

def post_contact_msg(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            #send_email(comment.name, comment.email, comment.subject, comment.text)
        else:
            context = {
                'form': form, 'has_err': True
            }
            return render(request, 'blog/contact.html', context=context)
    return redirect('../../')
