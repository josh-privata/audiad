<h1 align="center">
  <a href="https://www.mysql.com/"><img src="https://cloud.githubusercontent.com/assets/5771200/19331499/73b6d90a-9128-11e6-925e-c5ff1eaf5d2e.jpg" alt="PHP and MySQL" height="150"></a>
  <a href="https://www.w3.org/"><img src="https://cloud.githubusercontent.com/assets/5771200/19331463/4e5ee6ac-9128-11e6-8a09-4d5426d9ba95.jpg" alt="HTML5-CSS3" height="150"></a>
  <br>
  <br>
  GP Patients
  <br>
  <br>
</h1>
<h4 align="center">A simple php website to manage patients at a General Practice</h4>

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


**[Click here to view a demo of this website](https://www.joshcannons.com/gp/home.php)**


## Install
First, make a directory to install the files to and change to that directory using :

```bash
 mkdir gppatients && cd gppatients
```

Then all you need to do is clone the project from github into the directory by using :

```bash
 git clone https://github.com/josh-privata/GPPatients.git
```

## Usage

**Note:**  [Nginx](https://nginx.org/en/) or [Apache](https://httpd.apache.org/download.cgi) are required to run the preceding commands.

**Note:**  [MySQL](https://www.mysql.com/downloads/) or [MariaDB](https://mariadb.org/download/) are required to run the preceding commands.

**Note:**  [PHP](http://php.net/downloads.php) is required to run the preceding commands.

This appliction requires a running LAMP or LEMP stack.


For intructions on how to configure a LAMP stack look [here](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu) or for a LEMP stack look [here.](https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-in-ubuntu-16-04)

Initially the application needs to be copied to your root html folder. Assuming you are still in the gppatients folder
you can do this by running the command :

```bash
$ mkdir /var/www/html/gppatients && cp -r * /var/www/html/gppatients/
```

After you have copied the files across you will need to configure your webserver.

For intructions on how to configure virtual hosts on apache look [here](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-ubuntu-14-04-lts) or for server blocks on nginx look [here.](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)


**Assuming you have hosted the application locally, you can access the program by visiting**

**[http://localhost/gppatients/](http://localhost/gppatients/)**

**The login details are:**

|Username  |Password  |
|----------|----------|
| michael  |password  |
|  jane    |password  |


## Screenshots


## License
[BSD](LICENSE) Copyright (c) 2016 [Josh Cannons](http://joshcannons.com).