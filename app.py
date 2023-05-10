from flask import Flask, render_template
from templates import *

app = Flask(__name__)

@app.route("/")
def functionIndex():
    return render_template('index.html')

@app.route("/about")
def functionAbout():
    variable = "anuj"
    # return render_template('about.html', name=variable)
    return render_template('about.html', name=variable)

@app.route("/bs")
def functionBootStrap():
    return render_template('bootstrap.html')


# app = Flask(__name__)
# print(type(app))
# print(app)

app.run(debug=True)




