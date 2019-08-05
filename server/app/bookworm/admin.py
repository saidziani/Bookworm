from django.contrib import admin
from .models import House, Writer, Category, Book

admin.site.register(House)
admin.site.register(Writer)
admin.site.register(Category)
admin.site.register(Book)

