from flask import Flask, render_template, request, jsonify
from serpapi import GoogleSearch

app = Flask(__name__)

# Function to perform a Google search using SerpApi
def search_internet(query):
    params = {
        "q": query,
        "api_key": "74c956e3dc2cf3b3486f7552e213022bf6a06bf1b2cb4e012b75db28143c041e"  # Replace with your SerpApi key
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    # Check if 'organic_results' is in the response
    if 'organic_results' in results:
        return results['organic_results']
    else:
        return []  # Return an empty list if no organic results are found

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        results = search_internet(query)
        return render_template('search_results.html', results=results, query=query)
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    results = search_internet(query)
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)
