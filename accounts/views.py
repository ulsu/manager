from forms import *
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms.util import ErrorList

def login(request):
    go_next = request.GET['next'] if 'next' in request.GET else '/'

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(go_next)
            else:
                errors = form._errors.setdefault('username', ErrorList())
                errors.append(u'Username or password incorrect')

            return render(request, 'accounts/login.html', {
                    'form': form,
                    'next': go_next,
                })
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')

        form = LoginForm()

    return render(request, 'accounts/login.html', {
            'form': form,
            'next': go_next,
        })

def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
    return HttpResponseRedirect('/')