"""
This module strips unnecessary whitespaces from HTML.
    Author : Baseplate-Admin
"""


# class HTMLStripWhiteSpace(MiddlewareMixin):
#     def __init__(self, get_response) -> NoReturn:
#         self.get_response = get_response
#         self.ignored_path: List = [
#             "/sitemap.xml"  # Ignore Sitemap.xml because our code mangles with it.
#         ]

#     def __call__(self, request: HttpRequest) -> HttpResponse:
#         response = self.get_response(request)  # Get response from view function.

# if not response.streaming and not request.path in self.ignored_path:
#     content = minify(response.content)
#     response.content = content
# return response


import asyncio
from typing import List
from .libs import minify
from django.utils.decorators import sync_and_async_middleware


from django.http.request import HttpRequest
from django.http.response import HttpResponse


@sync_and_async_middleware
def HTMLStripWhiteSpace(get_response):
    ignored_paths: List = [
        "/sitemap.xml"  # Ignore Sitemap.xml because our code mangles with it.
    ]
    # One-time configuration and initialization goes here.
    if asyncio.iscoroutinefunction(get_response):

        async def middleware(request: HttpRequest):
            # Do something here!
            response = await get_response(request)
            if not response.streaming and not request.path in ignored_paths:
                content = minify(response.content)
                response.content = content
            return response

    else:

        def middleware(request: HttpRequest):
            # Do something here!
            response = get_response(request)
            if not response.streaming and not request.path in ignored_paths:
                content = minify(response.content)
                response.content = content
            return response

    return middleware
