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
        user_review = Review.objects.filter(user=request.user, parent__isnull=True).first()
    all_reviews = Review.objects.filter(parent__isnull=True).order_by('-id').prefetch_related('replies')
    show_review_posted_modal = False
    show_review_deleted_modal = False
    show_review_edited_modal = False
    show_reply_deleted_modal = False

    is_edit = request.GET.get('edit') == '1' and user_review

    if request.method == "POST":
        # Handle replies
        if request.POST.get('parent_id'):
            parent_id = request.POST.get('parent_id')
            parent_review = Review.objects.filter(id=parent_id, parent__isnull=True).first()
            if parent_review and request.user.is_authenticated:
                text = request.POST.get('text', '').strip()
                if text:
                    Review.objects.create(
                        user=request.user,
                        text=text,
                        parent=parent_review
                    )
                return redirect('review')
        # Editing existing review
        elif is_edit and user_review:
            form = ReviewForm(request.POST, instance=user_review)
            if form.is_valid():
                form.save()
                return redirect(f"{reverse('review')}?edited=1")
        # New review
        elif not user_review:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.save()
                return redirect(f"{reverse('review')}?posted=1")
        else:
            form = ReviewForm(instance=user_review)
    else:
        if is_edit and user_review:
            form = ReviewForm(instance=user_review)
        else:
            form = ReviewForm()

    if request.GET.get('posted') == '1':
        show_review_posted_modal = True
    if request.GET.get('deleted') == '1':
        show_review_deleted_modal = True
    if request.GET.get('edited') == '1':
        show_review_edited_modal = True
    if request.GET.get('reply_deleted') == '1':
        show_reply_deleted_modal = True

    return render(request, "game/review.html", {
        "form": form,
        "user_review": user_review,
        "all_reviews": all_reviews,
        "show_review_posted_modal": show_review_posted_modal,
        "show_review_deleted_modal": show_review_deleted_modal,
        "show_review_edited_modal": show_review_edited_modal,
        "show_reply_deleted_modal": show_reply_deleted_modal,
        "is_edit": is_edit,
    })


@login_required
def delete_review(request):
    if request.method == "POST":
        review = Review.objects.filter(user=request.user).first()
        if review:
            review.delete()
            return redirect(f"{reverse('review')}?deleted=1")
    return redirect('review')


@login_required
def delete_reply(request, reply_id):
    if request.method == "POST":
        reply = Review.objects.filter(id=reply_id, parent__isnull=False, user=request.user).first()
        if reply:
            reply.delete()
            return redirect(f"{reverse('review')}?reply_deleted=1")
    return redirect('review')


