#dbs prediction - v2

from flask import Flask, render_template, request
import joblib

modelPKL = joblib.load("DBS_SingDollar.pkl")

app = Flask(__name__)
# flask framwork as is
# must have double underscore

@app.route("/",methods=["GET","POST"])
# when you run the program it will run the function "route"

def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    return(render_template("main.html"))

@app.route("/dbs",methods=["GET","POST"])
def dbs():
    return(render_template("dbs.html"))

@app.route("/DBSresult",methods=["GET","POST"])
def DBSresult():
    q = float(request.form.get("q")) # front end is q?? back end r?; cast it as float
    print(q)
    r = modelPKL.predict([[q]]) # back end
    print(r)
    return(render_template("DBSresult.html", r=r))
     #first r is front, second r is back end

if __name__ == "__main__":
    app.run(port=5320)
    

