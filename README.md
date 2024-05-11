# URL Hashing System with MongoDB

This is a Flask application that implements a URL hashing system with MongoDB as the database. The application allows users to generate hashed URLs for long URLs with UTM tracking parameters, and provides functionality for accessing original URLs from hashed ones and tracking clicks.

## Features

- **Generate Hashed URLs**: Users can submit long URLs with UTM tracking parameters to the `/generate` endpoint, which generates a unique hashed URL and token and stores them in the MongoDB database.

- **Access Original URLs**: Users can access the original URL corresponding to a hashed URL by making a GET request to `/<hashed_url>`. If the hashed URL exists in the database, the original URL is returned in the response.

- **Track Clicks**: Click tracking functionality is provided through the `/track/<hashed_url>/<token>` endpoint. Users can track clicks on hashed URLs by providing the hashed URL and token in the URL path.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/KajalSund/url_hashing_system.git
    cd url-hashing-system
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Update MongoDB connection string:

    Replace `<username>`, `<password>`, `<cluster>`, and `<database>` in the `MONGO_URI` variable in `main.py` with your MongoDB Atlas credentials.

4. Run the application:

    ```
    python main.py
    ```

## Usage

### Generating Hashed URLs

To generate a hashed URL for a long URL with UTM tracking parameters, send a POST request to the `/generate` endpoint with a JSON body containing the original URL:


