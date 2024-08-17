from rest_framework.serializers import ModelSerializer
from .models import Customer, Policy

class PolicySerializer(ModelSerializer):
    class Meta:
        model = Policy
        fields =[
            'policy_id',
            'policy_details',
            'policy_status'
        ]

class CustomerSerializer(ModelSerializer):
    policies = PolicySerializer(many = True, read_only= True, source = 'policy_set')

    class Meta:
        model = Customer
        fields =[
            'customer_id',
            'name',
            'email',
            'phone_number',
            'policies'
        ]