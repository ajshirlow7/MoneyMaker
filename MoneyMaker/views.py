from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages


def home_page_view(request):
    from django.contrib import messages
    messages.info(request, "Test message: If you see this, messages work!")
    form = UserCreationForm()
    login_form = AuthenticationForm()
    return render(request, "homepage.html", {"form": form, "login_form": login_form})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'You have logged in as "{user.username}"')
            return redirect("home")
        else:
            return render(request, "homepage.html", {"form": form})
    else:
        return redirect("home")

def logout_view(request):
    username = request.user.username
    logout(request)
    messages.info(request, f'You have logged out as "{username}"')
    return redirect("home")

