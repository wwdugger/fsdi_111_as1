from flask import Flask, render_template

app = Flask(__name__)

#@app.get("/")
#def index():
#    return ("<h1>Hello world!</h1>")

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/about")
def about():
    me = {
        "first_name": "Wesley",
        "last_name": "Dugger",
        "hobbies": "Fitness",
        "bio": "My name is Wesley Dugger and I am a student at SDGKU to become a full stack developer, I have ambitions to become a freelance web developer." 
    }
    return render_template("about.html", about_dict=me)

@app.get("/objects")
def objects():
    return render_template("objects.html")