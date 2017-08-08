from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.db.models import Q
from django.shortcuts import render

from music.forms import GenreForm, UserForm
from music.tables import *

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def create_genre(request):
    form = GenreForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        genre = form.save(commit=False)
        genre.save()
        all_albums = Album.objects.all()
        return render(request, 'music/index.html', {'all_albums': all_albums})
    context = {
        "form": form,
    }
    return render(request, 'music/genre/create_genre.html', context)


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'music/auth/login.html')
    else:
        user_songs = Song.objects.filter(fav=True)
        user_artists = Artist.objects.filter(fav=True)
        user_albums = Album.objects.filter(user=request.user, fav=True)
        albums_count = Album.objects.filter(user=request.user).count()
        artists_count = Artist.objects.all().count()
        songs_count = Song.objects.all().count()
        return render(request, 'music/index.html', {'artists_count': artists_count,
                                                    'user_albums': user_albums,
                                                    'user_songs': user_songs,
                                                    "user_artists": user_artists,
                                                    'songs_count': songs_count,
                                                    'albums_count': albums_count})


def searchresults(request):
    albums = Album.objects.all()
    artists = Artist.objects.all()
    songss = Song.objects.all()
    query = request.GET.get("q")
    albums = albums.filter(Q(title__icontains=query))
    songss = songss.filter(Q(title__icontains=query))
    artists = artists.filter(Q(name__icontains=query))
    return render(request, 'music/search/searchresults.html', {
        'artists': artists,
        'albums': albums,
        'songs': songss,
    })


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music/auth/login.html', context)


def login_user(request):
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
    return render(request, 'music/auth/login.html')


def register(request):
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
