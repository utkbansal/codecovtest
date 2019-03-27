from django.urls import reverse
import unittest
from django.test import Client


class SimpleTest(unittest.TestCase):
    def test_http_200(self):
        c = Client()
        response = c.get(reverse('first'))
        assert response.status_code == 200
