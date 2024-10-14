from django.shortcuts import render

# Create your views here.


def platform(request):
    return render(request, "fourth_task/platform.html")


def games(request):
    name_1 = "TES 5: Skyrim"
    name_2 = "TES 5: Skyrim Legendary Edition"
    name_3 = "TES 5: Skyrim Special Edition"
    name_4 = "TES 5: Skyrim Anniversary Edition"
    context = {
        "game_names": [name_1, name_2, name_3, name_4]
    }
    return render(request, "fourth_task/games.html", context)


def cart(request):
    return render(request, "fourth_task/cart.html")
