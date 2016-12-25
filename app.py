#!python3
from flask  import Flask,jsonify,abort,json,make_response
import pymongo
import os
import csv
from pymongo import MongoClient
from urllib.parse import quote_plus
app = Flask(__name__, static_url_path='')
mongo_host = os.environ.get('MONGODB_PORT_27017_TCP_ADDR','localhost')
mongo_port = os.environ.get('MONGODB_PORT_27017_TCP_PORT',5000)
mongo_username = os.environ.get('MONGODB_USERNAME','admin')
mongo_password = os.environ.get('MONGODB_PASSWORD','password')
mongo_db = os.environ.get('MONGODB_INSTANCE_NAME','movies')
uri = "mongodb://%s:%s@%s:%d/%s" % (quote_plus(mongo_username), quote_plus(mongo_password), mongo_host,int(mongo_port),mongo_db)
client = MongoClient(uri)
db = client.get_default_database()
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
@app.route('/sfmovies/actions/dbinfo',methods=['GET'])
def get_mongodb_info():
    return jsonify(
            {'MONGODB_PORT_27017_TCP_ADDR':os.environ.get('MONGODB_PORT_27017_TCP_ADDR','localhost'),
                'MONGODB_PORT_27017_TCP_PORT':os.environ.get('MONGODB_PORT_27017_TCP_PORT','5000'),
                'MONGODB_USERNAME':os.environ.get('MONGODB_USERNAME','none'),
                'MONGODB_PASSWORD':os.environ.get('MONGODB_PASSWORD','non'),
                'MONGODB_INSTANCE_NAME':os.environ.get('MONGODB_INSTANCE_NAME','none')})
@app.route('/sfmovies/actions/initdb', methods=['GET'])
def init_database():
    movies = db.movies
    with open('/src/Film_Locations_in_San_Francisco.csv', 'rt') as f:
        reader = csv.reader(f)
        for movie in reader:
            title, release_year, location, fun_fact, p_company, distributor, director, writer,actor1, actor2, actor3 = movie
            if(movies.find({'title':title}).count() >0):
                movies.update_one({'title':title},{'$push':{'location':location,'fun_fact':fun_fact}})
            else:
                movie = {
                    'title':title,
                    'release_year':release_year,
                    'location':[location],
                    'fun_fact':[fun_fact],
                    'p_company':p_company,
                    'distributor':distributor,
                    'director':director,
                    'writer':writer,
                    'actor1':actor1,
                    'actor2':actor2,
                    'actor3':actor3}
                movies.insert_one(movie)
    return jsonify({'insertdb':'OK'})
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
