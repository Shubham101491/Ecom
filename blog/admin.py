from django.contrib import admin
from blog.models import Blog_Data,Blog_Category,BlogComments

class AdminBlog_data(admin.ModelAdmin):
    list_display = ['id','blog_category','blog_title','blog_date']

class AdminBlog_Category(admin.ModelAdmin):
    list_display = ['id','blog_category']

# use multiple model in admin like this
# admin.site.register((Blog_Data,Blog_Category))

admin.site.register(Blog_Data,AdminBlog_data)
admin.site.register(Blog_Category,AdminBlog_Category)
admin.site.register(BlogComments)
