from django.urls import reverse, resolve


class TestUrls:
    
    def test_index_url(self):
        path = reverse('place-list')
        assert resolve(path).view_name == 'place-list'
        
    def test_detail_url(self):
        path = reverse('place-detail', kwargs={'slug': 1})
        assert resolve(path).view_name == 'place-detail'
