from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from .models import Customer, Policy
from .serializer import CustomerSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND
# Create your views here.

class CustomerSearchView(GenericAPIView):
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        phone_number = request.query_params.get('phone_number', None)
        email = request.query_params.get('email', None)
        policy_id = request.query_params.get('policy_id', None)
        if phone_number: 
            customer = Customer.objects.filter(phone_number = phone_number).first()
        elif email:
            customer = Customer.objects.filter(email = email).first()
        elif policy_id:
            policy = Policy.objects.filter(policy_id = policy_id).first()
            customer = policy.customer if policy else None
        else:
            return Response({"error": "Please provide a valid phone number/ email/ policy-id to proceed"}, status=HTTP_400_BAD_REQUEST)
        
        if customer:
            serializer = self.get_serializer(customer)
            return Response(serializer.data)
        else: 
            return Response({"error": "Customer not found."}, status=HTTP_404_NOT_FOUND)

class ReactView(APIView):
    def get(self, request):
        output = [ {
            'customer_id': customer.customer_id,
            'name': customer.name,
            'email': customer.email,
            'phone_number': customer.phone_number,
            'policies': [
                    {
                        'policy_id': policy.policy_id,
                        'policy_details': policy.policy_details,
                        'policy_status': policy.policy_status
                    }
                    for policy in Policy.objects.filter(customer=customer)
                ]
        }
        for customer in Customer.objects.all()
        ]
        return Response(output)
    
        