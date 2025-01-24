from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        api_key = "cd652d6138424cab4cc131f0b2418ad2"  # Replace with your Weatherstack API key
        base_url = "http://api.weatherstack.com/current"
        params = {"access_key": api_key, "query": city}

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            weather_data = response.json()

            # Ensure the response contains the expected data
            if 'current' in weather_data:
                weather_data = weather_data['current']
            else:
                weather_data = {"error": "Could not fetch weather data for this city."}

        except requests.exceptions.RequestException as e:
            weather_data = {"error": f"Could not fetch weather data: {e}"}

    return render_template("weather.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
