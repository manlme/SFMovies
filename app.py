#!python3
from flask  import Flask,jsonify,abort,json,make_response
import pymongo
import os
from pymongo import MongoClient
app = Flask(__name__, static_url_path='')
client = MongoClient()
db = client.sfmovies
@app.route('/')
def index():
    return app.send_static_file('index.html')
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
@app.route('/sfmovies/dbinfo',methods=['GET'])
def get_mongodb_info():
    return jsonify(
            {'MONGODB_PORT_27017_TCP_ADDR':os.environ.get('MONGODB_PORT_27017_TCP_ADDR','localhost'),
                'MONGODB_PORT_27017_TCP_PORT':os.environ.get('MONGODB_PORT_27017_TCP_PORT','5000'),
                'MONGODB_USERNAME':os.environ.get('MONGODB_USERNAME','none'),
                'MONGODB_PASSWORD':os.environ.get('MONGODB_PASSWORD','non'),
                'MONGODB_INSTANCE_NAME':os.environ.get('MONGODB_INSTANCE_NAME','none')})
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
