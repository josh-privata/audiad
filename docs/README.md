<h1 align="center">
  <a href="https://www.mysql.com/"><img src="https://www.djangoproject.com/m/img/logos/django-logo-positive.png" alt="Django" width="150"></a>
  <a href="https://www.w3.org/"><img src="https://cloud.githubusercontent.com/assets/5771200/19331463/4e5ee6ac-9128-11e6-8a09-4d5426d9ba95.jpg" alt="HTML5-CSS3" width="100"></a>
  <br>
  <br>
  Audiad
  <br>
  <br>
</h1>
<h4 align="center">Music management the easy way</h4>

<p align="center">
  <a href=""><img src="https://img.shields.io/travis/feross/standard/master.svg" alt="Passing"></a>
  <a href="https://secure.php.net/"><img src="https://img.shields.io/badge/PHP-7.0-brightgreen.svg" alt="PHP 7.0"></a>
  <a href="https://www.w3.org/"><img src="https://img.shields.io/badge/HTML-5-brightgreen.svg" alt="HTML 5.0"></a>
  <a href="https://opensource.org/licenses/BSD-2-Clause"><img src="https://img.shields.io/badge/License-BSD-blue.svg" alt="BSD License"></a>
</p>
<br>

## Table of Contents
- [Synopsis](#synopsis)
- [Install](#install)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [License](#license)

## Synopsis

**[Click here to view app website](https://www.audiad.com)**

### Docs

### Static
#### Images
#### js
#### Themes


### Templates

#### Accounts
forms.html

signup.html

#### Admin
index.html

base_site.html

#### Base
base.html

form_template.html

base_visitor.html

#### Music

##### Album
albums.html

bootstrap-responsive.html

album_list.html

album_table.html

album_create.html

album_delete.html

album_detail_bak.html

album_filter.html

album_update.html

album_detail.html

##### Artist
artist_update.html

bootstrap-responsive.html

artist_create.html

artist_delete.html

artist_detail.html

artist_table.html

artist_list.html

artist_filter.html

artists.html

artist_edit.html

##### Auth
profile.html

register.html

login.html

##### Base
album_2col.html

genre_1col.html

genre_2col.html

song_1col.html

artist_base.html

album_base.html

song_2col.html

song_base.html

label_base.html

artist_1col.html

genre_base.html

artist_2col.html

label_1col.html

label_2col.html

album_1col.html

##### Genre
genres.html

genre_update.html

genre_table.html

bootstrap-responsive.html

genre_detail.html

genre_list.html

genre_create.html

genre_delete.html

genre_filter.html

##### Label
label_create.html

label_filter.html

labels.html

label_table.html

label_update.html

label_list.html

bootstrap-responsive.html

label_delete.html

label_detail.html

##### Search
searchresults.html

album_search.html

album_text.txt

##### Song
song_list.html

song_detail.html

songs.html

songs_table.html

bootstrap-responsive.html

song_delete.html

song_create.html

song_update.html

song_filter.html

#### Search
album_search.html

search.html

album_text.txt

### Conf


### Audiad
#### Settings
#### Urls
#### Filter_Mixin
#### Wsgi


### Accounts
#### Signals
#### Command
#### Admin
#### Tables
#### Tests
#### Forms
#### Filters
#### Managers
#### Models
#### Views
#### Urls


### Music
#### Signals
#### Command
#### Admin
#### Tables
#### Tests
#### Forms
#### Filters
#### Managers
#### Models
#### Views
album.py

song.py

views.py

__init__.py

artist.py

genre.py

label.py

#### Urls


### Importer
#### Signals
#### Command
#### Admin
#### Tables
#### Tests
#### Forms
#### Filters
#### Managers
#### Models
#### Views
#### Urls


### NEWAPP
#### Signals
#### Command
#### Admin
#### Tables
#### Tests
#### Forms
#### Filters
#### Managers
#### Models
#### Views
#### Urls


## Install
First, make a directory to install the files to and change to that directory using :

```bash
 mkdir audiad && cd audiad
```

Then all you need to do is clone the project from github into the directory by using :

```bash
 git clone https://github.com/josh-privata/Audiad.git
```

## Usage

**Note:**  [Python 3](https://python.org) is required to run the project.

**Note:**  [Django 1.11](https://www.djangoproject.com/) or newer is required to run the project.

**Note:**  [MySQL](https://www.mysql.com/downloads/) or [MariaDB](https://mariadb.org/download/) are required to use an external database.



Initially the application needs to be copied to your root html folder. Assuming you are still in the gppatients folder
you can do this by running the command :

```bash
$ mkdir /var/www/html/gppatients && cp -r * /var/www/html/gppatients/
```

After you have copied the files across you will need to configure your webserver.


**Assuming you have hosted the application locally, you can access the program by visiting**

**[http://localhost/gppatients/](http://localhost:8080)**

**The login details are:**

|Username  |Password  |
|----------|----------|
|  josh    | password |


## Screenshots


## License
[BSD](LICENSE) Copyright (c) 2017 [Josh Cannons](http://joshcannons.com).