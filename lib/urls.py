from django.urls import path
from django.http import HttpResponse
from lib.views import (book_detail, index, add_book, update_book,
                       logout_user, register_user,
                       login_user, books, delete_book)


urlpatterns = [
    path('', index, name='index'),                       # Rota inicial
    path('login/', login_user, name='login'),            # Rota de login
    path('logout/', logout_user, name='logout'),         # Rota de logout
    path('register/', register_user, name='register'),   # Rota de cadastro

    # Rota para a lista de livros
    path('books/', books, name='books'),
    # Rota para adicionar um livro
    path('add_book/', add_book, name='add_book'),
    # Rota para editar um livro
    path('update_book/<int:id>/', update_book, name='update_book'),
    # Rota para detalhes de um livro
    path('books/<int:id>/', book_detail, name='books_detail'),
    # Rota para deletar um livro
    path('delete_book/<int:id>/', delete_book, name='delete_book'),
]
