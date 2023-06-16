from django.shortcuts import render, get_object_or_404
from .models import Photos

# Create your views here.
def all_photos(request):

    photos = Photos.objects.all()

    context = {
        'photos': photos,
    }
    return render(request, 'photos/photos.html', context)


def photos_detail(request, photos_id):
    """ A view to show individual product details """

    photos = get_object_or_404(Photos, pk=photos_id)

    context = {
        'photos': photos,
    }

    return render(request, 'photos/photos_detail.html', context)