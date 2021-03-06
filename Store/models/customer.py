from django.db import models

class Customer(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    phone=models.ImageField(max_length=20)
    email=models.EmailField(null=True)
    password = models.CharField(max_length=500)


    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            False
        

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        else:
            return  False


   