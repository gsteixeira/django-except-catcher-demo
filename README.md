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

Now go to url, and login as superuser:

    http://localhost:8000/

Click in _Throw an error_, go back, now click in _See errors_.
