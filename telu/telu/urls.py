
from django.contrib import admin
from django.urls import path, include
from . import views
from api.models import MovieResource

movie_resource = MovieResource()
urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('api/', include(movie_resource.urls))
]
