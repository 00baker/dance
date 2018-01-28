from django.shortcuts import render
from django.shortcuts import render_to_response,get_object_or_404
from .models import Category,Image,Video
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
# Create your views here.
def view_images(request):
    return render_to_response('gallery/index.html',{
        'categories': Category.objects.all(),
        'images': Image.objects.all().order_by("-posted_on"),
    })
def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('gallery/view_category.html', {
        'category': category,
        'images': Image.objects.filter(category=category),
        'videos': Video.objects.filter(category=category)
    })
def view_videos(requerst):
    return render_to_response('gallery/video.html',{
        'videos': Video.objects.all().order_by("-posted_on"),
        'categories': Category.objects.all(),
    }
    )