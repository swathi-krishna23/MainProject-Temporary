from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'client'

urlpatterns = [
    # /client/
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),

    # /client/register/
    path('register/', views.register, name='register'),
    
    # /client/view/
    path('view/', views.view, name='view'),
    
    # /client/upload/
    path('upload/', views.input, name='input'),
    
    # /client/search/
    path('search/', views.searchBar, name='search'),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

