

# COhPy.org website&nbsp;&nbsp;&nbsp;![](https://travis-ci.org/cohpy/cohpy.org.svg?branch=master)

## Install Linux Packages (apt,rpm etc) for Python development

Even if you have Python installed, there are certain Python development 
packages that may not have been installed by your Linux distro.  To Make 
sure that you have the necessary packages installed, run the following 
command:

`sudo apt-get install python3-dev python3-venv`

## Clone the repository

1. find a directory where you want to clone the cohpy.org repository to.  You'll wind up
creating a cohpy.org and a cohpy.org-venv directory there.
2. cd into that directory
3. run the following command:
`git clone https://github.com/cohpy/cohpy.org.git`

## Setup

We have two methods of setting up the development environment.  
* Method 1 configures Django to use an SQLite database (avoiding the need 
to set up the Postgres database) and will use the develop-linux script to 
automate various development tasks.
* Method 2 is a manual setup process that includes setting up the Postgres 
database and provides a dev environment that better resembles production

### Setup method 1 - develop-linux script


### Setup method 2 - Manual Setup

#### Install & Configure PostgreSQL

**Install PostgreSQL**

`sudo apt-get install postgresql`

**Connect to PostgreSQL and Create a Database User**

`psql` is a command-line client that is included with PostgreSQL.  When 
PostgreSQL is installed a `postgres` user is created that has full access
to PostgreSQL.  To connect to PostgreSQL use the following command:

`sudo -u postgres psql`

Once you're connected, create a user with a command similar the following change, just don't use a password 
that an idiot would use on their luggage.

`CREATE ROLE django_cohpy WITH PASSWORD '12345';

#### Install python-dev libraries 

`sudo apt-get install python3-venv`


In to develop locally, please set a `SECRET_KEY` and ```BROWSER``` 
in your .bash_profile.  `SECRET_KEY` can be any string, but I'd use something 
at least 50 characters long.  If ```BROWSER='HEADLESS'```, then the functional
tests will run with PhantomJS, otherwise they default to Firefox:

```
SECRET_KEY='your secret key'
export SECRET_KEY
BROWSER='FIREFOX'
export BROWSER
```

To run the development server, navigate to the ```cohpy``` directory and run:

```
$ python manage.py runserver
```

To run all tests (from the cohpy directory):

```
$ py.test -v
```

To run only meetup unit tests:

```
$ py.test meetups -v
```

To run only functional tests:

```
$ py.test functional_tests -v
```

Note: Firefox is currently required for the functional tests

To check test coverage, use pytest-cov:

```
$ py.test meetups --cov=meetups --cov-report=html
```

This will produce an html report in the project directory.

Open the report in a browser ```htmlcov/index.html```.

### Test data generation:

To create fixture data to be used in tests:

```
$ python manage.py dumpdata meetups python_resources info_blocks --indent 2 > fixtures/testdata.json
```

### Production setup

To set up the system to run in a production environment, or recreate how it is running in production today,
please follow the instructions and use the files provided in the ```prod_setup``` directory.

### References:

pytest-django documentation - https://pytest-django.readthedocs.org/en/latest/index.html

pytest-cov - https://pypi.python.org/pypi/pytest-cov

Testing tutorial - https://realpython.com/blog/python/testing-in-django-part-1-best-practices-and-examples/
