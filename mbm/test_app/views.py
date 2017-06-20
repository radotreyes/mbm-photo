from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from test_app.models import Topic, Webpage, AccessRecord, User
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
    form = forms.FormNameEmailMsg()

    if request.method == 'POST':
        form = forms.FormNameEmailMsg( request.POST )

        if form.is_valid():
            form.save( commit = True )
            return HttpResponseRedirect( '/' )
        else:
            print( "ERR: Form invalid!" )

    return render( request, 'test_app/contact/index.html', { 'form': form } )

def users( request ):
    users_list = User.objects.order_by( 'lname' )
    lname_ord = { 'users_lname': users_list }
    return render( request, 'test_app/users/index.html', context = lname_ord )
