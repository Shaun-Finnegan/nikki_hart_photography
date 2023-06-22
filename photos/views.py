from django.shortcuts import render, get_object_or_404
from .models import Photos
from .forms import ProductForm

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


def add_photo(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'photos/add_photo.html'
    context = {
        'form': form,
    }

    return render(request, template, context)