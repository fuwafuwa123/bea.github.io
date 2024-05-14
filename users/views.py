from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import login, authenticate # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore

def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)

# Create your views here.
