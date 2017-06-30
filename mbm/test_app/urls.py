from django.conf.urls import url
from test_app import views

app_name = 'test_app'

urlpatterns = [
    url( r'^$', views.Index.as_view(), name = 'index' ),
    url( r'portrait/', views.Portrait.as_view(), name = 'portrait' ),
    url( r'landscape/', views.Landscape.as_view(), name = 'landscape' ),
    url( r'upload/', views.Upload.as_view( template_name = 'test_app/upload/index.html' ), name = 'upload' ),
    url( r'login/', views.Login.as_view(), name = 'login' ),
    url( r'logout/', views.Logout.as_view(), name = 'logout' )
]
