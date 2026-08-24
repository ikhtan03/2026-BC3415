#dbs prediction - v2

from flask import Flask, render_template, request

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

if __name__ == "__main__":
    app.run()

