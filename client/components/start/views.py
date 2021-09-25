from django.http import HttpResponse


def home_page(request):
    return HttpResponse("<html><title>Bulls and Cows</title></html>")
