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

@app.route("/burglary")
def burg():
    return render_template("Burglary.html")

@app.route("/cacrimetrend")
def cacrimetrend():
    return render_template("CAcrimetrend.html")

@app.route("/crimetrend")
def crimetrend():
    return render_template("CrimeTrends.html")

@app.route("/dccrimetrend")
def dcct():
    return render_template("DCcrimetrend.html")

@app.route("/homicideml")
def homml():
    return render_template("Homicide_ml.html")

@app.route("/motor")
def motor():
    return render_template("Motor.html")

@app.route("/njcrimetab")
def njcrimetab():
    return render_template("NJ_Crime_Tab.html")

@app.route("/njcrimetrend")
def Njct():
    return render_template("NJcrimetrend.html")

@app.route("/nycrimetrend")
def nyct():
    return render_template("NYcrimetrend.html")

@app.route("/robbery")
def robbery():
    return render_template("Robbery.html")

@app.route("/usacrimetrend")
def USct():
    return render_template("USAcrimetrend.html")
    
@app.route("/decrimetrend")
def dect():
    return render_template("DEcrimetrend.html")

if __name__ == "__main__":
    app.run(debug=True)