HTML Whitespace remover for Django
=================================

Introduction :
--------------
A powerful tool to optimize HTML

Why use "django_stip_whitespace" ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*   It speeds up website by reducing the HTML size.
*   Its mostly based on C ( gzip ) and Rust ( minify-html : https://pypi.org/project/minify-html/ ) libraries
*   Can be used with 'django.middleware.gzip.GZipMiddleware'
*   It can automagically minify inline CSS, JS

Why souldn't you use django_stip_whitespace ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*   This Module expects that you write js with line breaks. 

So for example if you have a file like this::

    <div x-init="
            () => {
                console.log('Hello World')
                console.log("Hello World Again") // This will cause error because theres no ;
            }
        "
    > </div>

The resulted HTML will have an error and AlpineJS won't init.

  

Requirements :
--------------

*    Django > 3 ( Should work with version 2? )
*    Brotli
*    minify-html
*    Python 3 ( Should work with all version? )

User guide :
============

Installation :
--------------

Install with pip from pypi::

    python -m pip install django_stip_whitespace

Install with pip from github::
    
    python -m pip install https://codeload.github.com/baseplate-admin/django_strip_whitespace/zip/refs/heads/main


Then include it in your django project::

    MIDDLEWARE = [
        ...
        "django_strip_whitespace.middlewares.HtmlStripWhiteSpaceMiddleware.HTMLStripWhiteSpace",
    ]

Or if you like::

    MIDDLEWARE += "django_strip_whitespace.middlewares.HtmlStripWhiteSpaceMiddleware.HTMLStripWhiteSpace"


Contributing :
==============
I created this project for my own use.
But feel free to Contribute in any way possible.
If you like this project add a star.


Roadmap :
=========
*    Add line break to InlineJS
*    Add Brotli Compression ? ( Should Work )