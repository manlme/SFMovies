# SFMovies
the app is hosted on DAOCLOUD with CI enabled with git repository

backend :
    python flask pymongo and mongodb service provided by DAOCLOUD.
frontend:
    a simple web page which can get locations for movies with autocomplete.

restful webservice:
entry:
    http://kelevensh-sfmovies.daoapp.io/
get dbinfo:
    http://kelevensh-sfmovies.daoapp.io/sfmovies/actions/dbinfo
populate db:
    http://kelevensh-sfmovies.daoapp.io/sfmovies/actions/initdb
get movies:
   http://kelevensh-sfmovies.daoapp.io/sfmovies/api/v1.0/movies
	 http://kelevensh-sfmovies.daoapp.io/sfmovies/api/v1.0/movies/<movie_title>

get locations:
   http://kelevensh-sfmovies.daoapp.io/sfmovies/api/v1.0/locations

