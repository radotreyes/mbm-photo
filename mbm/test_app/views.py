from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import RedirectView
from django.utils.decorators import method_decorator
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth import REDIRECT_FIELD_NAME, login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse, reverse_lazy
from . import forms, models

# Create your views here.

'''
MODELS CALLED IN context_processors.py:
    - UserProfile
'''

class Login( FormView ):
    title = 'login'
    template_name = 'test_app/login/index.html'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    success_url = settings.LOGIN_REDIRECT_URL

    def get_context_data( self, **kwargs ):
        title = self.title

        data = super().get_context_data( **kwargs )
        data['title'] = title
        return data

    def form_valid( self, form ):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate( username = username, password = password )

        if user is not None and user.is_active:
            login( self.request, user )
            return super( Login, self ).form_valid( form )
        else:
            return self.form_invalid( form )

class Logout( RedirectView ):
    url = settings.LOGIN_REDIRECT_URL

    @method_decorator( login_required )
    def get( self, request, *args, **kwargs ):
        logout( request )
        return super( Logout, self ).get( request, *args, **kwargs )

class About( TemplateView ):
    title = 'about'
    template_name = 'test_app/about/index.html'

    def get_context_data( self, **kwargs ):
        title = self.title

        data = super().get_context_data( **kwargs )
        data['title'] = title
        return data

# class AboutUpdate( UpdateView ):

class Email( CreateView ):
    title = 'email'
    form_class = forms.EmailForm
    model = models.EmailRequest
    template_name = 'test_app/about/email.html'
    success_url = settings.UPLOAD_SUCCESS_URL

    def get_context_data( self, **kwargs ):
        title = self.title

        data = super().get_context_data( **kwargs )
        data['title'] = title
        return data

    def form_valid( self, form ):
        form.instance.user = self.request.user
        return super( Email, self ).form_valid( form )

    @method_decorator( login_required )
    def dispatch( self, request, *args, **kwargs ):
        return super( Email, self ).dispatch( request, *args, **kwargs )

class Index( ListView ):
    title = 'home'
    template_name = 'test_app/main/index.html'
    model = models.ImageUpload

    def get_context_data( self, **kwargs ):
        title = self.title
        image_objects = self.model.objects.order_by( '-id' ) # all objects in ImageUpload model

        data = super().get_context_data( **kwargs )
        data['title'] = title
        data['images'] = image_objects
        return data

class Gallery( ListView ):
    # to be inherited
    template_name = 'test_app/main/gallery.html'
    model = models.ImageUpload

    # to be overwritten
    title = 'gallery'
    category = None

    def get_context_data( self, **kwargs ):
        title = self.title
        image_objects = self.model.objects.order_by( '-id' ) # all objects in ImageUpload model
        category = self.category

        data = super().get_context_data( **kwargs )
        data['title'] = title
        data['images'] = image_objects
        data['category'] = category
        return data

class ImageCreate( CreateView ):
    title = 'new'
    form_class = forms.ImageUploadForm
    template_name = 'test_app/upload/index.html'
    success_url = settings.UPLOAD_SUCCESS_URL
    # success_message = 'Image uploaded!'

    def get_context_data( self, **kwargs ):
        title = self.title

        data = super().get_context_data( **kwargs )
        data['title'] = title
        return data

    def form_valid( self, form ):
        form.instance.user = self.request.user
        return super( ImageCreate, self ).form_valid( form )

    @method_decorator( login_required )
    def dispatch( self, request, *args, **kwargs ):
        return super( ImageCreate, self ).dispatch( request, *args, **kwargs )

class ImageUpdate( UpdateView ):
    template_name = 'test_app/img/details.html'
    fields = ( 'title', 'category', 'frontpage')
    model = models.ImageUpload

    def get_success_url( self, **kwargs ):
        image = self.model.objects.filter( pk = self.kwargs['pk'] ).values()[0]
        if image['category'] == 'portrait':
            print( 'portrait' )
            return reverse_lazy( 'test_app:portrait' )
        elif image['category'] == 'landscape':
            print( 'landscape' )
            return reverse_lazy( 'test_app:landscape' )
        else:
            print( 'default' )
            return reverse_lazy( 'test_app:index' )

    def get_context_data( self, **kwargs ):
        image = self.model.objects.filter( pk = self.kwargs['pk'] ).values()[0] # retrieve pk from url
        title = image['title']

        data = super().get_context_data( **kwargs )
        data['title'] = title
        data['image'] = image
        data['loggedin'] = self.request.user.is_authenticated
        return data

    def form_valid( self, form ):
        form.instance.user = self.request.user
        return super( ImageUpdate, self ).form_valid( form )

class ImageSuccess( TemplateView ):
    template_name = 'test_app/upload/success.html'
    fields = ( 'title', 'category', 'frontpage')
    model = models.ImageUpload

    @method_decorator( login_required )
    def dispatch( self, request, *args, **kwargs ):
        return super( ImageSuccess, self ).dispatch( request, *args, **kwargs )

class ImageDelete( DeleteView ):
    template_name = 'test_app/img/delete.html'
    fields = ( 'title', 'category', 'frontpage' )
    model = models.ImageUpload

    def get_success_url( self, **kwargs ):
        image = self.model.objects.filter( pk = self.kwargs['pk'] ).values()[0] # retrieve pk from url
        if image['category'] == 'portrait':
            print( 'portrait' )
            return reverse_lazy( 'test_app:portrait' )
        elif image['category'] == 'landscape':
            print( 'landscape' )
            return reverse_lazy( 'test_app:landscape' )
        else:
            print( 'default' )
            return reverse_lazy( 'test_app:index' )

    def get_context_data( self, **kwargs ):
        image = self.model.objects.filter( pk = self.kwargs['pk'] ).values()[0] # retrieve pk from url
        title = image['title']

        data = super().get_context_data( **kwargs )
        data['title'] = title
        data['image'] = image
        return data

    @method_decorator( login_required )
    def dispatch( self, request, *args, **kwargs ):
        return super( ImageDelete, self ).dispatch( request, *args, **kwargs )
