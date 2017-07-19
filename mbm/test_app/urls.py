from django.conf.urls import url
from test_app import views

app_name = 'test_app'

urlpatterns = [
    url( r'^$', views.Index.as_view(), name = 'index' ),
    url( r'^about/(?P<pk>\d+)$', views.About.as_view(), name = 'about' ),
    url( r'^email/$', views.Email.as_view(), name = 'email' ),
    url( r'^portrait/', views.Gallery.as_view( title = 'portrait', category = 'portrait' ), name = 'portrait' ),
    url( r'^landscape/', views.Gallery.as_view( title = 'landscape', category = 'landscape' ), name = 'landscape' ),
    url( r'^img/new/$', views.ImageCreate.as_view(), name = 'upload' ),
    url( r'^img/success/$', views.ImageSuccess.as_view(), name = 'success' ),
    url( r'^img/(?P<pk>\d+)/$', views.ImageUpdate.as_view(), name = 'update' ),
    url( r'^img/(?P<pk>\d+)/delete/$', views.ImageDelete.as_view(), name = 'delete' ),
    url( r'^login/', views.Login.as_view(), name = 'login' ),
    url( r'^logout/', views.Logout.as_view(), name = 'logout' ),
]
