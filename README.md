# Flask Weather App 🌦️

This is a simple weather application built with Flask. It allows users to fetch and display the current weather for any city using the Weatherstack API. The app also logs weather data into a MySQL database for record-keeping.

## Features

- Fetch current weather data using the [Weatherstack API](https://weatherstack.com/).
- Store weather data (city, temperature, and description) in a MySQL database.
- Form-based input for city names.
- Flask testing with `pytest` and API mocking using `pytest-mock`.

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/flask-weather-app.git
   cd flask-weather-app
   ```
2. **Set Up a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```
4. **Set Up Environment Variables** Create a .env file in the root directory and add the following:


API_KEY=your_weatherstack_api_key
TEST_USER=username
TEST_PASSWORD=password
5. **Set Up the Database**

Install MySQL and create the required databases:
~~~~sql
CREATE DATABASE flask_weather_app;
CREATE DATABASE test_flask_weather_app;
~~~~
Set up the weather_logs table:
~~~~sql
USE flask_weather_app;
CREATE TABLE weather_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(255),
    temperature VARCHAR(255),
    description VARCHAR(255),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
~~~~
6. **Run the Application**


python app.py
7. **Access the App Open your browser and visit: http://localhost:5000**

Testing
Run Tests

bash
Copy
Edit
pytest test_app.py
What’s Tested

Home page loads successfully.
Weather API mocking to test POST requests without hitting the actual API.
File Structure
bash
Copy
Edit
flask-weather-app/
│
├── app.py                  # Main application
├── test_app.py             # Test cases for the app
├── templates/
│   └── weather.html        # HTML template for the app
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
└── README.md               # Documentation
API Key Management
The API key for Weatherstack is stored in the .env file for security.
Make sure the .env file is included in .gitignore to prevent exposing secrets.
Future Enhancements
Add user authentication to log personalized weather searches.
Implement pagination for weather logs.
Dockerize the application for easier deployment.
Contributing
Feel free to fork the repository and submit pull requests. Contributions are welcome!

License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

### **Next Steps**
1. Add the `.env` handling in your `test_app.py` as described above.
2. Create the `README.md` file in your project directory and commit it to GitHub.
