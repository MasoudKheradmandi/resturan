from django.contrib.auth import login , authenticate ,logout
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.

def SignupView(request):

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('resturan:home')
	else:
		form = UserCreationForm()

	return render(request,'signup.html',{'form':form})


def LoginView(request):
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request,user)
			return redirect('resturan:home')


	form = AuthenticationForm()
	return render(request,'login.html',{'form':form})


def LogOut(request):
	logout(request)
	return redirect('resturan:home')