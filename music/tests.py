from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views.views import *
from .models import *


class PageTests(TestCase):

    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/music')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('music:index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('music:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'music/index.html')

    def test_home_view_status_code(self):
        url = reverse('music:index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/music/')
        self.assertEquals(view.func, IndexView())

class ModelTests(TestCase):
    def setUp(self):
        Album.objects.create(name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)
