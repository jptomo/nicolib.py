# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.rst') as fp:
    long_description = fp.read()


setup(
    name='nicolib',
    version=__import__('nicolib').__version__,
    packages=find_packages(),
    author='Tomohiro NAKAMURA',
    author_email='quickness.net@gmail.com',
    description='The aim to provide a connection with Niconico API.',
    long_description=long_description,
    license=u'The MIT License',
    keywords='NiconicoAPI Niconico API ニコニコ動画API ニコニコ動画',
    url='https://github.com/jptomo/nicolib.py',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
    ],

)
