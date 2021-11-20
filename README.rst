HTML Whitespace remover for Django
==================================
|Pepy.tech Badge| |PyPi Version Badge| |Python Versions Badge| |License Badge|

.. |Pepy.tech Badge| image:: https://static.pepy.tech/personalized-badge/django-strip-whitespace?period=month&units=international_system&left_color=grey&right_color=orange&left_text=Downloads
   :target: https://pepy.tech/project/django-strip-whitespace

.. |PyPi Version Badge| image:: https://badge.fury.io/py/django-strip-whitespace.svg
    :target: https://badge.fury.io/py/django-strip-whitespace

.. |Python Versions Badge| image:: https://img.shields.io/pypi/pyversions/django-strip-whitespace
    :alt: PyPI - Python Version
    :target: https://github.com/baseplate-admin/django_strip_whitespace/blob/main/setup.py

.. |License Badge| image:: https://img.shields.io/pypi/l/django-strip-whitespace
   :alt: PyPI - License
   :target: https://github.com/baseplate-admin/django_strip_whitespace/blob/main/LICENSE

Introduction :
--------------
A powerful tool to optimize HTML

Why use "django_stip_whitespace" ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*   It speeds up website by reducing the HTML size.
*   Its mostly based on C ( gzip ) and Rust ( minify-html : https://pypi.org/project/minify-html/ ) libraries
*   Can be used with 'django.middleware.gzip.GZipMiddleware'
*   It can automagically minify inline CSS, JS.
*   Significantly lower bytes transferred ( 246kb > 16kb ) when working with frameworks like AlpineJs & Petite Vue.

Why souldn't you use django_stip_whitespace ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*   This Module expects that you write inline js with line breaks. 

So for example if you have a file like this:
   .. code-block:: html

       <div x-init="
               () => {
                   console.log('Hello World')
                   console.log("Hello World Again") // This will cause error because theres no ';' to break the line
               }
           "
       > </div>

The resulted HTML will have an error and AlpineJS won't init.

The Proper way to write:
   .. code-block:: html
        
        <div x-init="
               () => {
                   console.log('Hello World');
                   console.log("Hello World Again"); // This will work just fine
               }
           "
       > </div>

*   Disables the use of &nbsp; in HTML. Although this can be easily mitigated by using CSS pesudo element. 

Use this:
    .. code-block:: css
       
       selector::before { 
           content : '\00a0\00a0'
       }
    

Requirements :
--------------

*    Brotli (or BrotliPy)
*    minify-html
*    Django > 3 ( Should work with version 2? )
*    Python 3 ( Should work with all version? )

User guide :
============

Installation :
--------------

Install with pip from pypi::

      $ python -m pip install django_strip_whitespace

Install with pip from github ( Development )::
    
      $ python -m pip install https://codeload.github.com/baseplate-admin/django_strip_whitespace/zip/refs/heads/main


Then include it in your django project:
   
   .. code-block:: python
   
       MIDDLEWARE = [
           ...
           "strip_whitespace.middlewares.HtmlStripWhiteSpaceMiddleware.html_strip_whitespace",
       ]

Or if you like:
   
   .. code-block:: python
   
         MIDDLEWARE += "strip_whitespace.middlewares.HtmlStripWhiteSpaceMiddleware.html_strip_whitespace"


Contributing :
==============
If you like this project add a star. If you have problems or suggestions please put them in the `Issue Tracker <https://github.com/baseplate-admin/django_strip_whitespace/issues>`_.


Roadmap :
=========
*    Add line break to InlineJS
*    Add ZStandard Compression ? ( Should Work )
*    Do not remove '&nbsp;' from html
