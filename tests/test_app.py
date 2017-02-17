# -*- coding: utf-8 -*-
"""Test an application using django-dnt."""
from __future__ import unicode_literals

from django.test import TestCase


class AppTest(TestCase):
    """Test middleware through the Django test client."""

    def test_request_dnt(self):
        """Test a request with header "DNT: 1"."""
        response = self.client.get('/', HTTP_DNT='1')
        self.assertEqual(response['Vary'], 'DNT')
        content = response.content.decode('utf8')
        self.assertInHTML('<code class="dnt">True</code>', content)

    def test_request_no_dnt(self):
        """Test a request with no DNT header."""
        response = self.client.get('/')
        self.assertEqual(response['Vary'], 'DNT')
        content = response.content.decode('utf8')
        self.assertInHTML('<code class="dnt">False</code>', content)
