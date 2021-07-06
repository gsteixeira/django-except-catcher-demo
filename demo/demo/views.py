
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    html = """
    <ul>
        <li>
            <a href="/text-exception/">There is a Bug!!</a>
        </li>
        <li>
            <a href="/errors/">See errors</a>
        </li>
        <li>
            <a href="/admin/">Django admin</a>
        </li>
    </ul>
    """
    return HttpResponse(html)
