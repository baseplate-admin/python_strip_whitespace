import pathlib
from setuptools import setup


long_description = (pathlib.Path(__file__).parent.resolve() / "README.rst").read_text(
    encoding="utf-8"
)

packages = [
    "strip_whitespace",
    "strip_whitespace.middlewares",
    "strip_whitespace.middlewares.libs",
    "strip_whitespace.middlewares.libs.functions",
    "strip_whitespace.middlewares.libs.functions.regex_patterns",
    "strip_whitespace.middlewares.libs.functions.rust_variables",
    "strip_whitespace.middlewares.libs.functions.compressors",
    "strip_whitespace.middlewares.libs.functions.decompressors",
]


package_data = {"": ["*"]}

install_requires = [
    "Brotli; implementation_name == 'cpython'",
    "brotlipy; implementation_name == 'PyPy'",
    "django>3",
    "minify-html",
]

setup_kwargs = setup(
    name="django-strip-whitespace",
    version="0.1.0",
    description="A powerful HTML whitespace remover",
    long_description=long_description,
    author="baseplate-admin",
    author_email="zarifahanf@outlook.com",
    # 'maintainer': 'baseplate-admin',
    # 'maintainer_email': None,
    keywords="django alpinejs middleware",
    url="https://github.com/baseplate-admin/django_strip_whitespace",
    packages=packages,
    package_data=package_data,
    install_requires=install_requires,
    # zip_safe=False,
    python_requires=">=3.6, <3.11",
    license="GPLv3",
    platforms="any",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only ",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
