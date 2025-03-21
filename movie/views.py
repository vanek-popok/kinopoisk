from django.shortcuts import render,redirect
from .models import *
from core.models import User


# Create your views here.
def catalog(request):
    movies = Movie.objects.all()
    return render(request, 'movie/catalog.html', {'movies': movies})

def film_detail(request, film_id):
    movie = Movie.objects.get(id = film_id )

    return render(request, "movie/film_detail.html", {
        'movie': movie,
        "reviews": MovieReview.objects.filter(
            movie_id = film_id
        ).order_by('-created_at')
        } )

def leave_review(request):
    if not request.user.is_authenticated:
        return redirect('catalog')
    if request.method == 'POST':
        review_text = request.POST.get("comment")
        movie_id = request.POST.get("movie_id")
        MovieReview.objects.create(
            author = request.user,
            movie = Movie.objects.get(id=movie_id),
            text = review_text 
        )
        return redirect('film_detail', film_id=movie_id)
