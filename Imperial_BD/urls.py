from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('code/', code, name='code'),
    path('grandmaster/', grandmaster, name='grandmaster'),
    path('fynnfu/', fynnfu, name='fynnfu'),
    path('dossier/<int:user_id>', dossier, name='dossier'),
    path('chat/', chat, name='chat'),
    path('login-stellar/', login, name='login'),
    path('register-stellar/', register, name='register'),
    path('update-stellar/', update, name='update'),
    path('create-directive-stellar/', create_directive, name='create_directive'),
    path('all-directive-stellar/', all_directive, name='all_directive'),
    path('mark-as-read-stellar/', mark_as_read, name='mark_as_read'),
    path('get-directive-stellar/', get_directive, name='get_directive'),
    path('check-stellar/', check, name='check'),
    path('set-check-stellar/', set_check, name='set_check'),
    path('get-check-stellar/', get_check, name='get_check')
]

