from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse

from .forms import ReviewForm
from .models import Review, GameState


@login_required
def play_view(request):
    gamestate, created = GameState.objects.get_or_create(user=request.user)
    return render(request, "game/play.html", {"money": gamestate.money})


@login_required
def review_page(request):
    user_review = Review.objects.filter(user=request.user).first()
    all_reviews = Review.objects.select_related('user').order_by('-created_at')

    if request.method == "POST":
        if user_review:
            form = ReviewForm(request.POST, instance=user_review)
        else:
            form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review')
    else:
        form = ReviewForm(instance=user_review)

    return render(request, "game/review.html", {
        "form": form,
        "user_review": user_review,
        "all_reviews": all_reviews,
    })


@login_required
def leaderboard_view(request):
    users = User.objects.all().order_by('username')
    return render(request, "game/leaderboard.html", {"users": users})


@login_required
def delete_review(request):
    user_review = Review.objects.filter(user=request.user).first()
    if user_review:
        user_review.delete()
    return redirect('review')


@login_required
def earn_money(request):
    gamestate = GameState.objects.get(user=request.user)
    gamestate.money += 10  # or whatever amount you want to add
    gamestate.save()
    return JsonResponse({'money': gamestate.money})



