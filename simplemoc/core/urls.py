from django.urls import path
from . import views

urlpatterns = [
    # url(r'^$', 'index', name='index'),
    # url(r'^contato/$', 'contact', name='contact'),
    path('', views.home, name='home'),
    path('contato/', views.contact, name='contact'),
]