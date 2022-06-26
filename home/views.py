from django.shortcuts import render



def templates(request):
    return render(request, "home/index.html", {})


