HTML Whitespace remover for Python
==================================
|Pepy.tech Badge| |PyPi Version Badge| |Python Versions Badge| |License Badge| |Code Style|

.. |Pepy.tech Badge| image:: https://static.pepy.tech/personalized-badge/python-strip-whitespace?period=week&units=international_system&left_color=grey&right_color=orange&left_text=Downloads
   :target: https://pepy.tech/project/python-strip-whitespace

.. |PyPi Version Badge| image:: https://badge.fury.io/py/python-strip-whitespace.svg
    :target: https://badge.fury.io/py/python-strip-whitespace

.. |Python Versions Badge| image:: https://img.shields.io/pypi/pyversions/python-strip-whitespace
    :alt: PyPI - Python Version
    :target: https://github.com/baseplate-admin/python_strip_whitespace/blob/main/setup.py

.. |License Badge| image:: https://img.shields.io/pypi/l/python-strip-whitespace
   :alt: PyPI - License
   :target: https://github.com/baseplate-admin/python_strip_whitespace/blob/main/LICENSE
   
.. |Code Style| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :alt: Code Style
   
Introduction :
--------------
A powerful tool to optimize HTML

Why use "python_stip_whitespace" ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*   Adds line break to InlineJS.
*   It can automagically minify inline CSS, JS.
*   Removes <!--prettier-ignore--> from HTML.
*   It speeds up website by reducing the HTML size.
*   It compiles regex at runtime. So it's blazing fast.
*   Its mostly based on C ( gzip ) and Rust ( `minify-html <https://pypi.org/project/minify-html/>`__  ) libraries.
*   Significantly lower bytes transferred when working with frameworks like AlpineJs ( Almost fully working & Please open a issue in the `Issue Tracker <https://github.com/baseplate-admin/django_strip_whitespace/issues>`__ if you encounter any bug) & Petite Vue.
*   Is very customizable. ( You can configure lower level `minify-html <https://github.com/wilsonzlin/minify-html/blob/master/python/src/lib.template.rs/>`_ rust bindings and also the lower level `python <https://github.com/juancarlospaco/css-html-js-minify/blob/master/css_html_js_minify/html_minifier.py/>`_ bindings from .env files )


Why souldn't you use python_stip_whitespace ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*   Adds unnecessary ';;' in HTML. ( If you know any regex to fix this please put a pull request )

*   Although I tried my best to use Compiled Language for Optimizations. It can still be sub miliseconds ( > 0.001 ) slower compared to normal Django Rendering. ( If you know any way to improve performance, please put a pull request )


Requirements :
--------------

*    minify-html
*    Python 3 ( Should work with all version? )
*    Brotli ( or BrotliPy ) | ( Optional )
*    ZSTD ( Optional ) 

Used Internally by :
====================
*     `django-strip-whitespace <https://github.com/baseplate-admin/django_strip_whitespace>`_
*     `flask-strip-whitespace <https://github.com/baseplate-admin/flask_strip_whitespace>`_

Contributing :
==============
If you like this project add a star. 
If you have problems or suggestions please put them in the `Issue Tracker <https://github.com/baseplate-admin/python_strip_whitespace/issues>`__.
If you like to add features. Fork this repo and submit a Pull Request. 😛

Roadmap :
=========
You tell me. If i have free time, I will implement it.
