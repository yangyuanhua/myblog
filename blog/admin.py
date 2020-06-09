from django.contrib import admin
from .models import Category,Post,Tag


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["title","category","user","id"]
    fields = ["title","body","category","tag","user","create_time"]

class TagAdmin(admin.ModelAdmin):
    list_display = ["id","name"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name"]




admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag,TagAdmin)
