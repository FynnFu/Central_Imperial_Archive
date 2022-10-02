from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('code/', code, name='code'),
    path('dossier/<int:user_id>', dossier, name='dossier')
]

