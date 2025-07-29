from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
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
    user_review = Review.objects.filter(user=request.user, parent__isnull=True).first()
    all_reviews = Review.objects.filter(parent__isnull=True).select_related('user').order_by('-created_at')
    edit_mode = request.GET.get("edit") == "1" and user_review is not None

    if request.method == "POST":
        parent_id = request.POST.get("parent_id")
        text = request.POST.get("text")
        if parent_id:
            # This is a reply
            parent = get_object_or_404(Review, id=parent_id)
            Review.objects.create(
                user=request.user,
                text=text,
                parent=parent
            )
            return redirect('review')
        else:
            # This is a top-level review
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
        form = ReviewForm(instance=user_review if edit_mode else None)

    return render(request, "game/review.html", {
        "form": form,
        "user_review": user_review,
        "all_reviews": all_reviews,
        "edit_mode": edit_mode,
    })


@login_required
def leaderboard_view(request):
    users = User.objects.all().order_by('username')
    # Get each user's score from GameState
    user_scores = []
    for user in users:
        gamestate = GameState.objects.filter(user=user).first()
        score = gamestate.money if gamestate else 0
        user_scores.append({'user': user, 'score': score})
    return render(request, "game/leaderboard.html", {"user_scores": user_scores})


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


@login_required
def delete_reply(request, reply_id):
    reply = get_object_or_404(Review, id=reply_id, user=request.user)
    parent_id = reply.parent.id if reply.parent else None
    reply.delete()
    return redirect('review')



