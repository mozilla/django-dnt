# -*- coding: utf-8 -*-
"""Middleware tests."""
from __future__ import unicode_literals

from django.test import TestCase
from django.http import HttpRequest, HttpResponse

from dnt.middleware import DoNotTrackMiddleware


class DoNotTrackMiddlewareTest(TestCase):
    """Unit tests for the DoNotTrackMiddleware."""

    def request(self):
        """Create a request object for middleware testing."""
        req = HttpRequest()
        req.META = {
            'SERVER_NAME': 'testserver',
            'SERVER_PORT': 80,
        }
        req.path = req.path_info = "/"
        return req

    def response(self):
        """Create a response object for middleware testing."""
        resp = HttpResponse()
        resp.status_code = 200
        resp.content = b'    '
        return resp

    def test_request_dnt(self):
        """The header "DNT: 1" sets request.DNT."""
        request = self.request()
        request.META['HTTP_DNT'] = '1'
        DoNotTrackMiddleware().process_request(request)
        self.assertTrue(request.DNT)

    def test_request_dnt_off(self):
        """The header "DNT: 0" clears request.DNT."""
        request = self.request()
        request.META['HTTP_DNT'] = '0'
        DoNotTrackMiddleware().process_request(request)
        self.assertFalse(request.DNT)

    def test_request_no_dnt(self):
        """If the DNT header is not present, request.DNT is false."""
        request = self.request()
        DoNotTrackMiddleware().process_request(request)
        self.assertFalse(request.DNT)

    def test_response(self):
        """The Vary caching header in the response includes DNT."""
        request = self.request()
        response = self.response()
        response = DoNotTrackMiddleware().process_response(request, response)
        self.assertEqual(response['Vary'], 'DNT')
