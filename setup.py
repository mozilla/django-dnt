#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Packaging setup for django-dnt."""

from setuptools import setup

description = 'Make Django requests aware of the DNT header'


def read_file(path):
    contents = open(path).read()
    if hasattr(contents, 'decode'):
        return contents.decode('utf8')  # Python2 bytes to unicode
    else:
        return contents  # Python3 reads unicode


def long_description():
    """Create a PyPI long description from docs."""
    readme = read_file('README.rst')
    body_tag = ".. Omit badges from docs"
    try:
        readme_body_start = readme.index(body_tag)
    except ValueError:
        readme_body = readme
    else:
        # Omit the badges and reconstruct the title
        readme_text = readme[readme_body_start + len(body_tag) + 1:]
        readme_body = """\
%(title_mark)s
%(title)s
%(title_mark)s
%(readme_text)s
""" % {
            'title_mark': '=' * len(description),
            'title': description,
            'readme_text': readme_text,
        }

    try:
        history = read_file('HISTORY.rst')
    except IOError:
        history = ''

    long_description = """\
%(readme)s

%(history)s
""" % {
        'readme': readme_body,
        'history': history
    }
    return long_description


setup(
    name='django-dnt',
    version='1.0',
    description=description + '.',
    long_description=long_description(),
    author='James Socol',
    author_email='james@mozilla.com',
    maintainer='John Whitlock',
    maintainer_email='jwhitlock@mozilla.com',
    url='http://github.com/mozilla/django-dnt',
    license='BSD',
    packages=['dnt'],
    zip_safe=False,
    keywords='django-dnt dnt do not track',
    classifiers=[
        'Development Status :: 6 - Mature',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: Mozilla',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
