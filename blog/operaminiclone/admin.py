from typing import Any
from django.contrib import admin
from . models import Blog, AuthorProfile, Comment, Reply, Contact
from datetime import datetime
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Register your models here.
@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display=['id', 'heading', 'content', 'blog_status', 'author', 'pub_date', 'coverimage','link']
    list_filter = ('blog_status', 'categories')
    search_fields = ('heading', 'content')
    formfield_overrides = {
       'content': {'widget': CKEditorUploadingWidget},
    }

    def save_model(self, request, obj, form, change):
        if obj.pub_date is None:
        # Set the pub_date to the current date and time
            obj.pub_date = datetime.now()
        pub_year=obj.pub_date.year
        pub_month=obj.pub_date.month
        formatted_date=f"{pub_year}/{pub_month}"
        obj.link=f"{formatted_date}/{obj.heading.lower().replace(' ', '-')}"
        return super().save_model(request, obj, form, change)
    
    



admin.site.register(AuthorProfile)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Contact)
