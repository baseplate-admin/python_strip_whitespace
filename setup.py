import pathlib
from setuptools import setup


long_description = (pathlib.Path(__file__).parent.resolve() / "README.rst").read_text(
    encoding="utf-8"
)

packages = [
    "python_strip_whitespace",
    "python_strip_whitespace.html",
    "python_strip_whitespace.functions",
    #    "python_strip_whitespace.functions.compressors",
    #   "python_strip_whitespace.functions.decompressors",
    "python_strip_whitespace.functions.regex_patterns",
]


package_data = {"": ["python_strip_whitespace/*"]}
extras_require = {
    "brotli": [
        "Brotli; implementation_name == 'cpython'",
        "brotlipy; implementation_name == 'PyPy'",
    ],
    "zstd": ["zstd"],
}

install_requires = [
    "minify-html",
]

setup_kwargs = setup(
    name="python-strip-whitespace",
    version="0.0.3",
    description="A powerful HTML whitespace remover for python",
    long_description=long_description,
    author="baseplate-admin",
    author_email="zarifahanf@outlook.com",
    # 'maintainer': 'baseplate-admin',
    # 'maintainer_email': None,
    keywords="python3 alpinejs html5 js css",
    url="https://github.com/baseplate-admin/python_strip_whitespace",
    packages=packages,
    package_data=package_data,
    install_requires=install_requires,
    extras_require=extras_require,
    # zip_safe=False,
    python_requires=">=3.7, <3.11",
    license="GPLv3",
    platforms="any",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only ",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
