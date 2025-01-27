import pytest
from flask import template_rendered
from app import app
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the variables
TEST_USER = os.getenv("TEST_USER")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["MYSQL_DATABASE_USER"] = TEST_USER
    app.config["MYSQL_DATABASE_PASSWORD"] = TEST_PASSWORD
    app.config["MYSQL_DATABASE_DB"] = "test_flask_weather_app"
    app.config["MYSQL_DATABASE_HOST"] = "localhost"
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Weather" in response.data  # Assuming my weather.html contains 'Weather'


def test_weather_api_mock(mocker, client):
    # Mock the requests.get call to simulate API response
    mock_response = mocker.patch("requests.get")
    mock_response.return_value.json.return_value = {
        "current": {
            "temperature": 25,
            "weather_descriptions": ["Sunny"]
        }
    }

    # Mock save_weather_to_db to prevent database interaction
    mock_save_weather = mocker.patch("app.save_weather_to_db")

    # Simulate a POST request to the Flask endpoint
    response = client.post("/", data={"city": "London"})

    # Assertions
    assert response.status_code == 200
    assert b"25" in response.data  # Check if temperature is displayed
    assert b"Sunny" in response.data  # Check if weather description is displayed
    mock_save_weather.assert_called_once_with("London", {
        "temperature": 25,
        "weather_descriptions": ["Sunny"]
    })
