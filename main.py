#!/Users/christopher.ogbunuzor/.pyenv/shims/python
from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
import json
from config import Config
app = Flask(__name__, instance_relative_config=False)
app.config.from_object(Config)

db = SQLAlchemy(app)

class Movies(db.model):
    id = db.Column('id', db.Integer, PRIMARY_KEY=True)
    name = db.Column( db.VARCHAR(length=255))
    release_year = db.Column(db.Integer)


movie_db = {
    "1": {"name": "star", "title":"i love star trex"},
    "2": {"name": "5star", "title":"Originals"}
}
#return json.dumps(movie_db)
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/hello")
def world():
    return """<html>
<body>

<h2>Image Size</h2>

<p>Here we specify the width and height of an image with the width and height attributes:</p>

<img src="/static/imggirl.jpg" alt="Girl in a jacket" width="500" height="600">

</body>
</html>"""

@app.route("/movies")
def movies():
    movies = Movies.query.all()
    html_response = "<ul>"
    for m in movies:
        html_response+= "<li>"+ "<a href ='/movies/'"+str(m.id)+"'>"+ m.name + "</a></li>"
    return json.dumps(movie_db)

@app.route("/movies/<movieid>")
def getmovies_id(movieid):
    return json.dumps(movie_db[movieid])

#create a post api for creating new task in todo list
@app.route("/movies/add", methods=['POST'])
def addmovie():
    req_data= request.get_json()
    movie = req_data['movie']
    #name = req_data['name']
    #title = req_data['title']
    newmovie = {"3":movie}
    movie_db.update(newmovie)
    return "movie addition was successful"

# @app.route("/getmovieshtmlformat")
# def addmovie():
#     req_data= request.get_json()
#     movie = req_data['movie']
#     #name = req_data['name']
#     #title = req_data['title']
#     newmovie = {"3":movie}
#     movie_db.update(newmovie)
#     return "movie addition was successful"


if __name__ == "__main__":
    app.run(host = '127.0.0.1')
