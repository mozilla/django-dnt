==========
Django-DNT
==========

Do Not Track offers an easy way to pay attention to the ``DNT`` HTTP header. If
users are sending ``DNT: 1``, ``DoNotTrackMiddleware`` will set ``request.DNT =
True``, else it will set ``request.DNT = False``.

Just add ``dnt.middleware.DoNotTrackMiddleware`` to your ``MIDDLEWARE_CLASSES``
and you're good to go.
