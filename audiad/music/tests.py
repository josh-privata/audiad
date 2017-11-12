"""docstrings.


Example:

#
# Attributes:
#     module_level_variable1 (int): Module level variables may be documented in
#         either the ``Attributes`` section of the module docstring, or in an
#         inline docstring immediately following the variable.
#
# Todo:
#
# """
# todo Finish docstring


from unittest import TestCase
from django.core.urlresolvers import reverse
from django_webtest import WebTest
from model_mommy import mommy
from audiad.music.models import *
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# from selenium.webdriver.chrome import webdriver as chromedriver
from selenium.webdriver.firefox.options import Options


class GenreSeleniumTest(LiveServerTestCase):

    def setUp(self):
        """ setUp is where you instantiate the selenium webdriver and loads the browser. """
        # User.objects.create_superuser(
        #     username='josh',
        #     password='josh',
        #     email='josh@example.com'
        # )
        options = Options()
        options.add_argument('-headless')
        self.selenium = webdriver.Firefox(firefox_options=options)
        # self.selenium.maximize_window()
        super(GenreSeleniumTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(GenreSeleniumTest, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/music/register/')
        # Find the form element
        username = selenium.find_element_by_name('username')
        email = selenium.find_element_by_name('email')
        password = selenium.find_element_by_name('password')
        submit = selenium.find_elements_by_id('submit')
        # Fill the form with data
        username.send_keys('quaser')
        email.send_keys('q@q.com')
        password.send_keys('123456')
        # Submitting the form
        submit[0].click()
        # Check the returned result
        assert 'Welcome quaser' in selenium.page_source


class GenreWebTest(WebTest, TestCase):
    def test_factory_create(self):
        """
        Test that we can create an instance via our object factory.
        """
        instance = mommy.make(Genre)
        self.assertTrue(isinstance(instance, Genre))

    def test_genre_all(self):
        """
        Test that the main view returns at least our factory created instance.
        """
        responsereverse = self.app.get(reverse('music:genres', kwargs={'filter_by': 'all'}))
        response = self.client.get('/music/view/genres/all/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(responsereverse.status_code, 200)

    def test_list_view(self):
        """
        Test that the list view returns at least our factory created instance.
        """
        response = self.app.get(reverse('music:genre_list'))
        self.assertEqual(response.status_code, 200)
    #
    def test_create_view(self):
        """
        Test that we can create an instance via the create view.
        """
        response = self.app.get(reverse('music:create_genre'))
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        """
        Test that we can view an instance via the detail view.
        """
        instance = mommy.make(Genre)
        response = self.app.get(reverse('music:create_genre'))
        self.assertEqual(response.status_code, 200)

    def test_update_view(self):
        """
        Test that we can update an instance via the update view.
        """
        instance = mommy.make(Genre)
        response = self.app.get(reverse('music:edit_genre', kwargs={'pk': instance.pk, }))
        print(instance.pk)
        self.assertEqual(response.status_code, 200)


    def test_delete_view(self):
        """
        Test that we can delete an instance via the delete view.
        """
        instance = mommy.make(Genre)
        url = '/music/delete/genres/'
        url.join(str(instance.pk))
        # response1 = self.app.get(reverse('music:delete_genre', kwargs={'pk': '1', }))
        print(instance.pk)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response1.status_code, 200)

