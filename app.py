from flask import Flask, render_template, request
import requests
import os

app=Flask(__name__)

#Homepage route
@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    city_input = "" #city input değerini saklamak için
    weather_main = None
    icon_code = None

    if request.method == "POST":
        city = request.form.get("city")
        city_input = city #city inputu sakla

        #API key
        api_key= "5d0d495ebc8027f5ea0ec131bfe857a3"
        url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"
        response = requests.get(url)

        icon_code = None

        if response.status_code == 200:
            weather_data = response.json()
            weather_main = weather_data["weather"][0]["main"] #hava durumu tipi
            icon_code = weather_data["weather"][0]["icon"]
        else:
            weather_data = {"error":"Şehir bulunamadı."}


    return render_template("index.html", weather=weather_data, city_input=city_input, weather_main=weather_main, icon_code=icon_code)

if __name__ == "__main__":
    app.run(debug=True)