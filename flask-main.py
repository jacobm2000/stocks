from main import *
from flask import Flask, render_template,request,flash

app=Flask(__name__)

@app.route("/home",methods=["PoST","GET"])

def home() :
    if request.method=="POST":
        output,price=(getPrice( str(request.form["t"])))
        return render_template("home.html", output=output,price=price)
    else:
        return render_template("home.html")


if __name__== "__main__":
    app.run(debug=False)