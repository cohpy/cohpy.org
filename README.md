!(https://travis-ci.org/cohpy/cohpy.org.svg?branch=master)

# COhPy.org website

In order to develop locally, please set a SECRET_KEY in your .bash_profile:

```
SECRET_KEY='your secret key'
export SECRET_KEY
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

### References:

pytest-django documentation - https://pytest-django.readthedocs.org/en/latest/index.html

pytest-cov - https://pypi.python.org/pypi/pytest-cov

Testing tutorial - https://realpython.com/blog/python/testing-in-django-part-1-best-practices-and-examples/
