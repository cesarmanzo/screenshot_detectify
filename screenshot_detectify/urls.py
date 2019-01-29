from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from screenshot.views import *
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()

urlpatterns = [
    path('', welcome),
    path('rest_framework', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('read_source', read_source, name = 'read_source'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)