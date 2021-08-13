from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import InputForm, UserSignupForm



def register(request):
    if request.method == 'POST':
        form=UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            messages.success(request, 'You have been signed up')
            return redirect('/login/')
    else:
        form=UserSignupForm()
    return render(request, 'users/register.html', {'form':form})

def apply(request):
    form=InputForm()
    return render(request, 'users/application.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')




