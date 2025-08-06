from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import ReviewForm
from .models import Review  # Make sure to import the Review model
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home_page_view(request):
    form = UserCreationForm()
    login_form = AuthenticationForm()
    return render(
        request,
        "homepage.html",
        {
            "form": form,
            "login_form": login_form,
        }
    )


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
    messages.info(request, f'You have logged out "{username}", come back soon.')
    return redirect("home")


def review_view(request):
    user_review = None
    if request.user.is_authenticated:
        user_review = Review.objects.filter(user=request.user).first()
    all_reviews = Review.objects.all().order_by('-id')
    show_review_posted_modal = False
    show_review_deleted_modal = False

    if request.method == "POST" and not user_review:
        if request.POST.get('parent_id'):
            form = ReviewForm()
        else:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.save()
                return redirect(f"{reverse('review')}?posted=1")
    else:
        form = ReviewForm()

    if request.GET.get('posted') == '1':
        show_review_posted_modal = True
    if request.GET.get('deleted') == '1':
        show_review_deleted_modal = True

    return render(request, "game/review.html", {
        "form": form,
        "user_review": user_review,
        "all_reviews": all_reviews,
        "show_review_posted_modal": show_review_posted_modal,
        "show_review_deleted_modal": show_review_deleted_modal,
    })


@login_required
def delete_review(request):
    if request.method == "POST":
        review = Review.objects.filter(user=request.user).first()
        if review:
            review.delete()
            return redirect(f"{reverse('review')}?deleted=1")
    return redirect('review')


