from django.shortcuts import render, redirect, get_object_or_404

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


def login(request):
    return render(request, 'SocialMedia/login.html')