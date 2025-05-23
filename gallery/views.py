from django.shortcuts import render, get_object_or_404
from .models import Image, Category

def gallery_view(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        images = Image.objects.filter(categories__id=category_id).distinct()
    else:
        images = Image.objects.all()
    return render(request, 'gallery.html', {
        'images': images,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None
    })

def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, 'image_detail.html', {'image': image})

def static_gallery_view(request):
    image_folder = os.path.join(settings.MEDIA_ROOT, 'gallery_images')
    images = [
        'gallery_images/' + filename
        for filename in os.listdir(image_folder)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
    ]
    return render(request, 'static_gallery.html', {'images': images})