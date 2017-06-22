from django.conf.urls import url
from test_app import views

app_name = 'test_app'

urlpatterns = [
    url( r'^$', views.index, name = 'index' ),
    url( r'portrait/', views.portrait, name = 'portrait' ),
    url( r'landscape/', views.landscape, name = 'landscape' ),
    url( r'contact/', views.contact, name = 'contact' ),
    url( r'users/', views.users, name = 'users' ),
    url( r'upload/', views.upload, name = 'upload' ),
]
