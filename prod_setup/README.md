## System Preparation

This document assumes Ubuntu 14.04 LTS base

### Install needed packages

First, install the applications that the site relies on. Specifically, PostgreSQL, and Nginx. 

```
# aptitude install postgresql-server-dev-all postgresql-client postgresql nginx
```

Then, install the python software, git, and stuff to build our requirements with pip

```
# aptitude install git python3-pip python3-dev python-dev virtualenvwrapper build-essential
```

Finally, install uwsgi via pip3. We need to pip3 install uwsgi to get version 2.

```
# pip3 install uwsgi
```

### Prepare user (web is presumed, but it doesn't matter as long as you are consistent)
```
# adduser web
# usermod -G sudo web
```

### Add user to Postgres
```
# su - postgres
# createuser web
# createdb -O web cohpy
```

### As user "web", setup:

Set up your ssh keys, to use as a deployment key

```
# ssh-keygen
```

Take .ssh/id_rsa.pub and make a deployment key, then set up git config:

```
# git config --global user.email "{your email}"
# git config --global user.name "{your name}"
# git config --global push.default simple
```

Clone the repo or fork:

```
# mkdir ~/dev
# cd ~/dev
# git clone (the base repo or your fork, make sure deployment keys are setup)
```

Create the virtual Python environment:

```
# echo "export WORKON_HOME=~/Env" >> ~/.bashrc
# source ~/.bashrc
# mkvirtualenv --python=/usr/bin/python3 cohpy
# pip install -r {root of this repo}/requirements.txt
```

Set up the environment file by copying env_template in this directory to the root github directory of cohpy.org, and:

```
# cp env_template {root of this repo}/.env
# vi .env (or the editor of your choice)
```

Edit the .env file and uncomment the SECRET_KEY line and change the key to whatever you would like.

Build the database and the static folders.

```
# cd cohpy (within this repo)
# python manage.py migrate --settings=config.settings.production
# python manage.py collectstatic --settings=config.settings.production
```

You'll need to populate the database with some data. One easy was is just to load the test fixtures, but you can populate however you wish.

```
# python manage.py loaddata {root of this repo}/cohpy/fixtures/testdata.json --settings=config.settings.production
```

### As root, setup:

Setup nginx config.

```
# cp {this directory}/nginx/cohpy /etc/nginx/sites-available/
# ln -s /etc/nginx/sites-available/cohpy /etc/nginx/sites-enabled/
# rm /etc/nginx/sites-enabled/default
```

Setup uwgsi config.

```
# mkdir -p /etc/uwsgi/sites
# cp {this directory}/uwsgi/cohpy.ini /etc/uwsgi/sites
# cp {this directory}/uwsgi/uwsgi.conf /etc/init/
```

Restart uwsgi and nginx to get things working.

```
# service uwsgi restart
# service nginx restart
```

