import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
from shop.models import Product

class TestAddProductToDB:
    def test_can_add_item(self):
        obj = mixer.blend('shop.Product', name='Gillete')
        expected = 'Gillete'
        assert obj.name == expected




