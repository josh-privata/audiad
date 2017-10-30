"""docstrings.


Example:


Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

Todo:

"""
# todo Finish docstring

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.db.models import Q
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView, ListView
from haystack.generic_views import SearchView
from music.filters import AlbumFilter, ArtistFilter, SongFilter
from music.forms import UserForm, AlbumSearchForm
from music.tables import *
from website.filter_mixin import ListFilteredMixin

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
"""int: Module level variable documented inline."""
# todo Finish docstring

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
"""int: Module level variable documented inline."""
# todo Finish docstring

class IndexView(TemplateView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring
    template_name = 'music/index.html'

    def dispatch(self, request, *args, **kwargs):
        """docstring

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            param1: The first parameter.
            param2: The second parameter.

        Returns:
            True if successful, False otherwise.

        """
        # todo Finish docstring
        if not request.user.is_authenticated():
            return render(request, 'music/auth/login.html')
        else:
            return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['artists_count'] = Artist.objects.all().count()
        context['songs_count'] = Song.objects.all().count()
        context['albums_count'] = Album.objects.filter(user=self.request.user).count()
        context['user_albums'] = Album.objects.filter(user=self.request.user, fav=True)
        context['user_artists'] = Artist.objects.filter(fav=True)
        context['user_songs'] = Song.objects.filter(fav=True)
        # context['urls'] = (
        #             (reverse('tutorial'), 'Tutorial'),
        #             (reverse('multiple'), 'Multiple tables'),
        #             (reverse('filtertableview'), 'Filtered tables'),
        #             (reverse('singletableview'), 'Using SingleTableMixin'),
        #             (reverse('multitableview'), 'Using MultiTableMixin'),
        #             (reverse('bootstrap'), 'Using the bootstrap template'),
        #             (reverse('semantic'), 'Using the Semantic UI template'),
        #         )
        return context


class MySearchView(SearchView):
    """docstring

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    # todo Finish docstring
    model = Album

    def get_queryset(self):
        """str: Properties should be documented in their getter method."""
        # todo Finish docstring
        return super(MySearchView, self).get_queryset().order_by('title')
        # further filter queryset based on some set of criteria

    def get_context_data(self, *args, **kwargs):
        """str: Properties should be documented in their getter method."""
        # todo Finish docstring
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        return context


def search(request):
    """docstring

            Note:
                Do not include the `self` parameter in the ``Args`` section.

            Args:
                param1: The first parameter.
                param2: The second parameter.

            Returns:
                True if successful, False otherwise.

            """
    # todo Finish docstring
    form = AlbumSearchForm(request.GET)
    album = form.search()
    return render_to_response('search/album_search.html', {'album': album})


def searchresults(request):
    """docstring

            Note:
                Do not include the `self` parameter in the ``Args`` section.

            Args:
                param1: The first parameter.
                param2: The second parameter.

            Returns:
                True if successful, False otherwise.

            """
    # todo Finish docstring
    query = request.GET.get("q")
    albums = Album.objects.all().filter(Q(title__icontains=query))
    artists = Artist.objects.all().filter(Q(name__icontains=query))
    songs = Song.objects.all().filter(Q(title__icontains=query))
    genres = Genre.objects.all().filter(Q(name__icontains=query))
    labels = Label.objects.all().filter(Q(name__icontains=query))
    return render(request, 'music/search/searchresults.html', {
        'artists': artists,
        'albums': albums,
        'songs': songs,
        'labels': labels,
        'genres': genres,
    })


def logout_user(request):
    """docstring

            Note:
                Do not include the `self` parameter in the ``Args`` section.

            Args:
                param1: The first parameter.
                param2: The second parameter.

            Returns:
                True if successful, False otherwise.

            """
    # todo Finish docstring
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music/auth/login.html', context)


def login_user(request):
    """docstring

            Note:
                Do not include the `self` parameter in the ``Args`` section.

            Args:
                param1: The first parameter.
                param2: The second parameter.

            Returns:
                True if successful, False otherwise.

            """
    # todo Finish docstring
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
            else:
                return render(request, 'music/auth/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/auth/login.html', {'error_message': 'Invalid login'})
    else:
        albums = Album.objects.filter(user=request.user)
        return render(request, 'music/index.html', {'albums': albums})


def filter_album(request):
    """str: Properties should be documented in their getter method."""
    # todo Finish docstring
    f = AlbumFilter(request.GET, queryset=Album.objects.all())
    return render(request, 'music/album/album_filter.html', {'filter': f})


def filter_song(request):
    """str: Properties should be documented in their getter method."""
    # todo Finish docstring
    f = SongFilter(request.GET, queryset=Song.objects.all())
    return render(request, 'music/song/song_filter.html', {'filter': f})


def filter_artist(request):
    """str: Properties should be documented in their getter method."""
    # todo Finish docstring
    f = ArtistFilter(request.GET, queryset=Artist.objects.all())
    return render(request, 'music/artist/artist_filter.html', {'filter': f})


def register(request):
    """docstring

            Note:
                Do not include the `self` parameter in the ``Args`` section.

            Args:
                param1: The first parameter.
                param2: The second parameter.

            Returns:
                True if successful, False otherwise.

            """
    # todo Finish docstring
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'music/auth/register.html', context)

# class ClassBased(SingleTableView):
#     table_class = ThemedCountryTable
#     queryset = Country.objects.all()
#     template_name = 'class_based.html'
#
#
# # note that this is not really the way to go because the queryset is not re
# # -evaluated after the first time the dry herb vape
# view is requested.
# qs = Person.objects.all()
#
#
# class MultipleTables(MultiTableMixin, TemplateView):
#     template_name = 'multiTable.html'
#     tables = [
#         PersonTable(qs),
#         PersonTable(qs, exclude=('country', ))
#     ]
#
#     table_pagination = {
#         'per_page': 10
#     }
#
#
# def tutorial(request):
#     return render(request, 'tutorial.html', {'people': Person.objects.all()})
#
#
# class FilteredPersonListView(FilterView, ExportMixin, SingleTableView):
#     table_class = PersonTable
#     model = Person
#     template_name = 'bootstrap_template.html'
#
#     filterset_class = PersonFilter
#
# def index(request):
#     create_fake_data()
#     table = PersonTable(Person.objects.all())
#     RequestConfig(request, paginate={
#         'per_page': 5
#     }).configure(table)
#
#     return render(request, 'index.html', {
#         'table': table,
#         'urls': (
#             (reverse('tutorial'), 'Tutorial'),
#             (reverse('multiple'), 'Multiple tables'),
#             (reverse('filtertableview'), 'Filtered tables'),
#             (reverse('singletableview'), 'Using SingleTableMixin'),
#             (reverse('multitableview'), 'Using MultiTableMixin'),
#             (reverse('bootstrap'), 'Using the bootstrap template'),
#             (reverse('semantic'), 'Using the Semantic UI template'),
#         )
#     })

# def multiple(request):
#     qs = Country.objects.all()
#
#     example1 = CountryTable(qs, prefix='1-')
#     RequestConfig(request, paginate=False).configure(example1)
#
#     example2 = CountryTable(qs, prefix='2-')
#     RequestConfig(request, paginate={'per_page': 2}).configure(example2)
#
#     example3 = ThemedCountryTable(qs, prefix='3-')
#     RequestConfig(request, paginate={'per_page': 3}).configure(example3)
#
#     example4 = ThemedCountryTable(qs, prefix='4-')
#     RequestConfig(request, paginate={'per_page': 3}).configure(example4)
#
#     example5 = ThemedCountryTable(qs, prefix='5-')
#     example5.template = 'extended_table.html'
#     RequestConfig(request, paginate={'per_page': 3}).configure(example5)
#
#     return render(request, 'multiple.html', {
#         'example1': example1,
#         'example2': example2,
#         'example3': example3,
#         'example4': example4,
#         'example5': example5,
#     })

#
# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })
