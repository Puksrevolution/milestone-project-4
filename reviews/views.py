"""
Code adapted from https://github.com/BrianWhelanDublin/milestone-project-4
"""

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review


def our_reviews(request):
    """
    renders all the reviews
    """

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.stars = int(request.POST.get('stars'))
            review.save()
            messages.success(request,
                             'New Review has been added.')

    reviews = Review.objects.all()

    form = ReviewForm()
    template = 'reviews/our_reviews.html'
    context = {
        'reviews': reviews,
        'form': form,
    }

    return render(request,
                  template,
                  context)


@login_required
def edit_review(request, review_id):
    """
    View to edit a users review
    """

    review = get_object_or_404(Review, pk=review_id)
    if review.reviewer != request.user:
        messages.error(request,
                       'You do not have permission to do this.')
        return redirect(reverse('our_reviews'))
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.stars = int(request.POST.get('stars'))
            review.save()
            messages.success(request,
                             'Review has been updated.')
            return redirect(reverse('our_reviews'))
        else:
            messages.error(request,
                           'Failed to update review. Please try again later.')
    else:
        form = ReviewForm(instance=review)

    reviews = Review.objects.all()

    template = 'reviews/our_reviews.html'
    context = {
        'form': form,
        'edit_review': True,
        'review_to_edit': review,
    }

    return render(request,
                  template,
                  context)


@login_required
def delete_review(request, review_id):
    """
    View to delete a review
    """

    review = get_object_or_404(Review, pk=review_id)
    if request.user == review.reviewer:
        review.delete()
        messages.success(request, 'Review has been deleted')
        return redirect('our_reviews')
    messages.error(request, 'You are not the owner of this review.')
    return redirect('our_reviews')
