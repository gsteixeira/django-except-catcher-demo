# except-catcher-demo

Demo project for [django-except-catcher](https://github.com/gsteixeira/django-except-catcher).


## Instalation

Bare metal

```shell
    virtualenv --python=python3 env/
    source env/bin/activate

    git clone https://github.com/gsteixeira/django-except-catcher-demo
    cd django-except-catcher-demo/demo/

    pip install -r requirements.txt
    python manage.py migrate

    python manage.py createsuperuser --username admin --email admin@example.com

    python manage.py runserver
```
Or with docker:

```shell
    git clone https://github.com/gsteixeira/django-except-catcher-demo
    cd django-except-catcher-demo/
    docker build --tag except-catcher-demo .
    docker run -p 8000:8000 -it except-catcher-demo
```

Or with docker compose:

```shell
    git clone https://github.com/gsteixeira/django-except-catcher-demo
    cd django-except-catcher-demo/
    docker-compose up
```

Now go to url, and login as superuser:

    http://localhost:8000/

If your using docker, the demo credentials are:
username: **admin**
password: **demo**


Click in _Throw an error_, go back, now click in _See errors_.

