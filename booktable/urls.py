from django.urls import path
from . import views


app_name='booktable'

urlpatterns = [
    path('book/',views.Book_A_Table, name='book-table'),
]
