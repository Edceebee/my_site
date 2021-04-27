from django.test import TestCase

from django.test import SimpleTestCase


class Tests(TestCase):

    def test_questionaire_page_status_code(self):  # failing test
        response = self.client.get('/questionaire/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
