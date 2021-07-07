# except-catcher-demo

Demo django project for [django-except-catcher](https://github.com/gsteixeira/django-except-catcher)


Instalation

```
    virtualenv --python=python3 env/
    source env/bin/activate

    pip install -r requirements.txt

    python manage.py migrate

    python manage.py createsuperuser --username admin --email admin@example.com

    python manage.py runserver
```

Login as superuser, now go to url:

    http://localhost:8000/errors/

You can now throw an exception in the url:

    http://localhost:8000/test-exception/
