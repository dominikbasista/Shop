from django.test import TestCase
from django.db import models

import datetime

from .models import SampleModel, Product



class SampleModelTest(TestCase):

    def test_saving_and_retrieving_Model(self):

        first_item = SampleModel()
        first_item.text = "First element Sample text"
        first_item.save()

        second_item = SampleModel()
        second_item.text = "Second element Sample text"
        second_item.save()

        all_saved_items = SampleModel.objects.all()
        self.assertEqual(all_saved_items.count(), 2)

        first_Model = all_saved_items[0]
        second_Model = all_saved_items[1]

        self.assertEqual(first_item.text, "First element Sample text")
        self.assertEqual(second_item.text, "Second element Sample text")



class AddProductToDBTest(TestCase):

    def model_can_send_and_retrieve(self):

        Model = Product()
        Model.name = "Wojna i pokuj"
        Model.slug = "wojna-i-pokuj"
        Model.image = models.ImageField(upload_to='shop/alatests/pictures_tests_output',
                                       default='shop/alatests/pictures_tests_input/thumb_2.png')
        Model.description = "Lore ipsum text description"
        Model.price = 11.0
        Model.stock = 6
        Model.available = True
        Model.created = datetime.datetime.now()
        Model.updated = datetime.datetime.now()+datetime.timedelta(hours=2)

        sample_name= "Wojna i pokuj"
        sample_slug = "wojna-i-pokuj"
        sample_image = models.ImageField(upload_to='shop/alatests/pictures_tests_output',
                                            default='shop/alatests/pictures_tests_input/thumb_2.png')
        sample_description = "Lore ipsum text description"
        sample_price = 11.0
        sample_stock = 6
        sample_available = True
        sample_created = datetime.datetime.now()
        sample_updated = datetime.datetime.now() + datetime.timedelta(hours=2)

        item = Product.object.all(name="Wojna i pokuj")

        self.assertEqual(item.name, sample_name)
