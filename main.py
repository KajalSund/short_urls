from flask import Flask, request, jsonify
from pymongo import MongoClient
import hashlib
import uuid


app = Flask(__name__)
# Connect to MongoDB
#client = MongoClient('mongodb://localhost:27017/')
MONGO_URI = "mongodb+srv://kajalsund9:SXzizCoCxv5OBm91@cluster0.gmrg5ha.mongodb.net/url_hashing?ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(MONGO_URI)
db = client['url_hashing']


# Define collection for hashed URLs
hashed_urls_collection = db['hashed_urls']


@app.route('/generate', methods=['POST'])
def generate_hash():
    data = request.json
    url = data.get('url')
    if url:
        # Check if the URL already exists in the database
        existing_url = hashed_urls_collection.find_one({'original_url': url})
        if existing_url:
            # If the URL already exists, return the existing hashed URL
            hashed_url = existing_url['hashed_url']
            token = existing_url['token']
            return jsonify({'hashed_url': hashed_url, 'token': token}), 200
        else:
            # Generate unique token
            token = str(uuid.uuid4())
            # Hash the URL
            hashed_url = hashlib.sha256(url.encode()).hexdigest()
            # Store hashed URL and token in MongoDB
            hashed_urls_collection.insert_one({'hashed_url': hashed_url, 'original_url': url, 'token': token})
            return jsonify({'hashed_url': hashed_url, 'token': token}), 200
    else:
        return jsonify({'error': 'URL not provided'}), 400


@app.route('/<hashed_url>', methods=['GET'])
def get_original_url(hashed_url):
   hashed_url_data = hashed_urls_collection.find_one({'hashed_url': hashed_url})
   if hashed_url_data:
       original_url = hashed_url_data['original_url']
       return jsonify({'original_url': original_url}), 200
   else:
       return jsonify({'error': 'URL not found'}), 404


@app.route('/track/<hashed_url>/<token>', methods=['GET'])
def track_click(hashed_url, token):
   hashed_url_data = hashed_urls_collection.find_one({'hashed_url': hashed_url, 'token': token})
   if hashed_url_data:
       # Log click or perform tracking action
       return jsonify({'message': 'Click tracked successfully'}), 200
   else:
       return jsonify({'error': 'Unauthorized access'}), 401


if __name__ == '__main__':
   app.run(debug=True)



