from django.shortcuts import render,HttpResponse,redirect
from ecom import settings
from blog.models import Blog_Data,Blog_Category,BlogComments

from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages

# Authnticate APIs
def blogs(request):
    blg = None
    blogss = None
    catego = Blog_Category.objects.all()
    categoryID = request.GET.get('category')
    
    if categoryID:
        blg = Blog_Data.objects.filter(blog_category_id = categoryID)
    else:
        blg = Blog_Data.objects.all()
    data = {}
    data['blog'] = blg
    data['categ'] = catego
    data['new'] = blogss
    # use base url in dictionary
    data['BASE_URL'] = settings.BASE_URL
    return render(request,'blog/blog.html',data)

def bsearch(request):
    query = request.GET['query']
    post = Blog_Data.objects.filter(blog_title__icontains=query)
    params = {'blog':post}
    data = {"BASE_URL":settings.BASE_URL}
    return render(request,'blog/blog-search.html',params,data)

def blog_detail(request,id):
    allimages = Blog_Data.objects.filter(id=id)
    return render(request,'blog/blog-details.html',{"BASE_URL":settings.BASE_URL,'images':allimages})

def asearch(request):
    query = request.GET['query']
    post = Blog_Data.objects.filter(blog_content__icontains=query)
    params = {'blog':post}
    data = {"BASE_URL":settings.BASE_URL}
    return render(request,'blog/blog-details.html',params,data)

def blog_details(request):
    allimages = Blog_Data.objects.all()
    return render(request,'blog/blog-details.html',{"BASE_URL":settings.BASE_URL,'categ':allimages})

def postComment(request):
    if request.method == "POST":
        comment = request.POST['comment']
        name = request.name['name']
        email = request.POST['email']
        blog = BlogComments(comment=comment,name=name,email=email)
        blog.save()
        print(blog)
        
        return render(request,'blog/blog-details.html',{"BASE_URL": settings.BASE_URL})
    else:
        return render(request,'blog/blog-details.html',{"BASE_URL": settings.BASE_URL})