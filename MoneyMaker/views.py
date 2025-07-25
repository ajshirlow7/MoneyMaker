from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def home_page_view(request):
    print("User:", request.user, "Authenticated:", request.user.is_authenticated)
    form = UserCreationForm()
    login_form = AuthenticationForm()
    return render(request, "homepage.html", {"form": form, "login_form": login_form})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            # Render homepage with errors if form is invalid
            return render(request, "homepage.html", {"form": form})
    else:
        return redirect("home")

