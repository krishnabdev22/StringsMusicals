from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    # otp = models.IntegerField(null=True)
    # otp_verified = models.BooleanField(default=False)

    def register(self):
        self.save()
