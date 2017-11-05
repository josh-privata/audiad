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
# # todo Finish docstring

from django.core.urlresolvers import reverse
from django_webtest import WebTest
from model_mommy import mommy
from .models import Album, Artist, Song, Genre, Label, Country, Style


class GenreTest(WebTest):
    def test_factory_create(self):
        """
        Test that we can create an instance via our object factory.
        """
        instance = mommy.make(Genre)
        self.assertTrue(isinstance(instance, Genre))

    def test_list_view(self):
        """
        Test that the list view returns at least our factory created instance.
        """
        instance = mommy.make(Genre)
        response = self.app.get(reverse('importer:list'))
        object_list = response.context['object_list']
        self.assertIn(instance, object_list)

    def test_create_view(self):
        """
        Test that we can create an instance via the create view.
        """
        response = self.app.get(reverse('importer:create'))
        new_name = 'A freshly created thing'

        # check that we don't already have a model with this name
        self.assertFalse(Genre.objects.filter(name=new_name).exists())

        form = response.forms['importer_form']
        form['name'] = new_name
        form.submit().follow()

        instance = Genre.objects.get(name=new_name)
        self.assertEqual(instance.name, new_name)

    def test_detail_view(self):
        """
        Test that we can view an instance via the detail view.
        """
        instance = mommy.make(Genre)
        response = self.app.get(instance.get_absolute_url())
        self.assertEqual(response.context['object'], instance)

    def test_update_view(self):
        """
        Test that we can update an instance via the update view.
        """
        instance = mommy.make(Genre)
        response = self.app.get(reverse('importer:update', kwargs={'pk': instance.pk, }))

        form = response.forms['importer_form']
        new_name = 'Some new thing'
        form['name'] = new_name
        form.submit().follow()

        instance = Genre.objects.get(pk=instance.pk)
        self.assertEqual(instance.name, new_name)

    def test_delete_view(self):
        """
        Test that we can delete an instance via the delete view.
        """
        instance = mommy.make(Genre)
        pk = instance.pk
        response = self.app.get(reverse('importer:delete', kwargs={'pk': pk, }))
        response = response.form.submit().follow()
        self.assertFalse(Genre.objects.filter(pk=pk).exists())


class LabelTest(WebTest):
    def test_factory_create(self):
        """
        Test that we can create an instance via our object factory.
        """
        instance = mommy.make(Label)
        self.assertTrue(isinstance(instance, Label))

    def test_list_view(self):
        """
        Test that the list view returns at least our factory created instance.
        """
        instance = mommy.make(Label)
        response = self.app.get(reverse('importer:list'))
        object_list = response.context['object_list']
        self.assertIn(instance, object_list)

    def test_create_view(self):
        """
        Test that we can create an instance via the create view.
        """
        response = self.app.get(reverse('importer:create'))
        new_name = 'A freshly created thing'

        # check that we don't already have a model with this name
        self.assertFalse(Label.objects.filter(name=new_name).exists())

        form = response.forms['importer_form']
        form['name'] = new_name
        form.submit().follow()

        instance = Label.objects.get(name=new_name)
        self.assertEqual(instance.name, new_name)

    def test_detail_view(self):
        """
        Test that we can view an instance via the detail view.
        """
        instance = mommy.make(Label)
        response = self.app.get(instance.get_absolute_url())
        self.assertEqual(response.context['object'], instance)

    def test_update_view(self):
        """
        Test that we can update an instance via the update view.
        """
        instance = mommy.make(Label)
        response = self.app.get(reverse('importer:update', kwargs={'pk': instance.pk, }))

        form = response.forms['importer_form']
        new_name = 'Some new thing'
        form['name'] = new_name
        form.submit().follow()

        instance = Label.objects.get(pk=instance.pk)
        self.assertEqual(instance.name, new_name)

    def test_delete_view(self):
        """
        Test that we can delete an instance via the delete view.
        """
        instance = mommy.make(Label)
        pk = instance.pk
        response = self.app.get(reverse('importer:delete', kwargs={'pk': pk, }))
        response = response.form.submit().follow()
        self.assertFalse(Label.objects.filter(pk=pk).exists())


class CountryTest(WebTest):
    def test_factory_create(self):
        """
        Test that we can create an instance via our object factory.
        """
        instance = mommy.make(Country)
        self.assertTrue(isinstance(instance, Country))

    def test_list_view(self):
        """
        Test that the list view returns at least our factory created instance.
        """
        instance = mommy.make(Country)
        response = self.app.get(reverse('importer:list'))
        object_list = response.context['object_list']
        self.assertIn(instance, object_list)

    def test_create_view(self):
        """
        Test that we can create an instance via the create view.
        """
        response = self.app.get(reverse('importer:create'))
        new_name = 'A freshly created thing'

        # check that we don't already have a model with this name
        self.assertFalse(Country.objects.filter(name=new_name).exists())

        form = response.forms['importer_form']
        form['name'] = new_name
        form.submit().follow()

        instance = Country.objects.get(name=new_name)
        self.assertEqual(instance.name, new_name)

    def test_detail_view(self):
        """
        Test that we can view an instance via the detail view.
        """
        instance = mommy.make(Country)
        response = self.app.get(instance.get_absolute_url())
        self.assertEqual(response.context['object'], instance)

    def test_update_view(self):
        """
        Test that we can update an instance via the update view.
        """
        instance = mommy.make(Country)
        response = self.app.get(reverse('importer:update', kwargs={'pk': instance.pk, }))

        form = response.forms['importer_form']
        new_name = 'Some new thing'
        form['name'] = new_name
        form.submit().follow()

        instance = Country.objects.get(pk=instance.pk)
        self.assertEqual(instance.name, new_name)

    def test_delete_view(self):
        """
        Test that we can delete an instance via the delete view.
        """
        instance = mommy.make(Country)
        pk = instance.pk
        response = self.app.get(reverse('importer:delete', kwargs={'pk': pk, }))
        response = response.form.submit().follow()
        self.assertFalse(Country.objects.filter(pk=pk).exists())


class StyleTest(WebTest):
    def test_factory_create(self):
        """
        Test that we can create an instance via our object factory.
        """
        instance = mommy.make(Style)
        self.assertTrue(isinstance(instance, Style))

    def test_list_view(self):
        """
        Test that the list view returns at least our factory created instance.
        """
        instance = mommy.make(Style)
        response = self.app.get(reverse('importer:list'))
        object_list = response.context['object_list']
        self.assertIn(instance, object_list)

    def test_create_view(self):
        """
        Test that we can create an instance via the create view.
        """
        response = self.app.get(reverse('importer:create'))
        new_name = 'A freshly created thing'

        # check that we don't already have a model with this name
        self.assertFalse(Style.objects.filter(name=new_name).exists())

        form = response.forms['importer_form']
        form['name'] = new_name
        form.submit().follow()

        instance = Style.objects.get(name=new_name)
        self.assertEqual(instance.name, new_name)

    def test_detail_view(self):
        """
        Test that we can view an instance via the detail view.
        """
        instance = mommy.make(Style)
        response = self.app.get(instance.get_absolute_url())
        self.assertEqual(response.context['object'], instance)

    def test_update_view(self):
        """
        Test that we can update an instance via the update view.
        """
        instance = mommy.make(Style)
        response = self.app.get(reverse('importer:update', kwargs={'pk': instance.pk, }))

        form = response.forms['importer_form']
        new_name = 'Some new thing'
        form['name'] = new_name
        form.submit().follow()

        instance = Style.objects.get(pk=instance.pk)
        self.assertEqual(instance.name, new_name)

    def test_delete_view(self):
        """
        Test that we can delete an instance via the delete view.
        """
        instance = mommy.make(Style)
        pk = instance.pk
        response = self.app.get(reverse('importer:delete', kwargs={'pk': pk, }))
        response = response.form.submit().follow()
        self.assertFalse(Style.objects.filter(pk=pk).exists())


class SongTest(WebTest):
    def test_factory_create(self):
        """
        Test that we can create an instance via our object factory.
        """
        instance = mommy.make(Song)
        self.assertTrue(isinstance(instance, Song))

    def test_list_view(self):
        """
        Test that the list view returns at least our factory created instance.
        """
        instance = mommy.make(Song)
        response = self.app.get(reverse('importer:list'))
        object_list = response.context['object_list']
        self.assertIn(instance, object_list)

    def test_create_view(self):
        """
        Test that we can create an instance via the create view.
        """
        response = self.app.get(reverse('importer:create'))
        new_name = 'A freshly created thing'

        # check that we don't already have a model with this name
        self.assertFalse(Song.objects.filter(name=new_name).exists())

        form = response.forms['importer_form']
        form['name'] = new_name
        form.submit().follow()

        instance = Song.objects.get(name=new_name)
        self.assertEqual(instance.name, new_name)

    def test_detail_view(self):
        """
        Test that we can view an instance via the detail view.
        """
        instance = mommy.make(Song)
        response = self.app.get(instance.get_absolute_url())
        self.assertEqual(response.context['object'], instance)

    def test_update_view(self):
        """
        Test that we can update an instance via the update view.
        """
        instance = mommy.make(Song)
        response = self.app.get(reverse('importer:update', kwargs={'pk': instance.pk, }))

        form = response.forms['importer_form']
        new_name = 'Some new thing'
        form['name'] = new_name
        form.submit().follow()

        instance = Song.objects.get(pk=instance.pk)
        self.assertEqual(instance.name, new_name)

    def test_delete_view(self):
        """
        Test that we can delete an instance via the delete view.
        """
        instance = mommy.make(Song)
        pk = instance.pk
        response = self.app.get(reverse('importer:delete', kwargs={'pk': pk, }))
        response = response.form.submit().follow()
        self.assertFalse(Song.objects.filter(pk=pk).exists())


class AlbumTest(WebTest):
    def test_factory_create(self):
        """
        Test that we can create an instance via our object factory.
        """
        instance = mommy.make(Album)
        self.assertTrue(isinstance(instance, Album))

    def test_list_view(self):
        """
        Test that the list view returns at least our factory created instance.
        """
        instance = mommy.make(Album)
        response = self.app.get(reverse('importer:list'))
        object_list = response.context['object_list']
        self.assertIn(instance, object_list)

    def test_create_view(self):
        """
        Test that we can create an instance via the create view.
        """
        response = self.app.get(reverse('importer:create'))
        new_name = 'A freshly created thing'

        # check that we don't already have a model with this name
        self.assertFalse(Album.objects.filter(name=new_name).exists())

        form = response.forms['importer_form']
        form['name'] = new_name
        form.submit().follow()

        instance = Album.objects.get(name=new_name)
        self.assertEqual(instance.name, new_name)

    def test_detail_view(self):
        """
        Test that we can view an instance via the detail view.
        """
        instance = mommy.make(Album)
        response = self.app.get(instance.get_absolute_url())
        self.assertEqual(response.context['object'], instance)

    def test_update_view(self):
        """
        Test that we can update an instance via the update view.
        """
        instance = mommy.make(Album)
        response = self.app.get(reverse('importer:update', kwargs={'pk': instance.pk, }))

        form = response.forms['importer_form']
        new_name = 'Some new thing'
        form['name'] = new_name
        form.submit().follow()

        instance = Album.objects.get(pk=instance.pk)
        self.assertEqual(instance.name, new_name)

    def test_delete_view(self):
        """
        Test that we can delete an instance via the delete view.
        """
        instance = mommy.make(Album)
        pk = instance.pk
        response = self.app.get(reverse('importer:delete', kwargs={'pk': pk, }))
        response = response.form.submit().follow()
        self.assertFalse(Album.objects.filter(pk=pk).exists())


class ArtistTest(WebTest):
    def test_factory_create(self):
        """
        Test that we can create an instance via our object factory.
        """
        instance = mommy.make(Artist)
        self.assertTrue(isinstance(instance, Artist))

    def test_list_view(self):
        """
        Test that the list view returns at least our factory created instance.
        """
        instance = mommy.make(Artist)
        response = self.app.get(reverse('importer:list'))
        object_list = response.context['object_list']
        self.assertIn(instance, object_list)

    def test_create_view(self):
        """
        Test that we can create an instance via the create view.
        """
        response = self.app.get(reverse('importer:create'))
        new_name = 'A freshly created thing'

        # check that we don't already have a model with this name
        self.assertFalse(Artist.objects.filter(name=new_name).exists())

        form = response.forms['importer_form']
        form['name'] = new_name
        form.submit().follow()

        instance = Artist.objects.get(name=new_name)
        self.assertEqual(instance.name, new_name)

    def test_detail_view(self):
        """
        Test that we can view an instance via the detail view.
        """
        instance = mommy.make(Artist)
        response = self.app.get(instance.get_absolute_url())
        self.assertEqual(response.context['object'], instance)

    def test_update_view(self):
        """
        Test that we can update an instance via the update view.
        """
        instance = mommy.make(Artist)
        response = self.app.get(reverse('importer:update', kwargs={'pk': instance.pk, }))

        form = response.forms['importer_form']
        new_name = 'Some new thing'
        form['name'] = new_name
        form.submit().follow()

        instance = Artist.objects.get(pk=instance.pk)
        self.assertEqual(instance.name, new_name)

    def test_delete_view(self):
        """
        Test that we can delete an instance via the delete view.
        """
        instance = mommy.make(Artist)
        pk = instance.pk
        response = self.app.get(reverse('importer:delete', kwargs={'pk': pk, }))
        response = response.form.submit().follow()
        self.assertFalse(Artist.objects.filter(pk=pk).exists())

