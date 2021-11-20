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

*   It can automagically minify inline CSS, JS.
*   It speeds up website by reducing the HTML size.
*   Can be used with 'django.middleware.gzip.GZipMiddleware'.
*   Significantly lower bytes transferred when working with frameworks like AlpineJs & Petite Vue.
*   Its mostly based on C ( gzip ) and Rust ( `minify-html <https://pypi.org/project/minify-html/>`__  ) libraries.
*   Is very customizable. ( You can configure lower level `minify-html <https://github.com/wilsonzlin/minify-html/blob/master/python/src/lib.template.rs/>`_ rust bindings from settings.py )
*   Removes <!--prettier-ignore--> from HTML.

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

Use this CSS code:
    .. code-block:: css
       
       selector::before { 
           content : '\00a0\00a0'
       }
    
*   Although I tried my best to use Compiled Language for Optimizations.It can still be sub miliseconds slower compared to normal Django Rendering.


Requirements :
--------------

*    Brotli ( or BrotliPy )
*    minify-html
*    Django > 3 ( Should work with version 2? )
*    Python 3 ( Should work with all version? )

User guide :
============

Installation :
--------------

Install with pip from pypi::

      $ python -m pip install django_strip_whitespace

Install with pip from github ( Development | Not Recommended for Production )::
    
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

Change Lower Level Bindings :
-----------------------------

The module allows settings to be changed from Django's settings.py file. If you would like to change any settings, refer to `minify-html's <https://github.com/wilsonzlin/minify-html/blob/master/python/src/lib.template.rs/>`_ source code.


The bindings are ( by default set to True):

    .. code-block:: python

        STRIP_WHITESPACE_DO_NOT_MINIFY_DOCTYPE, # passes do_not_minify_doctype to minify-html
        STRIP_WHITESPACE_ENSURE_SPEC_CONPLIANT_UNQUOTED_ATTRIBUTE_VALUES, # passes ensure_spec_compliant_unquoted_attribute_values to minify-html
        STRIP_WHITESPACE_KEEP_CLOSING_TAGS, # passes keep_closing_tags to minify-html
        STRIP_WHITESPACE_KEEP_COMMENTS, # passes keep_comments to minify-html
        STRIP_WHITESPACE_KEEP_HTML_AND_HEAD_OPENING_TAGS, # passes keep_html_and_head_opening_tags to minify-html
        STRIP_WHITESPACE_KEEP_SPACES_BETWEEN_ATTRIBUTES, # passes keep_spaces_between_attributes to minify-html
        STRIP_WHITESPACE_MINIFY_CSS, # passes minify_css to minify-html
        STRIP_WHITESPACE_MINIFY_JS, # passes minify_js to minify-html
        STRIP_WHITESPACE_REMOVE_BANGS, # passes remove_bangs to minify-html
        STRIP_WHITESPACE_REMOVE_PROCESSING_INSTRUCTIONS, # passes remove_processing_instructions to minify-html

If you would like to change any of the above variables, simply put them in settings.py. Please note that every variable here is a python boolean.

For example:

    .. code-block:: python

        # settings.py

        STRIP_WHITESPACE_DO_NOT_MINIFY_DOCTYPE = False


Contributing :
==============
If you like this project add a star. 
If you have problems or suggestions please put them in the `Issue Tracker <https://github.com/baseplate-admin/django_strip_whitespace/issues>`__.
If you like to add features. Fork this repo and submit a Pull Request. 😛

Roadmap :
=========
*    Add line break to InlineJS
*    Add ZStandard Compression ? ( Should Work )
*    Do not remove '&nbsp;' from html
