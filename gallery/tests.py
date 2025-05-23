from django.test import TestCase
from django.urls import reverse
from .models import Image, Category
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime

class GalleryViewsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.image = Image.objects.create(
            title='Test Image',
            image=SimpleUploadedFile(name='test.jpg', content=b'small image data', content_type='image/jpeg'),
            created_date=datetime.date.today(),
            age_limit=0
        )
        self.image.categories.add(self.category)

    def test_gallery_view_status_200(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Image')

    def test_gallery_filter_by_category(self):
        response = self.client.get(reverse('main'), {'category': self.category.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Image')

    def test_image_detail_view(self):
        response = self.client.get(reverse('image_detail', args=[self.image.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Image')

    def test_wrong_image_id_404(self):
        response = self.client.get(reverse('image_detail', args=[9999]))
        self.assertEqual(response.status_code, 404)
