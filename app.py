from db.models import *
from flask import Flask,request,flash,render_template,session,redirect,url_for
from datetime import datetime
import re

app = Flask(__name__)
app.secret_key = "secret key"

@app.route("/home")
def home():
    return render_template("home.html", Username= session['Username'])

@app.route("/login", methods= ['GET','POST'])
def login():
    flash('')
    if request.method =='POST' and 'Username' in request.form and 'Password' in request.form:
        Username = request.form["Username"]
        Password = request.form["Password"]
        date_time = datetime.now()
        day = date_time.strftime("%A")

        
        mycursor.execute('SELECT * FROM interninfo WHERE username=%s AND password=%s',(Username,Password))
        userinfo = mycursor.fetchone()

        if userinfo:
            session['loggedin'] = True 
            session['Username'] = Username
            flash('Logged in successfully!')
        
            mycursor.execute(f"""UPDATE login SET {day} = %s WHERE username=%s""",(date_time, Username))
            mydb.commit()
            return render_template('home.html')
        else:
            flash('Incorrect username/password.Try again!')
    return render_template("login.html")



@app.route("/SignUp" , methods=["GET", "POST"])
def SignUp():
    flash('')
    if request.method == "POST":
        Name = request.form.get("Name")
        Email = request.form.get("Email")
        Username = request.form.get("Username")
        Phone_number = request.form.get("Phone_number")
        Password = request.form.get("Password")
        Section = request.form.get("Section")
        Role = 'Intern'
        date_joined = datetime.now()

        mycursor.execute("SELECT * FROM interninfo WHERE email = %s",(Email,))
        account = mycursor.fetchone()

        if account:
            flash('Account already exists !')
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", Email):
            flash('Invalid email address !')    
        elif not Username or not Password or not Email:
            flash('Please fill out the form !')
        else:
              sql = "INSERT INTO interninfo (Name,Username,Password,Phone_number,Email,date_joined,Section,Role) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
              val = (Name,Username,Password,Phone_number,Email,date_joined,Section,Role)
              mycursor.execute(sql,val)
              mydb.commit()
              
              dat = "INSERT INTO login (Username,Monday,Tuesday,Wednesday,Thursday,Friday) VALUES(%s,%s,%s,%s,%s,%s)"
              num = (Username,'','','','','')
              mycursor.execute(dat,num) 
              mydb.commit()

              log = "INSERT INTO logout (Username,Monday,Tuesday,Wednesday,Thursday,Friday) VALUES(%s,%s,%s,%s,%s,%s)"
              out = (Username,'','','','','')
              mycursor.execute(log,out) 
              mydb.commit()

              flash('You have successfully registered !')

    elif request.method == 'POST':
        flash('Please fill out the form !')

    return render_template("SignUp.html")    


      
@app.route("/logout", methods=["GET","POST"])
def logout():
    flash("")
  
    Username = session['Username']
    date_time = datetime.now()
    day = date_time.strftime("%A")
   
   
    mycursor.execute(f"""UPDATE logout SET {day} = %s WHERE username=%s""",(date_time, Username))
    mydb.commit()
    session.pop('loggedin', None)
    session.pop('username', None)
    flash('Logged out successfully!')
        
    return render_template('login.html')


    
   
   


    #flash("You have been logged out!", )
    #return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
