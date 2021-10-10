FROM debian:latest

RUN apt-get update && \
    apt-get install -y python3 python3-virtualenv git

RUN virtualenv --python=python3 /var/env/ && \
    . /var/env/bin/activate && \
    cd /opt/ && \
    git clone https://github.com/gsteixeira/django-except-catcher-demo && \
    cd django-except-catcher-demo/demo/ && \
    pip install -r requirements.txt && \
    python manage.py migrate && \
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'example@example.com', 'demo')" | python manage.py shell

RUN echo "#!/bin/bash \n \
. /var/env/bin/activate\n \
cd /opt/django-except-catcher-demo/demo/\n \
python manage.py runserver 0:8000" > /etc/entrypoint.sh

RUN chmod +x /etc/entrypoint.sh

CMD ["/etc/entrypoint.sh"]
