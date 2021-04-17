from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'Generate Hashed Stringd Easily.'
LONG_DESCRIPTION = 'A package that allows to generate Hashed Strings in the easiest way.'

# Setting up
setup(
    name="gp-hashing",
    version=VERSION,
    author="Shouvik Bajpayee & Sayak Mukhopadhyay",
    author_email="<bajpayeeshouvik@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'hashing', 'gp-hashing', 'generate hash', 'easy hashing'],
    classifiers=[
        "Development Status :: 1 - First Stable Release",
        "Intended Audience :: Python Programmers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)