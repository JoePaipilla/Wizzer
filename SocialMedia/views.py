from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View
from django.contrib.auth.models import User as UserObject
from django.db import IntegrityError

from .models import WizzerUser, Whiz
from .forms import WhizForm, RegistrationForm, LoginForm, ReplyForm


# quick view to return the view name as an html response
def default(name):
    return HttpResponse('<h1>This is the {} view.</h1>'.format(name))


def index(request):
    user = request.user
    if request.method == "POST":
        print(request.POST)
        form = WhizForm(request.POST)
        if form.is_valid():
            # change the bottom 'whiz_poster' to the request.user object
            new_whiz = Whiz(whiz_poster=user.wizzeruser, content=request.POST['whiz_input'])
            new_whiz.save()
        elif 'delete' in request.POST:
            Whiz.objects.get(id=request.POST['delete']).delete()
        elif 'reply' in request.POST:
            pass
        elif 'like' in request.POST:
            whiz = Whiz.objects.get(id=request.POST['like'])
            liked_user = UserObject.objects.get(username__exact=user).wizzeruser
            if liked_user not in whiz.likes.all():
                whiz.likes.add(liked_user)
            else:
                whiz.likes.remove(liked_user)
        elif 'dislike' in request.POST:
            whiz = Whiz.objects.get(id=request.POST['dislike'])
            disliked_user = UserObject.objects.get(username__exact=user).wizzeruser
            if disliked_user not in whiz.dislikes.all():
                whiz.dislikes.add(disliked_user)
            else:
                whiz.dislikes.remove(disliked_user)
        elif 'report' in request.POST:
            pass
        elif 'follow' in request.POST:
            self_user = UserObject.objects.get(username__exact=user).wizzeruser
            followed_user = UserObject.objects.get(username__exact=request.POST['follow']).wizzeruser
            if self_user in followed_user.followers.all():
                followed_user.followers.remove(self_user)
                self_user.following.remove(followed_user)
            else:
                followed_user.followers.add(self_user)
                followed_user.save()
                self_user.following.add(followed_user)
                self_user.save()
        return redirect('index')
    else:
        form = WhizForm()

    if str(user) == 'AnonymousUser':
        return redirect('login')
    else:
        whizzes = Whiz.objects.all()[::-1]
        context = {'WizzerUser': user,
                   'Whizzes': whizzes,
                   'WhizForm': form
                   }
        return render(request, 'SocialMedia/WizzerFeed.html', context)


class LoginView(View):
    form_class = LoginForm
    template_name = 'SocialMedia/login.html'

    def get(self, request):
        try:
            current_user = UserObject.objects.get(username__exact=request.user)
            if current_user.is_authenticated:
                return redirect('index')
        except:
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('login')


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
                    # request.user.username etc...
        return render(request, self.template_name, {'form': form})


def follows(request):
    return default(follows.__name__)


def profile_page(request, username):
    user = request.user
    whiz_form = WhizForm(None)
    reply_form = ReplyForm(None)
    profile_user = get_object_or_404(UserObject.objects, username__exact=username)
    profile_user_whizzes = UserObject.objects.get(username__exact=username).wizzeruser.whiz_set.all()[::-1]
    context = {
        'ProfileUser': profile_user,
        'ProfileUserWhizzes': profile_user_whizzes,
        'MainUser': user,
        'WhizForm': whiz_form,
        'ReplyForm': reply_form
    }
    return render(request, 'SocialMedia/profile_page.html', context)


def notifications(request):
    return default(notifications.__name__)


def direct_messages(request):
    return default(direct_messages.__name__)


def gallery(request):
    return default(gallery.__name__)


def settings(request):
    return default(settings.__name__)


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
