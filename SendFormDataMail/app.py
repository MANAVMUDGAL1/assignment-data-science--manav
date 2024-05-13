from flask import Flask,render_template,url_for,request
from flask_mail import Mail,Message
import os
import json



app=Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='mail id'
app.config['MAIL_PASSWORD']='password'
app.config['MAIL_USE_TLS']=False
app.config["MAIL_USE_SSL"]=True

mail=Mail(app)

app

@app.route('/')
def home():
    return render_template('web.html')

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/userdata')
def userdata():
    return render_template('userdata.html')

@app.route('/submitdata',methods=['GET','POST'])
def submitdata():
    if request.method == 'POST':
        profession =request.form['profession']
        name =request.form['name']
        email=request.form['email']
        password=request.form['password']
        user_data={"user_profession":profession,"user_name":name,"user_email":email,"user_password":password}
        msg=Message ("i am sending users data using flask",sender='sender email',recipients=['reciever email'])
        msg.body=json.dumps(user_data)
        mail.send(msg)
        return user_data 


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=2525,debug=True)
