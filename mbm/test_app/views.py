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
class Index( TemplateView ):
    template_name = 'test_app/index.html'

class Portrait( ListView ):
    template_name = 'test_app/portrait/index.html'
    context_object_name = "image_uploads"
    model = models.ImageUpload

class Landscape( TemplateView ):
    template_name = 'test_app/landscape/index.html'

class Login( FormView ):
    template_name = 'test_app/login/index.html'

    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    success_url = settings.LOGIN_REDIRECT_URL

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

class Upload( CreateView ):
    form_class = forms.ImageUploadForm
    success_url = reverse_lazy( 'test_app:index' )

    # def form_valid(self, form):
    #     isvalid = super( Upload, self ).form_valid( form )
    #
    #     if self.request.FILES.get( 'image' ):
    #         m = ImageUpload.objects.get_or_create( image = image )[0]
    #         m.image = form.cleaned_data['image']
    #         m.save()
    #
    #         return isvalid
    #
    # def get_context_data(self, **kwargs):
    #     context = super( Upload, self ).get_context_data( **kwargs )
    #
    #     return context

    @method_decorator( login_required )
    def dispatch( self, request, *args, **kwargs ):
        return super( Upload, self ).dispatch( request, *args, **kwargs )
