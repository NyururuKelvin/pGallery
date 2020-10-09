from django.shortcuts import render,redirect
from .models import Image,Category,Location

# Views.
def home(request):

    # Default view
    images=Image.objects.all()
    return render(request, 'galleries/gallery.html', {'images':images})

def search_category(request):
    if 'category' in request.GET and request.GET['category']:
        search_term=request.GET.get('category')
        images =Image.search_image(search_term)
        message=f'{search_term}'
        
        return render(request,'galleries/search_category.html',{'message':message,'images':images,'title':search_term})
    
    else:
        message=f"You haven't searched for anything."
        return render(request,'galleries/search_category.html',{'message':message})
