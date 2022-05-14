from django.shortcuts import render
from .forms import RegistrationForm
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

def registration_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = RegistrationForm()
    context = {'form':form}
    return render(request, 'accounts/registration.html', context)
    
