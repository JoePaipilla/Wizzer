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


class HomepageView(View):
    form_class = WhizForm
    template_name = 'SocialMedia/WizzerFeed.html'

    def get(self, request):
        user = request.user
        form = self.form_class(None)
        whizzes = Whiz.objects.all()[::-1]
        context = {'WizzerUser': user,
                   'Whizzes': whizzes,
                   'WhizForm': form
                   }

        if user.id is None:
            return redirect('login')
        else:
            return render(request, self.template_name, context)

    def post(self, request):
        user = request.user
        form = self.form_class(request.POST)
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
        elif 'follow' in request.POST:
            self_user = UserObject.objects.get(username__exact=user).wizzeruser
            followed_user = UserObject.objects.get(username__exact=request.POST['follow']).wizzeruser
            if self_user in followed_user.followers.all():
                followed_user.followers.remove(self_user)
                self_user.following.remove(followed_user)
            else:
                followed_user.followers.add(self_user)
                self_user.following.add(followed_user)
        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('login')


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


class FollowsView(View):

    def get(self, request, *args, **kwargs):
        return default(self.__class__.__name__)


class NotificationsView(View):

    def get(self, request, *args, **kwargs):
        return default(self.__class__.__name__)


class DirectMessagesView(View):

    def get(self, request, *args, **kwargs):
        return default(self.__class__.__name__)


class GalleryView(View):

    def get(self, request, *args, **kwargs):
        return default(self.__class__.__name__)


class SettingsView(View):

    def get(self, request, *args, **kwargs):
        return default(self.__class__.__name__)