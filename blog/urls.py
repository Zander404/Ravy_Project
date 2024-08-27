from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.index, name='home'),
    path('poema/<int:pk>', views.read_more, name="poema"),
    path('contact/', views.contact, name='contact'),
    path('about_me/', views.about, name='about_me'),


    #Rotaas de Poemas

    path('add_poetry/', views.add_poetry, name='add_poetry'),
    path('edit_poetry/<int:pk>', views.edit_poetry, name='edit_poetry'),
    path('delete_poetry/<int:pk>', views.delete_poetry, name='delete_poetry'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)