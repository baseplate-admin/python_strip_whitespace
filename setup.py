import pathlib
from setuptools import setup


long_description = (pathlib.Path(__file__).parent.resolve() / "README.rst").read_text(
    encoding="utf-8"
)

packages = [
    "strip_whitespace",
    "strip_whitespace.middlewares",
    "strip_whitespace.middlewares.libs",
    "strip_whitespace.middlewares.libs.html",
    "strip_whitespace.middlewares.libs.content",
    "strip_whitespace.middlewares.libs.variables",
    "strip_whitespace.middlewares.libs.compressors",
    "strip_whitespace.middlewares.libs.decompressors",
]


package_data = {"": ["*"]}

install_requires = [
    "Brotli; implementation_name != 'PyPy'",
    "brotlipy; implementation_name == 'PyPy'",
    "django>3",
    "minify-html",
]

setup_kwargs = setup(
    name="django-strip-whitespace",
    version="0.0.16",
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
    python_requires=">=3.6",
    license="GPLv3",
    platforms="any",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3 :: Only ",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
