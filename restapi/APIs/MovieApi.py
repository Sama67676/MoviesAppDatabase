from typing import List
from ninja import Router
from restapi.models import Movie
from restapi.schemas import MovieOut, UserOut


movie_router= Router(tags=['Movie_router'])

@movie_router.get('display_all_movies', response={
    200: List[MovieOut]
})
def display_all_movies(request):
    movies= Movie.objects.all()
    return 200, movies
