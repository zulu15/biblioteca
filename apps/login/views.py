from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_param = request.GET.get("next", False)
            return redirect(next_param if next_param else 'index')
        else:
            return render(request, 'login.html', {'username':username,'error':'Usuario y/o contraseña incorrecta'})
    return render(request, template_name = 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
