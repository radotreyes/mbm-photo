from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from test_app.models import Topic, Webpage, AccessRecord, UserProfile
from . import forms

# Create your views here.
def index( request ):
    webpages_list = AccessRecord.objects.order_by( 'date' )
    date_ord = { 'access_records': webpages_list }
    return render( request, 'test_app/index.html', context = date_ord )

def portrait( request ):
    return render( request, 'test_app/portrait/index.html' )

def landscape( request ):
    return render( request, 'test_app/landscape/index.html' )

def contact( request ):
    form = forms.UserProfileForm()

    if request.method == 'POST':
        form = forms.UserProfileForm( request.POST )

        if form.is_valid():
            print( 'UPLOADED' )
            return HttpResponseRedirect( '/' )
        else:
            print( "ERR: Form invalid!" )

    return render( request, 'test_app/contact/index.html', { 'form': form } )

def users( request ):
    form = forms.UserAuthForm()
    loggedin = False

    if request.method == 'POST':
        form = forms.UserAuthForm( request.POST )

        if form.is_valid():
            user = form.save() # save form data to user
            user.set_password( user.password ) # set user password
            user.save() # register the user
            loggedin = True
            return HttpResponseRedirect( '/' )
        else:
            print( "ERR: Form invalid!" )

    return render( request, 'test_app/users/index.html', { 'form': form } )

def upload( request ):
    form = forms.UserProfileForm()

    if request.method == 'POST':
        form = forms.UserProfileForm( request.POST )

        if form.is_valid():
            print( 'UPLOADED' )
            return HttpResponseRedirect( '/' )
        else:
            print( "ERR: Form invalid!" )

    return render( request, 'test_app/upload/index.html', { 'form': form } )

def user_login( request ):
    if request.method == 'POST':
        username = request.POST.get( 'username' )
        password = request.POST.get( 'password' )

        user = authenticate( username = username, password = password )

        if user:
            if user.is_active():
                login( request, user )
                return HttpResponseRedirect( reverse( 'index' ) )

            else:
                return HttpResponse( 'Account not active.' )

        else:
            print( 'Failed login:' )
            print( 'Username: {}\nPassword: {}'.format( username, password ) )
            return HttpResponse( 'Invalid account info.' )
