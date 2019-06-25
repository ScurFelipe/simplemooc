"""simplemoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include(('simplemoc.core.urls', 'simplemoc.core'), namespace='core')),
    path('conta/', include(('simplemoc.accounts.urls', 'simplemoc.accounts'), namespace='accounts')),
    path('cursos/', include(('simplemoc.courses.urls', 'simplemoc.courses'), namespace='courses')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns = ['',
#     url(r'^', include('core.urls', namespace='core')),
#     url(r'^cursos/', include('courses.urls', namespace='courses')),
#     url(r'^admin/', include(admin.site.urls)),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)