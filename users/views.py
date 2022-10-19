from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def login_views(request):
    if request.method =='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print('인증성공')
            login(request, user)
            return redirect('users:index')
        else:
            print('인증실패')

    return render(request, 'login.html')

def logout_views(request):
    logout(request)
    return redirect('users:index')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('users:index')

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form' : form})
