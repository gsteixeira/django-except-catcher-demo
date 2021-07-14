
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required
def home(request):
    html = """
    <ul>
        <li>
            <a href="{}">Throw an error!!</a>
        </li>
        <li>
            <a href="{}">See errors</a>
        </li>
        <li>
            <a href="/admin/">Django admin</a>
        </li>
    </ul>
    """.format(reverse('except_catcher:test_exception'),
               reverse('except_catcher:list_reports'))
    return HttpResponse(html)
