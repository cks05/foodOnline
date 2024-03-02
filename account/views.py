from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserForm
from .models import User
from django.contrib import messages

# Create your views here.
def registerUser(request):
    if request.method  == "POST":
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            
            # Create a user using form
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # form.save()
            
            # Create the user using create user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username= username, email= email, password= password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, "Your account is successfully created")
            return redirect('registerUser')
        else:
            print(form.errors)
    else:
        form = UserForm
    context  ={
        'form': form
    }
    return render(request, "account/registerUser.html", context=context)