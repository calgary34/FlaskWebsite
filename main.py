from flask import Flask, redirect, url_for, render_template, request,session
import datetime
import random
from random import randint
app=Flask(__name__)
app.secret_key="hello123"
def leapyear(year):
    year=int(year)
    if year%4==0 and year%100!=0 and year%400!=0:
        return True
    elif year%4==0 and year%400==0:
        return True
    else:
        return False
def pythagoreantriple(n,m):
    
    if m>n and n>0 and m>0:
        return {"a":(m**2)-(n**2),"b":2*m*n,"c":(n**2)+(m**2)}
    else:
        pythagoreantriple(randint(1,10),randint(1,10))

def intify(x):
    if x==None:
        return 0
    else:
        return int(x)
@app.route("/")
def home():
    name=session.get('name')
    return render_template("index.html",name=name)
@app.route("/name/", methods=["POST", "GET"])
def name():
    if request.method == "POST":
        session.permanent = True
        postreq = request.form["nm"]
        mylast = request.form["lnm"]
        if name in session:
            session["name"] = postreq
        return redirect(url_for("yourname", fname=postreq,lname=mylast))
    else:
	    return render_template("name.html")
@app.route("/yourname/<fname>/<lname>/")
def yourname(fname,lname):
    return f"<h1>Hello {fname} {lname}</h1>"
@app.route("/redirected/")
def redirected():
    return render_template("redirected.html",no_params=True)
@app.route("/redirect/")
def redirect1():
    return redirect(url_for("redirected"))
@app.route("/template/")
def template1():
    return render_template("template.html",no_params=True)
@app.route("/template/<x>/")
def template(x):
    return render_template("template.html",x=x,no_params=False)
@app.route('/visits/')
def visits():
    if 'visits' in session:
        session.permanent = True
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
    return render_template("visits.html",count=session.get('visits'),clearcount=session.get('clearcount'))

@app.route('/clear-visits/')
def delete_visits():
    session.pop('visits', None) # delete visits
    if bool('clearcount' in session)==False:
        session['clearcount'] = 1
    else:
        session['clearcount'] = intify(session.get('clearcount')) + 1  # reading and updating session data
    
    return "Number of visits cleared; number of times you cleared view count is {}.".format(str(session.get('clearcount')))
@app.route("/datetime/")
def date():
    return "<h1>The time is {}</h1>".format(datetime.datetime.now())

@app.route('/math/pythagorean/')
def pythagorean_triple():
    triple=pythagoreantriple(randint(1,10),randint(1,10))
    while triple==None:
      triple=pythagoreantriple(randint(1,10),randint(1,10))
    a=triple["a"]
    b=triple["b"]
    c=triple["c"]
    return render_template("pythagoreantriple.html",a=a,b=b,c=c)
@app.route('/math/')
def math_tools():
    return render_template("mathtool.html")
@app.route('/leapyear/<year>/')
def leap_year_param(year):
  leap=leapyear(year)
  print(str(leap))
  txt=""
  if leap==True:
    txt="is a leap year."
  else:
    txt="is not a leap year."
  return render_template("leapyear.html",year=str(year),txt=txt)
@app.route('/leapyear/')
def leap_year_no_param():
  return render_template("leapyear.html")
if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # Establishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)