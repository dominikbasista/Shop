from django.http import HttpResponse
from django.test import TestCase
from orders.views import order_create

class ViewTest(TestCase):

    def test_order_create_can_send_POST_request(self):
        request = HttpResponse()
        request.method = 'POST'
        text = "New item added"
        request.POST["new_element"] = text
        response = order_create(request)
        self.assertIn(text, response.content.decode())

    def test_page_can_load_all_items(self):
        pass


    def test_user_can_login(self):
        pass

    def test_user_can_register(self):
        pass
