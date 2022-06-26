from django.shortcuts import render



def template(request):
    return render(request, "publico/index.html", {})


