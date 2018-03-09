from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View

from .models import WizzerUser, Whiz
from .forms import WhizForm, RegistrationForm, LoginForm

from django.contrib.auth.models import User as UserObject


def index(request):

    if request.method == "POST":
        form = WhizForm(request.POST)
        if form.is_valid():
            new_whiz = Whiz(whiz_poster=WizzerUser.objects.all()[0], content=request.POST['whiz_input'])
            new_whiz.save()
            return redirect('index')
    else:
        form = WhizForm()

    user = request.user
    whizzes = Whiz.objects.all()[::-1]
    context = {'WizzerUser': user, 'Whizzes': whizzes, 'WhizForm': form}
    return render(request, 'SocialMedia/WizzerFeed.html', context)

class LoginView(View):
    form_class = LoginForm
    template_name = 'SocialMedia/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("DIDN'T WORK")

class RegistrationView(View):
    form_class = RegistrationForm
    template_name = 'SocialMedia/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():

            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('testing')
                    #request.user.username etc...
        return render(request, self.template_name, {'form':form})

def testing(request):
    return render(request, 'SocialMedia/test.html', {'User': request.user})

"""def register(request):
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
    return render(request, 'SocialMedia/register.html', context)"""
