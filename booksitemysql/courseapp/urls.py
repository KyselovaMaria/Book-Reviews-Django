from django.urls import path
from . import views
from courseapp.views import upload_book

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('all_books', views.all_books, name = 'all_books'),
    path('genre/<str:slug>', views.category_detail, name = 'category_detail'),
    path('pdf/<str:slug>', views.book_detail, name = 'book_detail'),
    path('searched_books', views.search_book, name = 'book_search'),
    path('register', views.register_page, name = 'register'),
    path('login', views.login_page, name = 'login'),
    path('logout', views.logout_user, name = 'logout'),
    path('upload-book/', upload_book, name='upload_book'),
    path('book/<int:book_id>/rate/', views.rate_book, name='rate_book'),
    path('book/<int:book_id>/add-to-favorite/', views.add_to_favorite, name='add_to_favorite'),
    path('book/<int:book_id>/remove-from-favorite/', views.remove_from_favorite, name='remove_from_favorite'),
    path('mylist/', views.my_favorite_books, name='my_favorite_books'),
]
