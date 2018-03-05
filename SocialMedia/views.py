from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

from .models import WizzerUser, Whiz
from .forms import WhizForm


def index(request):

    if request.method == "POST":
        form = WhizForm(request.POST)
        if form.is_valid():
            new_whiz = Whiz(whiz_poster=WizzerUser.objects.all()[0], content=request.POST['whiz_input'])
            new_whiz.save()
            return redirect('index')
    else:
        form = WhizForm()

    user = WizzerUser.objects.all()[0]
    whizzes = Whiz.objects.all()[::-1]
    context = {'WizzerUser': user, 'Whizzes': whizzes, 'WhizForm': form}
    return render(request, 'SocialMedia/WizzerFeed.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'SocialMedia/register.html', context)