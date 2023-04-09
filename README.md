# URL Shortener

This is a Flask-based web application that allows users to shorten URLs.

## Technologies Used
- Flask
- Jinja
- Bootstrap
- JSON

## Demo Project Overview
The URL Shortener app allows users to submit a long URL and receive a shortened URL in return. The app keeps a JSON file of all of the URLs that have been submitted and their corresponding short URLs.

## Installation
1. Install Flask and Pipenv.
2. Clone the repository.
3. Run `pipenv install` in the root directory to install the necessary dependencies.

## Usage
1. Run `pipenv shell` in the root directory to activate the virtual environment.
2. Run `flask run` to start the server.
3. Navigate to http://localhost:5000/ to access the URL Shortener app.

## Functionality
- Submit a long URL and receive a shortened URL in return.
- The app keeps a JSON file of all of the URLs that have been submitted and their corresponding short URLs.
- The app allows for file uploads from users.
- The app works with static files.
- Custom error pages are displayed to users.
- Sessions are implemented.
- A JSON API is provided.
- The app uses template blocks and base templates.
- The app is templated with Bootstrap.

## Testing
To test the app, run `pytest` in the root directory.
