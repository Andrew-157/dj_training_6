from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse

from .models import Post, Author, Tag


def starting_page(request: HttpRequest) -> HttpResponse:
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html',
                  context={'posts': latest_posts})


def posts(request: HttpRequest) -> HttpResponse:
    all_posts = Post.objects.all().order_by("-date")
    return render(request, 'blog/all_posts.html',
                  context={'all_posts': all_posts})


def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html',
                  context={'post': identified_post})
