"""
This module strips unnecessary whitespaces from HTML.
    Author : Baseplate-Admin
"""


import asyncio
from typing import List
from .libs import minify
from django.utils.decorators import sync_and_async_middleware


from django.http.request import HttpRequest
from django.http.response import HttpResponse


@sync_and_async_middleware
def html_strip_whitespace(get_response):

    # One-time configuration and initialization goes here.
    ignored_paths: List = [
        "/sitemap.xml"  # Ignore Sitemap.xml because our code mangles with it.
    ]
    if asyncio.iscoroutinefunction(get_response):

        async def middleware(request: HttpRequest):
            # Do something here!
            response = await get_response(request)
            if not response.streaming and not request.path in ignored_paths:
                content = minify(response.content)
                response.content = content
            return response

    else:

        def middleware(request: HttpRequest) -> HttpResponse:
            # Do something here!
            response = get_response(request)
            if not response.streaming and not request.path in ignored_paths:
                content = minify(response.content)
                response.content = content
            return response

    return middleware
