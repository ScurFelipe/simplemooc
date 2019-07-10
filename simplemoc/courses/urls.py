from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:pk>/', views.details, name='details'),
    # path('<string:slug>/', views.details, name='details'),
    # re_path('^(?P<pk>\d+)/$', views.details, name='details'),
    re_path('^(?P<slug>[\w_-]+)/$', views.details, name='details'),
    re_path('^(?P<slug>[\w_-]+)/inscricao/$', views.enrollment, name='enrollment'),
    re_path('^(?P<slug>[\w_-]+)/cancelar-inscricao/$', views.undo_enrollment, name='undo_enrollment'),
    re_path('^(?P<slug>[\w_-]+)/anuncios/$', views.announcements, name='announcements'),
    re_path('^(?P<slug>[\w_-]+)/anuncios/(?P<pk>\d+)/$', views.show_announcement, name='show_announcement'),
    # url(r'^(?P<slug>[\w_-]+)/anuncios/$', views.announcements, name='announcements'),
    re_path('^(?P<slug>[\w_-]+)/aulas/$', views.lessons, name='lessons'),
    re_path('^(?P<slug>[\w_-]+)/aulas/(?P<pk>\d+)/$', views.single_lesson, name='single_lesson'),
    re_path('^(?P<slug>[\w_-]+)/materiais/(?P<pk>\d+)/$', views.material, name='material'),
    # path('contato/', views.courses, name='index'),
]
