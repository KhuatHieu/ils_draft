from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="books.index"),
    path("/create", views.create, name="book.create"),
    path("<int:book_id>", views.details, name="book.edit"),
    path("<book_id>/save", views.save, name="book.save")
]
