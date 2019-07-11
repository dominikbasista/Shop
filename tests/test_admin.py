from django.contrib.admin.sites import AdminSite
import pytest
from mixer.backend.django import mixer
from shop.admin import ProductAdmin
from shop.models import Product

pytestmark = pytest.mark.django_db

class TestModelProduct:
    def test_user_can_add_product_throu_admin_page(self):
        obj = mixer.blend('shop.Product', name='Gillete')
        site = AdminSite() #there is no other way to enstantiate Admin
        post_admin = ProductAdmin(Product(), site)
        post_admin(obj)



