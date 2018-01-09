from django.shortcuts import render
from django.shortcuts import render_to_response,get_object_or_404
from .models import Category,Image
# Create your views here.
def view_images(request):
    return render_to_response('gallery/index.html',{
        'categories': Category.objects.all(),
        'images': Image.objects.all()
    })
def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('gallery/view_category.html', {
        'category': category,
        'posts': Image.objects.filter(category=category)
    })