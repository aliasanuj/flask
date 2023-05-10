from flask import Flask, render_template, request
import mysql.connector
import datetime

app = Flask(__name__)

@app.route("/")
def functionIndex():
    return render_template('index.html')

@app.route("/about")
def functionAbout():
    return render_template('about.html')

@app.route("/bs")
def functionBootStrap():
    return render_template('bootstrap.html')

'''DB connection'''
db_config = {
    'host':"localhost",
    'user':"root",
    'password':"Switch@2023",
    'database':"databasename01"
}
@app.route("/contact", methods=['GET','POST'])
def functionContact():
    if (request.method=='POST'):
        firstName = request.form['firstName']
        Email = request.form['Email']
        phoneNo = request.form['phoneNo']
        createdTime = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        message = request.form['message']
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        query = "INSERT INTO flaskContact (firstName, Email, phoneNo, createdTime, message)  values (%s,%s,%s,%s,%s)"
        values = (firstName, Email, phoneNo, createdTime, message)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()
    return render_template('contact.html')

@app.route("/post")
def functionPost():
    return render_template('post.html')


# app = Flask(__name__)
# print(type(app))
# print(app)

app.run(debug=True)




