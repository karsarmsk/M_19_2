from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import UserRegister
from .models import *
from django.core.paginator import Paginator

# buyers = Buyer.objects.all()  # Получаем всех покупателей из базы данных
# users = ['Sergey', 'Kola', 'Sasha']

def sign_up_by_django(request):

    # uname = Buyer.objects.name
    Buyers = Buyer.objects.all()  # Получаем всех покупателей из базы данных
    info = {}
    form = UserRegister()

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in Buyers:
                info['error'] = 'Пользователь уже существует'


            else:
                # Проверяем, существует ли пользователь с таким именем
                user_exists = False
                for buyer in Buyers:
                    if buyer.name == username:
                        user_exists = True
                        break

                if user_exists:
                    info['error'] = 'Пользователь уже существует'
                else:
                    # Создаем нового покупателя
                    Buyer.objects.create(name=username, balance=0, age=age)
                    return HttpResponse(f'Приветствую, {username}!')

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)



def menu(request):
    return render(request, 'fifth_task/menu.html')
def platform(request):
    return render(request, 'fifth_task/platform.html')
def games(request):
    Games = Game.objects.all()

    context = {
        'Games': Games,
    }
    # games = Games.object.all()
    return render(request, 'fifth_task/games.html',context)
def cart(request):
    return render(request, 'fifth_task/cart.html')
def menu(request):
    return render(request, 'fifth_task/menu.html')

def sign_up_by_html(request):
    users = ['Sergey', 'Sveta', 'Oleg']
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            return HttpResponse(f'Приветствуем, {username}!')
        print(f"Имя: {username}")
        print(f"Пароль: {password}")
        print(f"Пароль: {repeat_password}")
        print(f"Возраст: {age}")


    return render(request, 'fifth_task/registration_page.html', info)

# Create your views here.
