from django.shortcuts import render, redirect
from Store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View

class Signup(View):
    def get( request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        Firstname = postData.get('Firstname')
        Lastname = postData.get('Lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'Firstname': Firstname,
            'Lastname': Lastname,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(Firstname=Firstname,
                            Lastname=Lastname,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(Firstname, Lastname, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('index')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer( customer):
        error_message = None
        if (not customer.Firstname):
            error_message = "First Name Required !!"
        elif len(customer.Firstname) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.Lastname:
            error_message = 'Last Name Required'
        elif len(customer.Lastname) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message
