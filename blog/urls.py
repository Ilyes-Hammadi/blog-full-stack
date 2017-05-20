"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from articles.views import index, detail, create, update, delete, ArticleViewSet
from users.views import login, logout, signup, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'articles', ArticleViewSet)





urlpatterns = [
    # List of all articles
    url(r'^$', view=index, name='index'),
    
    # Detail of an article
    url(r'^detail/(?P<id>\d+)$', view=detail, name='detail'),
    
    # Create an article
    url(r'^create/$', view=create, name='create'),

    # Update an article
    url(r'^update/(?P<id>\d+)/$', view=update, name='update'),

    # Delete an article
    url(r'^delete/(?P<id>\d+)/$', view=delete, name='delete'),

    url(r'^login/$', login, name='login'),

    url(r'^logout/$',logout, name='logout'),
    
    url(r'^signup/$', signup, name='signup'),

    # Admin
    url(r'^admin/', admin.site.urls),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)