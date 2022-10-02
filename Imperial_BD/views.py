from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
import json

from .models import *

# Create your views here.
import Imperial_BD.views


@login_required
def home(request):
    if request.method == 'POST':
        name = request.POST.get('db_search')
        if name == '':
            return render(request, 'home.html', {'title': 'CIA'})
        else:
            f = open('first_names.json', encoding='utf-8')
            data = json.load(f)
            user_ids = []
            for i in data:
                for c in data[i]:
                    if c.find(name.lower()) != -1:
                        if not (i in user_ids):
                            user_ids.append(i)

            object_user = []
            for user_id in user_ids:
                object_user.append(Users.objects.get(id=user_id))
            return render(request, 'home.html', {'title': 'CIA', 'list_user': object_user})
    else:
        return render(request, 'home.html', {'title': 'CIA'})


@login_required
def dossier(request, user_id):
    object_user = Users.objects.filter(id=user_id)
    if len(object_user) > 0:
        return render(request, 'dossier.html', {'title': 'CIA', 'user': object_user})
    else:
        raise Http404()


@login_required
def code(request):
    return render(request, 'error_404.html', {'title': 'CIA'})


@login_required
def pageNotFound(request, exception):
    return render(request, 'error_404.html')

