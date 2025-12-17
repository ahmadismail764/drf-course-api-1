from django.test import TestCase, Client

class OrderTests(TestCase):
    def test_order_list(self):        
        c = Client()
        response = c.get(path='/orders/', content_type='text/plain')
        self.assertEqual(response.status_code, 200)