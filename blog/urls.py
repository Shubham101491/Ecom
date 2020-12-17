from django.urls import path
from . import views

urlpatterns = [
    path('blogs/',views.blogs,name='blogs'),
    path('bsearch/',views.bsearch,name='bsearch'),
    path('asearch/',views.asearch,name='asearch'),

    path('blog_details/',views.blog_details,name='blog_details'),
    path('blog_detail/<int:id>',views.blog_detail,name='blog_detail'),

    # APIs to post a comment
    path('postComment/',views.postComment,name='postComment'),
   
]