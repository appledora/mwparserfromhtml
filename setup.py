from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.3'
DESCRIPTION = 'Wikipedia HTML Dump Parsing'
LONG_DESCRIPTION = 'A package that supports plaintext and object extraction from Wikipedia HTML dumps.'

# Dev dependencies
EXTRAS_REQUIRE = {
    "tests": ["pytest>=6.2.5"],
}

EXTRAS_REQUIRE["dev"] = (
    EXTRAS_REQUIRE["tests"]
)

# Setting up
setup(
    name="mwparserfromhtml",
    version=VERSION,
    author="Appledora & Isaac Johnson & Martin Gerlach",
    author_email="<isaac@wikimedia.org>",
    url="https://gitlab.wikimedia.org/repos/research/html-dumps",
    license="MIT License",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=['beautifulsoup4', 'requests'],
    keywords=['python', 'wikipedia', 'html'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",

    ],
    extras_require=EXTRAS_REQUIRE,
    include_package_data=True,
    zip_safe=False,
)