from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    confirm_password = models.CharField(max_length=500,null=True)
    otp = models.IntegerField(null=True)
    otp_verified = models.BooleanField(default=False)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False


