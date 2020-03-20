from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import TwuLoginForm
from django.contrib.auth.decorators import login_required
from . import request_twu

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for { username }!')
			return redirect('login')
		
	else:
		form = UserRegisterForm()

	return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
	return render(request, 'users/profile.html')


def TwuLogin(request):
	if request.method == 'POST':
		form = TwuLoginForm()
		#content = request_twu.request(form.username, form.password)
		return redirect('TwuInfo')
		#return render(request, 'users/TwuInfo.html', {'form': form})
	else:
		form = TwuLoginForm()


	return render(request, 'users/TwuLogin.html', {'form': form})


def TwuInfo(request):
	form = TwuLoginForm()
	return render(request, 'users/TwuInfo.html', {'form': form})