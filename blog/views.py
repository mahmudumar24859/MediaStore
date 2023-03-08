from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from .decorators import *
from django.core.mail import EmailMessage
from members.models import SubscribedUser
from django.views.generic import UpdateView
from django.contrib import messages


def blogs(request):
    posts = BlogPost.objects.all()
    posts = BlogPost.objects.filter().order_by('-dateTime')
    return render(request, "blog.html", {'posts': posts})


def blogs_comments(request, id):
    post = BlogPost.objects.filter(id=id).first()
    comments = Comment.objects.filter(blog=post)
    if request.method == "POST":
        user = request.user
        content = request.POST.get('content', '')
        blog_id = request.POST.get('blog_id', '')
        comment = Comment(user=user, content=content, blog=post)
        comment.save()
    return render(request, "blog_comments.html", {'post': post, 'comments': comments})


@user_is_superuser
def Delete_Blog_Post(request, id):
    posts = BlogPost.objects.get(id=id)
    if request.method == "POST":
        posts.delete()
        return redirect('/')
    return render(request, 'delete_blog_post.html', {'posts': posts})


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        blogs = BlogPost.objects.filter(title__contains=searched)
        return render(request, "search.html", {'searched': searched, 'blogs': blogs})
    else:
        return render(request, "search.html", {})


@login_required(login_url='/login')
def add_blogs(request):
    if request.method == "POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            return render(request, "add_blogs.html", {'obj': obj})
    else:
        form = BlogPostForm()
    return render(request, "add_blogs.html", {'form': form})


class UpdatePostView(UpdateView):
    model = BlogPost
    template_name = 'edit_blog_post.html'
    fields = ['title', 'content', 'image']


def user_profile(request, myid):
    post = BlogPost.objects.filter(id=myid)
    return render(request, "user_profile.html", {'post': post})


@user_is_superuser
def newsletter(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            recievers = form.cleaned_data.get('recievers').split(', ')
            email_message = form.cleaned_data.get('message')

            mail = EmailMessage(
                subject, email_message, f'Al-intisar Prints <{request.user.email}>', bcc=recievers)
            mail.content_subtype = 'html'

            if mail.send():
                messages.success(request, 'Email Sends successfully')
            else:
                messages.error(request, 'There was an error sending message!')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('/')

    form = NewsLetterForm()
    form.fields['recievers'].initial = ', '.join(
        [active.email for active in SubscribedUser.objects.all()])

    return render(request, 'newsletter.html', {'form': form})
