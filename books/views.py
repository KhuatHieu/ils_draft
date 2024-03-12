from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods

from books.models import Book, BookForm
from core.consts import ITEMS_PER_PAGE


# Create your views here.
def index(request):
    s = request.GET.get("s", "")
    page = request.GET.get("page", 1)

    books = Book.objects.filter(Q(name__icontains=s) | Q(content__icontains=s))
    paginator = Paginator(books, ITEMS_PER_PAGE)

    return render(request, "books.html", {
        "page": page,
        "total_pages": paginator.num_pages,
        "items": paginator.page(page),
        "items_count": books.count()
    })


def create(request):
    return render(request, "book_details.html", {
        "book": Book
    })


def details(request, book_id):
    return render(request, "book_details.html", {
        "book": get_object_or_404(Book, id=book_id)
    })


@require_http_methods("POST")
def save(request, book_id):
    book = get_object_or_404(Book, id=book_id) if book_id is not None else Book()
    book_form = BookForm(request.POST, instance=book)

    if book_form.is_valid():
        book_form.save()

    return redirect('books.index')

