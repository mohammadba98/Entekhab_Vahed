from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
# Create your views here.

from django.contrib.auth.forms import UserCreationForm




def index(request):
    # return HttpResponse('sdaglsdgnksd')

    return render(request , 'index.html')




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def contact_is_value(request):
    render(request, 'contact_is_value.html')


def contact_us_form(request):
    if request.method == 'POST':
        s = request.POST
        if 10 < len(s['text']) < 250:
            return render(request , 'contact_is_value.html')
    return render(request, 'contact_us.html')
