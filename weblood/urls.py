from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from blooddonor.views import DonorView
from rest_framework import routers

route = routers.DefaultRouter()
route.register('', DonorView, basename='donorview')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blooddonor.urls')),
    path('api/', include(route.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
