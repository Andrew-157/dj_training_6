from datetime import date

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


posts_data = [
    {"slug": "hike-in-the-mountains",
     "image": "mountains.jpg",
     "author": "Andrew-157",
     "date": date(2023, 7, 14),
     "title": "Mountain Hiking",
     "excerpt": """Mountain Hiking is amazing activity.
                    It is good for both your physical and mental health.""",
     "content": """ 
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus, delectus.
        Corrupti repellendus magni, assumenda eos provident officiis ipsam recusandae ad,
        necessitatibus quae dolore aliquid, temporibus totam fugit dicta officia porro!

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus, delectus.
        Corrupti repellendus magni, assumenda eos provident officiis ipsam recusandae ad,
        necessitatibus quae dolore aliquid, temporibus totam fugit dicta officia porro!

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus, delectus.
        Corrupti repellendus magni, assumenda eos provident officiis ipsam recusandae ad,
        necessitatibus quae dolore aliquid, temporibus totam fugit dicta officia porro!       
        """},
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Andrew-157",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Andrew-157",
        "date": date(2023, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
]


def get_post_date(post: {}):
    return post['date']


def starting_page(request: HttpRequest) -> HttpResponse:
    sorted_posts = sorted(posts_data, key=get_post_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html',
                  context={'posts': latest_posts})


def posts(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/all_posts.html',
                  context={'all_posts': posts_data})


def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
    identified_post = next(post for post in posts_data if post['slug'] == slug)
    return render(request, 'blog/post_detail.html',
                  context={'post': identified_post})
