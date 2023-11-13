from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm

def index(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']  
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  
                return redirect('home')  
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)  # Usar el método de login importado desde Django
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')


# from django.shortcuts import render, redirect
# # from django.contrib.auth import authenticate, login as auth_login
# # from django.contrib.auth import logout as auth_logout 
# from django.contrib.auth import authenticate, login, logout 
# from .forms import UserCreationForm, LoginForm


# # Create your views here.
# # Home page
# def index(request):
#     return render(request, 'home.html')

# def home(request):
#     return render(request, 'home.html')
# # signup page
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})

# # login page
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)  # Usar el método de login importado desde Django
#                 return redirect('home')
#             else:
#                 print(form.error_messages["invalid_login"])
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})

# def user_logout(request):
#     logout(request)
#     return redirect('home')