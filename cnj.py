from flask import *
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():

    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    image_tag = "<img src="+response['icon_url']+" alt='Chucks Image'>"
    joke = response['value']

    joke = joke.replace("Chuck","Aashiq")
    joke = joke.replace("Norris","Adams")
    joke = joke.replace("chuck","Aashiq")
    joke = joke.replace("norris","Adams")
    joke = joke.replace("CHUCK","Aashiq")
    joke = joke.replace("NORRIS","Adams")

    return image_tag+"<br/><br/><strong>Random Chuck Norris joke: </strong>" + "<h1>"+joke+"</h1>"


