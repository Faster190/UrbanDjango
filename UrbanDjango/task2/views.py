from django.shortcuts import render

# Create your views here.


def display_class(request):
    return render(request, "class_template.html")


def display_func(request):
    return render(request, "func_template.html")
