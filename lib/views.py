from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from lib.models import Book
from .forms import SignupForm, AddBookForm


def index(request):
    return render(request, 'index.html')


def login_user(request):
    if \
            request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['senha']
        # Autenticação
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if \
                user is not None:
            login(request, user)
            messages.success(
                request,
                "Login realizado com sucesso!"
            )
            print("Autenticação realizada com sucesso!")
            return redirect('index')
        else:
            messages.error(
                request, "ERRO: Autenticação falhou. Tente novamente!")
            print("ERRO: Autenticação falhou. Tente novamente!")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(
        request,
        "Logout realizado com sucesso!"
    )
    print("Logout realizado com sucesso!")
    return redirect('index')


def register_user(request):
    if \
            request.method == 'POST':
        form = SignupForm(request.POST)
        if \
                form.is_valid():
            # Salva o usuário
            user = form.save()
            # Autenticação automática após o cadastro
            username = form.cleaned_data['username']
            # Ajuste para usar o campo correto
            password = form.cleaned_data['password1']
            user = authenticate(
                request,
                username=username,
                password=password
            )
            if \
                    user is not None:
                login(request, user)
                messages.success(
                    request,
                    "Cadastro realizado com sucesso!"
                )
                return redirect('login')
        else:
            messages.error(
                request,
                "Erro no cadastro. Verifique os dados informados."
            )
    else:
        # Formulário vazio para requisições GET
        form = SignupForm()
        return render(
            request,
            'register.html',
            {'form': form})

    # Renderiza o template com o formulário
    return render(
        request,
        'register.html',
        {'form': form})


def books(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('senha')
        # Autenticação
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)  # Loga o usuário
            books = Book.objects.all()  # Obtém todos os livros
            return render(
                request,
                'books.html',
                {'books': books}
            )
        else:
            # Mensagem de erro para falha na autenticação
            messages.error(request, "Usuário ou senha inválidos.")
            return render(request, 'login.html')
    else:
        if request.user.is_authenticated:
            books = Book.objects.all()
            return render(
                request,
                'books.html',
                {'books': books}
            )
        else:
            messages.error(
                request,
                "ERRO: Usuário não autenticado. Tente novamente!"
            )
            return render(request, 'login.html')


def add_book(request):
    form = AddBookForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    "Livro adicionado com sucesso!"
                )
                return redirect('index')
        return render(
            request,
            'add_book.html',
            {'form': form}
        )
    else:
        messages.error(
            request,
            "ERRO: Usuário não autenticado. Tente novamente!"
        )
        return render(
            request,
            'index.html'
        )


@login_required
def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    form = AddBookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        messages.success(
            request,
            "Livro editado com sucesso!"
        )
        return redirect('books')
    else:
        if request.method == 'POST':
            messages.error(
                request,
                "ERRO: Houve um erro ao editar o livro. Verifique os dados informados!"
            )
    return render(
        request,
        'update_book.html',
        {'form': form}
    )


def book_detail(request, id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=id)
        return render(
            request,
            'book_detail.html',
            {'book': book}
        )
    else:
        messages.error(
            request,
            "ERRO: Usuário não autenticado. Tente novamente!"
        )
        return redirect('login')


def delete_book(request, id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=id)
        book.delete()
        messages.success(
            request,
            "Livro deletado com sucesso!"
        )
        return redirect('books')
    else:
        messages.error(
            request,
            "ERRO: Usuário não autenticado. Tente novamente!"
        )
        return redirect('index')
