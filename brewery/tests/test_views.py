import pytest
from brewery.models import Place
from brewery.views import PlaceList, PlaceDetail
from django.test import RequestFactory, TestCase
from django.urls import reverse, resolve
from mixer.backend.django import mixer

@pytest.mark.django_db
class TestPlaceViews(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(TestPlaceViews, cls).setUpClass()
        cls.place = mixer.blend(Place)
        
    def test_place_list(self):
        path = reverse('place-list')
        request = RequestFactory().get(path, {'search': 'browar'})
        response = PlaceList.as_view()(request)
        assert response.status_code == 200, 'Check place list view'
    
    def test_place_detail(self):
        path = reverse('place-detail', kwargs={'slug': self.place.slug})
        request = RequestFactory().get(path)
        response = PlaceDetail.as_view()(request, slug=self.place.slug)
        assert response.status_code == 200
