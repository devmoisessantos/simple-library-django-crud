from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Book


class SignupForm(UserCreationForm):
    email = forms.EmailField(
        label='', widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'E-mail',
            }
        )
    )

    first_name = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'First Name',
            }
        )
    )

    last_name = forms.CharField(
        label='', max_length=100, widget=forms.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Last Name',
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '''
            <ul class="form-text text-muted">
                <li><b>*</b>Obrigatório: 150 caracteres ou menos.</li>
                <li><b>*</b>Obrigatório: Letras, dígitos e @/./+/-/_ apenas.</li>
            </ul>
        '''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '''
            <ul class="form-text text-muted">
                <li><b>*</b>Senha deve ser única.</li>
                <li><b>*</b>Senha deve conter 8 caracteres ou mais.</li>
                <li><b>*</b>Senha não pode ser totalmente numérica.</li>
                <li><b>*</b>Ultilize ao menos um caractere especial.</li>
            </ul>
        '''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '''
            <span class="form-text text-muted">
                <small>Digite a mesma senha inserida acima.</small>
            </span>
        '''

        self.fields['email'].widget.attrs[
            'placeholder'] = 'Digite seu e-mail válido (ex: nome@dominio.com)'

# def save(self, commit=True):
#     user = super(SignupForm, self).save(commit=False)
#     user.email = self.cleaned_data['email']
#     if commit:
#         user.save()
#     return user

# def clean_email(self):
#     email = self.cleaned_data['email']
#     if User.objects.filter(email=email).exists():
#         raise forms.ValidationError('Este email já está em uso.')
#     return email

# def clean_password2(self):
#     password1 = self.cleaned_data.get('password1')
#     password2 = self.cleaned_data.get('password2')
#     if password1 and password2 and password1 != password2:
#         raise forms.ValidationError('As senhas não coincidem.')
#     return password2

# def clean_username(self):
#     username = self.cleaned_data['username']
#     if User.objects.filter(username=username).exists():
#         raise forms.ValidationError('Este nome de usuário já está em uso.')
#     return username


class AddBookForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        label='Titulo',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Titulo do Livro'
            }))

    description = forms.CharField(
        label='Descrição',
        max_length=255,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Descrição'
            }))

    year = forms.IntegerField(
        label='Ano',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control'
            }))

    genre = forms.CharField(
        label='Genero', max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }))

    value = forms.FloatField(
        label='Valor',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control'
            }))

    class Meta:
        model = Book
        fields = ('title', 'description', 'year', 'genre', 'value')
