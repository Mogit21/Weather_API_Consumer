from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        api_key = "your_api_key"  # Replace with your OpenWeatherMap API key
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": api_key, "units": "metric"}

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            weather_data = response.json()
        except requests.exceptions.RequestException as e:
            weather_data = {"error": f"Could not fetch weather data: {e}"}

    return render_template("weather.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
