from django.contrib import admin
from .models import Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):

    list_display = ["name","email","url","create_time","post"]
    fields = ["name","email","url","text"]




admin.site.register(Comment,CommentAdmin)
