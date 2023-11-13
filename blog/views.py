from datetime import date

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Post, Author, Tag

posts_data = []


def get_post_date(post: {}):
    return post['date']


def starting_page(request: HttpRequest) -> HttpResponse:
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html',
                  context={'posts': latest_posts})


def posts(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/all_posts.html',
                  context={'all_posts': posts_data})


def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
    identified_post = next(post for post in posts_data if post['slug'] == slug)
    return render(request, 'blog/post_detail.html',
                  context={'post': identified_post})
