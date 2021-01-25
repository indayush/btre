from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):

    # checking if the request type is GET or POST
    if request.method == 'POST':
        print(request)
        print("Request is submitted")
        # print("Request is submitted " + request) This is not allowed
        # i.e. - Mixed static and dynamic values
        # return redirect('register')

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        # Checking if passwords match
        if password == password2 :
            # Check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already registered')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now Registered')
                    return redirect('login')
                    '''
                    For logging the User in After Registeration
                    auth.login(request, user)
                    messages.success(request, 'You are now Registered & Logged In')
                    return redirect('index')
                    '''
        else:
            print('password = ' + password)
            print('password2 = ' + password2)

            messages.error(request, 'Passwords do not match')
            return redirect('register')
       
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        print(request)
        # Login User 
    else:
        return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

