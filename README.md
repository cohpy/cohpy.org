# COhPy.org website

In order to develop locally, please set a ```SECRET_KEY``` and ```BROWSER``` in your .bash_profile (If ```BROWSER='HEADLESS'```, then the functional tests will run with PhantomJS, otherwise they default to Firefox:

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
python manage.py dumpdata meetups python_resources info_blocks --indent 2 > fixtures/testdata.json
```

### References:

pytest-django documentation - https://pytest-django.readthedocs.org/en/latest/index.html

pytest-cov - https://pypi.python.org/pypi/pytest-cov

Testing tutorial - https://realpython.com/blog/python/testing-in-django-part-1-best-practices-and-examples/