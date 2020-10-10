from django.shortcuts import render,redirect
from .models import Image,Category,Location

# Views.
def home(request):

    # Default view
    images=Image.objects.all()
    return render(request, 'galleries/gallery.html', {'images':images})

def get_image_by_id(request,image_id):
    images=Image.get_image_by_id(image_id)
    return render(request,'galleries/gallery.html', {'images':images})

def search_category(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term=request.GET.get("image")
        searched_images=Image.search_by_title(search_term)
        message=f"{search_term}"
        
        return render(request,'galleries/search_category.html',{"message":message,"images":searched_images})
    
    else:
        message= "You haven't searched for anything."
        return render(request,'galleries/search_category.html',{"message":message})

def filter_by_location(request,location_id):
    try:
        get_location_id=Location.objects.get(pk=location_id)
        location=Image.filter_by_location(get_location_id) 
        message=f'{get_location_id}' 
        
    except Image.DoesNotExist:
        Http404('Image does not exist')
        
    return render(request,'galleries/location.html',{'message':message,'locations':location})


def get_image_id(request,image_id):
    try:
        image=Image.get_image_by_id(image_id)
        message=f'{image.image_name}'
    except Image.DoesNotExist:
        Http404('Image Does Not Exist')
    
    return render(request, 'galleries/image.html',{'image':image,'message':message,'title':image.image_name})
