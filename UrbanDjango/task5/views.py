from django.shortcuts import render
from django.http import HttpResponse
from task5.forms import ContactForm

# Create your views here.

def registration(request):
    users = {"Антон": ["12345678", 18],
             "Дима": ["87654321", 81],
             "Albert": ["11223344", 35],
             "Joe": ["11221122", 53]
             }
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")
        if password != repeat_password:
            context["error"] = "Пароли не совпадают"
        if int(age) < 18:
            context["error"] = "Вы должны быть старше 18"
        if username in users:
            context["error"] = "Пользователь уже существует"
        if not context:
            return HttpResponse(f"Приветствуем, {username}!")
    return render(request, "fifth_task/registration_page.html", context)


def django_sign_up(request):
    users = {"Антон": ["12345678", 18],
             "Дима": ["87654321", 81],
             "Albert": ["11223344", 35],
             "Joe": ["11221122", 53]
             }
    context = {}
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]
            if password != repeat_password:
                context["error"] = "Пароли не совпадают"
            if int(age) < 18:
                context["error"] = "Вы должны быть старше 18"
            if username in users:
                context["error"] = "Пользователь уже существует"
            if not context:
                return HttpResponse(f"Приветствуем, {username}!")
    return render(request, "fifth_task/registration_page.html", context)
