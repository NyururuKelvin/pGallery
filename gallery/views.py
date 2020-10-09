from django.shortcuts import render,redirect

# Views.
def home(request):
    return render(request, 'galleries/gallery.html')
