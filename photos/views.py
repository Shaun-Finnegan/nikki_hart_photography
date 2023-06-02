from django.shortcuts import render
from .models import Photos

# Create your views here.
def all_photos(request):

    photos = Photos.objects.all()

    context = {
        'photos': photos,
    }
    return render(request, 'photos/photos.html', context)