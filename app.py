from flask import Flask, render_template, redirect, url_for


#Create an instance of flask
app=Flask(__name__)

@app.route("/")
def home2():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("index.html")
    
@app.route("/aboutus")
def aboutus():
    return  render_template("AboutUs.html")

@app.route("/aggassault")
def aggassault():
    return  render_template("AggAssault.html")

@app.route("/homicide")
def homicide():
    return  render_template("Homicide.html")

@app.route("/mvt")
def mvt():
    return  render_template("MVT.html")

@app.route("/data")
def data():
    return  render_template("crimes_data.html")

@app.route("/usmap")
def usmap():
    return  render_template("Angel.html")

@app.route("/njmap")
def njmap():
    return  render_template("Tunde.html")

@app.route("/heatmap")
def heatmap():
    return  render_template("heatmap.html")


if __name__ == "__main__":
    app.run(debug=True)