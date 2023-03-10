from flask import Flask


app = Flask(__name__)


@app.get("/")
def about_me():
    me ={
        "first_name": "Kevin",
        "last_name": "Fierro",
        "hobbies": "Play videogames",
        "active": True
    }
    
    return me