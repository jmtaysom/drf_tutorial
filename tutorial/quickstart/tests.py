from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory


# Using the standard RequestFactory API to create a form POST request

class AccountTests(APITestCase):
    def test_create_user(self):
        factory = APIRequestFactory()
        request = factory.post('/users/', {'username': 'a person', 'email': 'some@address.com'})
        response = self.client.get('/users/1/')
        #self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'username': 'a person', 'email': 'some@address.com'})
