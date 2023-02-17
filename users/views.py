from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages

from django.contrib.auth.models import User
from django.views.generic.edit import CreateView


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользовать {username} был успешно создан! можешь проверить на почте)')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(
        request,
        'users/registrations.html',
        {
            'title': 'Страница регистрации',
            'form': form
        }
    )

class BaseRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = '/'