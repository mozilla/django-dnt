==========
Django-DNT
==========

.. image:: http://img.shields.io/travis/mozilla/django-dnt/master.svg
    :alt: The status of Travis continuous integration tests
    :target: https://travis-ci.org/mozilla/django-dnt

.. image:: https://img.shields.io/codecov/c/github/mozilla/django-dnt.svg
    :target: https://codecov.io/gh/mozilla/django-dnt
    :alt: The code coverage

.. image:: https://img.shields.io/pypi/v/django-dnt.svg
    :alt: The PyPI package
    :target: https://pypi.python.org/pypi/django-dnt

.. Omit badges from docs

Do Not Track offers an easy way to pay attention to the ``DNT`` HTTP header. If
users are sending ``DNT: 1``, ``DoNotTrackMiddleware`` will set ``request.DNT =
True``, else it will set ``request.DNT = False``.

Just add ``dnt.middleware.DoNotTrackMiddleware`` to your ``MIDDLEWARE_CLASSES``
(Django 1.9 and earlier) or ``MIDDLEWARE`` (Django 1.10 and later) and you're
good to go.
