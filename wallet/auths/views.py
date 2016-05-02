from django.shortcuts import render
from .forms import LoginForm


def index(request):
    return render(request, 'auths/index.html', {'form': LoginForm()})
