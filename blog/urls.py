from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.index),
    path('poema/<int:pk>', views.read_more, name="poema")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)