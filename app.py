from flask import Flask, render_template, request
import mysql.connector
import datetime
import json
from flask_mail import Mail


app = Flask(__name__)

with open('config.json','r') as f:
    params = json.load(f)['local_URI']
with open('config.json','r') as f1:
    params1 = json.load(f1)['prod_URI']

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params1['gmail_user'],
    MAIL_PASSWORD=params1['gmail_password'],
    )

mail = Mail(app)
@app.route("/")
def functionIndex():
    return render_template('index.html', name=params1)

@app.route("/about")
def functionAbout():
    return render_template('about.html',name=params1)

@app.route("/bs")
def functionBootStrap():
    return render_template('bootstrap.html',name=params1)

@app.route("/contact", methods=['GET','POST'])
def functionContact():
    if (request.method=='POST'):
        firstName = request.form['firstName']
        Email = request.form['Email']
        phoneNo = request.form['phoneNo']
        createdTime = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        message = request.form['message']
        db = mysql.connector.connect(**params)
        cursor = db.cursor()
        query = "INSERT INTO flaskContact (firstName, Email, phoneNo, createdTime, message)  values (%s,%s,%s,%s,%s)"
        values = (firstName, Email, phoneNo, createdTime, message)
        cursor.execute(query, values)
        db.commit()
        '''this will require enable smtp'''
        # mail.send_message("new message from blog" + firstName,
        #                   sender=Email,
        #                   recipients=[params1['gmail_user']],
        #                   body="message" + "\n" + phoneNo
        #                   )

        cursor.close()
        db.close()
    return render_template('contact.html',name=params1)

@app.route("/post")
def functionPost():
    return render_template('post.html',name=params1)


# app = Flask(__name__)
# print(type(app))
# print(app)

app.run(debug=True)




