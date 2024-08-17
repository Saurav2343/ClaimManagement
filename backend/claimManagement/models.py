from django.db import models

# Customer Details
class Customer(models.Model):
    customer_id = models.CharField(max_length=20, unique=True, primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, unique=True)

    def save(self, *args, **kwargs):
        if not self.customer_id:
            last_customer = Customer.objects.all().order_by('customer_id').last()
            if last_customer:
                last_id = int(last_customer.customer_id.split('-')[1])
                self.customer_id = f'CUST-{last_id + 1:04d}'
            else:
                self.customer_id = 'CUST-0001'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Policy Details
class Policy(models.Model):
    policy_id = models.CharField(max_length=20, unique=True, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    policy_details = models.TextField()
    policy_status = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.policy_id:
            last_policy = Policy.objects.all().order_by('policy_id').last()
            if last_policy:
                last_id = int(last_policy.policy_id.split('-')[1])
                self.policy_id = f'POL-{last_id + 1:04d}'
            else:
                self.policy_id = 'POL-0001'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Policy {self.policy_id} for {self.customer.name}"
