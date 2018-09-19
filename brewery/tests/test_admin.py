import pytest
from brewery import admin
from brewery.models import Place
from django.contrib.admin.sites import AdminSite
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestAdmin:
    
    def test_admin_place(self):
        site = AdminSite()
        place_admin = admin.PlaceAdmin(Place, site)
        
        place = mixer.blend(Place)
        assert place.id == 1