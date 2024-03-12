from django.http import HttpResponse
from django.template import loader

from books.models import Book


# Create your views here.
def index(request):
    dashboard = loader.get_template("dashboard.html")

    booksCount = Book.objects.count()

    return HttpResponse(dashboard.render({"booksCount": booksCount}, request))
