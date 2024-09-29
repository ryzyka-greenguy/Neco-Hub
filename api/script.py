from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

GITHUB_JSON_URL = 'https://raw.githubusercontent.com/ryzyka-greenguy/Neco-Hub/refs/heads/main/script.json'

def load_scripts():
    response = requests.get(GITHUB_JSON_URL)
    response.raise_for_status()
    return response.json()

@app.route('/api/script/search', methods=['GET'])
def search_scripts():
    query = request.args.get('q', '').lower()
    scripts = load_scripts()
    results = [script for script in scripts if query in script['name'].lower()]
    
    return jsonify(results)

# Vercel will use this function to run your app
if __name__ == "__main__":
    app.run()
