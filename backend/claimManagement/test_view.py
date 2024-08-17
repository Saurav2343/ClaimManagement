# claimManagement/tests/test_view.py

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Customer, Policy
import json

class CustomerSearchViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()  # Use APIClient
        self.customer = Customer.objects.create(
            name="John Doe",
            phone_number="1234567890",
            email="john.doe@example.com"
        )
        self.policy = Policy.objects.create(
            policy_id="1",
            customer=self.customer
        )

    def test_search_by_phone_number(self):
        url = reverse('search')  # Updated URL name
        response = self.client.get(url, {'phone_number': '1234567890'})
        print(type(response))  # Debugging: Check response type
        print(response.content)  # Debugging: Check response content
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data['name'], 'John Doe')

    def test_search_by_email(self):
        url = reverse('search')  # Updated URL name
        response = self.client.get(url, {'email': 'john.doe@example.com'})
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data['name'], 'John Doe')

    def test_search_by_policy_id(self):
        url = reverse('search')  # Updated URL name
        response = self.client.get(url, {'policy_id': 'POL123'})
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data['name'], 'John Doe')

    def test_search_with_invalid_params(self):
        url = reverse('search')  # Updated URL name
        response = self.client.get(url, {'phone_number': '0000000000'})
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response_data['error'], 'Customer not found.')

    def test_search_without_params(self):
        url = reverse('search')  # Updated URL name
        response = self.client.get(url)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_data['error'], 'Please provide a valid phone number/ email/ policy-id to proceed')
