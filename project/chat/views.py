from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Use Django's password hashing (not shown here)
        user = User.objects.create_user(username=username, password=password)
        # ... (other logic, avoid storing password in session)

        # Authenticate the user if you need to immediately redirect
        user_auth = authenticate(username=username, password=password)
        if user_auth is not None:
            login(request, user_auth)
            return redirect('app')
        else:
            # Handle invalid credentials
            pass
    return render(request, 'signup.html')

def app(request):
    if request.method == "POST":
        logout(request)

    # Authenticate the user if needed to access this view
    if not request.user.is_authenticated:
        return redirect('index')

    # Access the username securely (no password printing)
    username = request.user.username

    # Do something with the username
    return render(request, 'app.html', {"username": username})

def loginA(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        # print(request.POST)
        if user is not None:
            # User authenticated successfully
            login(request,user)
            return redirect('app')  # Redirect to the app page after login
        else:
            # Invalid credentials
            # Display an error message or redirect to a dedicated error page
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        # GET request (display login form)
        return render(request, 'login.html')