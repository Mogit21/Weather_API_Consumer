from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the variables
api_key = os.getenv("API_KEY")
test_user = os.getenv("TEST_USER")
test_password = os.getenv("TEST_PASSWORD")



app = Flask(__name__)

# MySQL Configuration
app.config["MYSQL_DATABASE_USER"] = "your_username"
app.config["MYSQL_DATABASE_PASSWORD"] = "your_password"
app.config["MYSQL_DATABASE_DB"] = "flask_weather_app"
app.config["MYSQL_DATABASE_HOST"] = "localhost"

mysql = MySQL(app)

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        # api_key = "key"  # Replace with your Weatherstack API key
        base_url = "http://api.weatherstack.com/current"
        params = {"access_key": api_key, "query": city}

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            weather_data = response.json()

            # Ensure the response contains the expected data
            if 'current' in weather_data:
                weather_data = weather_data['current']
                save_weather_to_db(city, weather_data)
            else:
                weather_data = {"error": "Could not fetch weather data for this city."}

        except requests.exceptions.RequestException as e:
            weather_data = {"error": f"Could not fetch weather data: {e}"}

    return render_template("weather.html", weather_data=weather_data)


def save_weather_to_db(city, weather_data):
    conn = mysql.connect()
    cursor = conn.cursor()

    query = """
    INSERT INTO weather_logs (city, temperature, description)
    VALUES (%s, %s, %s)
    """
    temperature = weather_data.get("temperature", "N/A")
    description = weather_data.get("weather_descriptions", ["N/A"])[0]

    cursor.execute(query, (city, temperature, description))
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    app.run(debug=True)
