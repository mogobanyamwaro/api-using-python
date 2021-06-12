from django.contrib import admin
from .models import Genre, Movie
# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'daily_rate',
                    'number_in_stock', 'genre', 'date_created')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MoviesAdmin)
