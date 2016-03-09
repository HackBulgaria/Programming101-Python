from django.shortcuts import render, redirect
from .models import User
from django.core.urlresolvers import reverse, reverse_lazy

from .decorators import login_required


def register(request):
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        if not User.exists(email):
            user = User(email=email, password=password)
            user.save()
        else:
            error = 'User already exists'

    return render(request, 'register.html', locals())


def login(request):
    session_email = request.session.get('email', False)

    if session_email:
        return redirect(reverse('profile'))

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        u = User.login(email, password)

        if u is None:
            error = 'Wrong username/password'
        else:
            request.session['email'] = email
            return redirect(reverse('profile'))

    return render(request, 'login.html', locals())


@login_required(redirect_url=reverse_lazy('login'))
def home(request):
    if request.method == 'POST':
        if request.POST.get('delete_session', False):
            session_key = request.POST.get('session_key')
            if session_key in request.session:
                del request.session[session_key]
        else:
            session_key = request.POST.get('session_key')
            session_value = request.POST.get('session_value')

            request.session[session_key] = session_value

    return render(request, 'index.html', locals())


def logout(request):
    request.session.flush()

    return redirect(reverse('login'))
