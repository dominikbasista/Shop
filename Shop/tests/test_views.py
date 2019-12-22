from django.http import HttpResponse
from django.test import TestCase
from shop.views import products_list
from orders.views import order_create
from django.test import RequestFactory
from django.test import Client

class TestHomeView:
    def test_home_page_can_display_product_list(self):
        c = Client()
        resp = products_list(c.get('/'))
        request1=RequestFactory().get("/")
        response = products_list()(request1)
        assert response.status_code ==200, "Dziala"

# class ViewTest(TestCase):
#
#     def test_display_main_page(self):
#         response = self.client.get('/')
#
#     def test_order_create_can_send_POST_request(self):
#         request = HttpResponse()
#         request.method = 'POST'
#         text = "New item added"
#         request.POST["new_element"] = text
#         response = order_create(request)
#         self.assertIn(text, response.content.decode())
#
#     def test_page_can_load_all_items(self):
#         pass
#
#
#     def test_user_can_login(self):
#         pass
#
#     def test_user_can_register(self):
#         pass

