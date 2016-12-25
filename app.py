#!/Users/jiangdaye/workspace/restfulapp/bin/python3.4
from flask  import Flask,jsonify,abort,json,make_response
import pymongo
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient()
db = client.sfmovies
@app.route('/')
def index():
    return "Welcome to SFMovies!"
@app.route('/sfmovies/api/v1.0/movies', methods=['GET'])
def get_movies():
    return jsonify({'movies':list(db.movies.find({},{'_id':0}))})
@app.route('/sfmovies/api/v1.0/movies/<movie_title>', methods=['GET'])
def get_movie(movie_title):
    moviefilter = filter(lambda t: t['title'] == movie_title, list(db.movies.find({},{'_id':0})))
    movie = list(moviefilter)
    print(movie)
    if len(movie) == 0:
        abort(404)
    return jsonify({'movie': movie[0]})
@app.route('/sfmovies/api/v1.0/movies/locations',methods=['GET'])
def get_locations():
    return jsonify({'location':list(db.movies.distinct('location',{}))})
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
if __name__ == '__main__':
    app.run(debug=True)
