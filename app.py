from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hh")
def harry():
    return "hhhhhhhhhhhhhhh!"

# app = Flask(__name__)
# print(type(app))
# print(app)


app.run(debug=True)

