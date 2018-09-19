import pytest
from brewery.models import Place, my_handler
from brewery.tool import random_slug
from django.test import TestCase
from django.urls import reverse, resolve
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestPlace(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(TestPlace, cls).setUpClass()
        cls.place = mixer.blend(Place, name='Name Test Of Brewery')
        
    def test_model(self):
        assert self.place.id == 1, 'Create place model'
        
    def test_name_unicode(self):
        assert self.place.__unicode__() == 'Name Test Of Brewery', 'Check get unicode model name'
    
    def test_get_api_url(self):
        path = reverse('place-api-rud', kwargs={'pk':self.place.pk})
        assert path == self.place.get_api_url(), 'Check API url'
    
    def test_my_handler(self):
        my_handler(Place, self.place)
        assert random_slug(self.place.slug)[:-5] == self.place.slug
        assert self.place.slug == 'name-test-of-brewery', 'Check slug generate'
