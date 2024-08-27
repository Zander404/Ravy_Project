from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.index, name='home'),
    path('poema/<int:pk>', views.read_more, name="poema"),
    path('contact/', views.contact, name='contact'),
    path('about_me/', views.about, name='about_me')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)