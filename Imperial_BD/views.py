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


# @login_required
# def home(request):
#     if request.method == 'POST':
#         name = request.POST.get('db_search')
#         if name == '':
#             return render(request, 'home.html', {'title': 'CIA'})
#         else:
#             f = open('first_names.json', encoding='utf-8')
#             data = json.load(f)
#             user_ids = []
#             for i in data:
#                 for c in data[i]:
#                     if c.find(name.lower()) != -1:
#                         if not (i in user_ids):
#                             user_ids.append(i)
#
#             object_user = []
#             for user_id in user_ids:
#                 object_user.append(Users.objects.get(id=user_id))
#             return render(request, 'home.html', {'title': 'CIA', 'list_user': object_user})
#     else:
#         return render(request, 'home.html', {'title': 'CIA'})


@login_required
def home(request):
    if request.method == 'POST':
        name = request.POST.get('db_search')
        if name == '':
            return render(request, 'home.html', {'title': 'CIA'})
        else:
            names = Names.objects.all()
            list_user = []
            for _name in names:
                if _name.name.find(name.lower()) != -1:
                    if not (_name.user in list_user):
                        list_user.append(_name.user)
            if len(list_user) > 0:
                msg = "По вашему запросу найдены следующие страницы:"
            else:
                msg = "Совпадений не найдено. Кибза опять напортачил..."
            return render(request, 'home.html', {'title': 'CIA', 'list_user': list_user, 'msg': msg})
    else:
        return render(request, 'home.html', {'title': 'CIA'})


@login_required()
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


@login_required
def grandmaster(request):
    return render(request, 'dev_mikhail.html', {'title': 'DEV'})

chat_msgs = []
online_users = set()

MAX_MESSAGES_COUNT = 100


@login_required
def chat(request):
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    return render(request, 'dev_mikhail.html', {'title': 'DEV'})


@login_required
def fynnfu(request):
    return render(request, 'dev_rashid.html', {'title': 'DEV'})


def login(request):
    login_str = request.GET.get("login")
    password_str = request.GET.get("password")
    if login_str is None:
        return HttpResponse("https://korki.pythonanywhere.com/login-stellar/?login=LOGIN&password=PASSWORD")
    try:
        user = Person.objects.get(rank=login_str)
    except:
        user = None
    if user is not None:
        if user.password == password_str:
            return HttpResponse('[{'+f'"first_name": "{user.first_name}", "last_name": "{user.last_name}", "rank": "{user.rank}", "level": "{user.level}", "tasks_completed": "{user.tasks_completed}", "level_pyramid": "{user.level_pyramid}"'+'}]')
        else:
            return HttpResponse("Неверный пароль!")
    else:
        return HttpResponse("Пользователь не найден!")


def register(request):
    first_name_str = request.GET.get("first_name")
    last_name_str = request.GET.get("last_name")
    rank_str = request.GET.get("rank")
    password_str = request.GET.get("password")
    try:
        user = Person.objects.get(rank=rank_str)
        return HttpResponse("Пользователь с таким позывным уже существует!")
    except:
        user = Person.objects.create(first_name=first_name_str, last_name=last_name_str, rank=rank_str, password=password_str)
        return HttpResponse("Пользователь создан!")


def update(request):
    rank_str = request.GET.get("rank")
    try:
        user = Person.objects.get(rank=rank_str)
    except:
        return HttpResponse("Пользователь не найден!")
    if user is not None:
        return HttpResponse('[{'+f'"level": "{user.level}", "tasks_completed": "{user.tasks_completed}"'+'}]')


def create_directive(request):
    task_str = request.GET.get("task")
    directive = Directive.objects.create(task=task_str)
    return HttpResponse("Директива успешно создана!")


def all_directive(request):
    rank_str = request.GET.get("rank")
    user = Person.objects.get(rank=rank_str)
    mark_arr = mark2arr(user.read_task)
    directive = Directive.objects.all()
    content = '['
    for directive_one in directive:
        if str(directive_one.id) in mark_arr:
            mark_id = directive_one.id
        else:
            mark_id = f"● {directive_one.id}"
        content += '{' + f'"id": "{mark_id}", "task": "{directive_one.task}"' + '}, '
    content += '{"id": "-1", "task": "end"}]'
    print(mark_arr)
    return HttpResponse(content)


def mark2arr(read_task: str):
    mark_arr = []
    i = 0
    while i < len(read_task):
        if read_task[i] == '|':
            buffer = ""
            i += 1
            while read_task[i] != '|':
                buffer += read_task[i]
                i += 1
                if i >= len(read_task):
                    break
            mark_arr.append(buffer)
    return mark_arr


def mark_as_read(request):
    rank_str = request.GET.get("rank")
    id_dir_str = request.GET.get("id")
    user = Person.objects.get(rank=rank_str)
    user.read_task += f'|{id_dir_str}'
    user.save(update_fields=['read_task'])
    return HttpResponse(f"Changes saved!")


def get_directive(request):
    id_str = request.GET.get("id")
    directive = Directive.objects.get(id=id_str)
    return HttpResponse(directive.task)


def set_check(request):
    rank_str = request.GET.get("rank")
    id_str = request.GET.get("id")
    user = Person.objects.get(rank=rank_str)
    if user.check_task:
        return HttpResponse("Вы не можете выполнять несколько директив одновременно")
    else:
        user.check_task = True
        user.id_task = id_str
        user.save(update_fields=['check_task', 'id_task'])
        return HttpResponse("Выполнение отправлено на рассмотрение")


def check(request):
    users = Person.objects.all()
    content = ''
    for user in users:
        if user.check_task:
            directive = Directive.objects.get(id=user.id_task)
            content += user.first_name + ": " + directive.task
            content += f"; <a href='/get-check-stellar?rank={user.rank}'>Confirm</a>"
            content += "<br>"
    return HttpResponse(content)


def get_check(request):
    rank_str = request.GET.get("rank")
    user = Person.objects.get(rank=rank_str)
    user.check_task = False
    user.id_task = 0
    user.tasks_completed += 1
    user.save(update_fields=['check_task', 'id_task', 'tasks_completed'])
