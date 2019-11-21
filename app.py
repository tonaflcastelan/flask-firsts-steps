from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'First Store',
        'items': [
            {
                'name': 'Item 1',
                'price': 11.11
            },
            {
                'name': 'Item 2',
                'price': 43.12
            }
        ]
    }
]
# @app.route('/') # 'http://localhost'
# def home():
#     return "Hello, Flask!"

# POST - receive data
# GET - send data

@app.route('/') # 'http://localhost'
def home():
    return render_template('index.html')

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store nof found it'})
    # Iterate osver stores
    # If the store name matches, return it
    # If none match, return an error message


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def crate_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'}) 

app.run(port=5000)
