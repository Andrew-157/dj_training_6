from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def starting_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/index.html')


def posts(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/all_posts.html')


def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
    pass
