from django.contrib import admin

# Register your models here.
from .models import Category, Priority, Todo

admin.site.register(Category)
admin.site.register(Priority)
admin.site.register(Todo)
