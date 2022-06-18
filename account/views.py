from django.shortcuts import render, redirect
from account.forms import RegisterUserForm
from django.views import View
from django.contrib.auth import authenticate, login, logout

class RegisterView(View):
    def get(self, request):
        return render(request, 'account/register.html', {'form':RegisterUserForm()})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
                login(request, user)
                return redirect('dashboard')
            else:
                return redirect('register')

class LoginView(View):
    def get(self, request):
        return render(request, 'account/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')