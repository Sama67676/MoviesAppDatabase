from django.contrib import admin
from restapi.models import Movie, User

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'category']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'email']

