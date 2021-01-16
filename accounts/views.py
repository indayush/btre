from django.shortcuts import render, redirect

def register(request):

    # checking if the request type is GET or POST
    if request.method == 'POST':
        print(request)
        print("Request is submitted")
        # print("Request is submitted " + request) This is not allowed
        # i.e. - Mixed static and dynamic values
        # return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        print(request)
        # Login USer 
    else:
        return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

