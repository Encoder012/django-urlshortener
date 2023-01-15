from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('send/', views.send, name = "send"),
    # re_path(r'^url/(?P<customURL>\w+)/$', views.customURL, name="customURL"),
    path('multiple/', views.multipleURLS, name = 'multiple'),
    path('<str:customURL>/',views.customURL, name = "customURL")
]
