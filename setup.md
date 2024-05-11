# Setup Instructions

## Deploying the Application

1. **Clone the Repository**: Clone the GitHub repository containing the Flask application to your local machine:

    ```
    git clone https://github.com/KajalSund/url_hashing_system.git
    ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using pip:

    ```
    cd url-hashing-system
    pip install -r requirements.txt
    ```

3. **Update MongoDB Connection String**: Open the `main.py` file and replace the placeholder values in the `MONGO_URI` variable with your actual MongoDB Atlas credentials.

4. **Run the Application**: Start the Flask application by running the following command:

    ```
    python main.py
    ```

   This will start the application locally on your machine.

## Using the Application

1. **Generating Hashed URLs**: To generate a hashed URL for a long URL with UTM tracking parameters, send a POST request to the `/generate` endpoint with a JSON body containing the original URL:

    ```
    POST /generate
    Content-Type: application/json

    {
        "url": "https://example.com/?utm_source=google&utm_medium=cpc&utm_campaign=summer_sale"
    }
    ```

2. **Accessing Original URLs**: To access the original URL corresponding to a hashed URL, send a GET request to `/<hashed_url>`.

3. **Tracking Clicks**: To track clicks on a hashed URL, send a GET request to `/track/<hashed_url>/<token>`.

## Running Unit Tests

1. **Install Pytest**: If you haven't already installed pytest, install it using pip:

    ```
    pip install pytest
    ```

2. **Run Tests**: Navigate to the project directory and run the pytest command to execute the unit tests:

    ```
    pytest
    ```

   This will run all the unit tests defined in the test file and display the results.


