from distutils.log import Log
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from filesharing.forms import SignupForm, FileUploadForm
from django.contrib.auth import logout
from django.contrib import messages
from files.models import File
from django.contrib.auth.models import User


def home(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FileUploadForm()
    online_users = User.objects.filter(is_active=True)
    files = File.objects.all().order_by('-uploaded_at')
    context = {'form': form, 'files': files, 'online_users': online_users}
    return render(request, 'auth/home.html', context)

def loggout(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    context = {'form': form}
    return render(request, 'auth/signup.html', context)

def searchFiles(request):
    query = request.GET.get('q')
    files = File.objects.filter(title__icontains=query) | File.objects.filter(uploaded_at__icontains=query)
    online_users = User.objects.filter(is_active=True)
    context = {
        'files': files,
        'online_users' : online_users
    }
    return render(request, 'auth/home.html', context)


