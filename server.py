import os
from flask import Flask, send_from_directory, jsonify, redirect, Response, request
from werkzeug.utils import secure_filename
from models import db
from icecream import ic
import items

app = Flask(__name__)

port = int(os.environ.get("PORT", 8000))

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fl0user:ULf8bhoGp1XS@ep-broken-paper-05736162.ap-southeast-1.aws.neon.fl0.io:5432/harvest-festival-db?sslmode=require'
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

with app.app_context():
    db.create_all()
    print("Created all tables")

@app.route('/api/newItem', methods=['POST'])
def addNewItem():
    """
    This is getting called directly from the form request.
    So we need to handle the payload and then return 
    the success value of the request.
    """
    itemId = items.create_item(request)
    ic("ItemID:",itemId)
    return jsonify(item_id = itemId), 201
    

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    items.delete_item(item_id)
    return jsonify(item_id=item_id), 200

@app.route('/api/items', methods=['GET'])
def get_all_items():
    item_list = items.get_all_items()
    ic(item_list)
    return jsonify(item_list), 200
 
@app.route('/api/bid/<int: item_id>', methods=['POST'])
def get_all_items(item_id):
    bid_result = items.create_bid(item_id) # bid_result would contain whether bid successful or fail and reason for fail.
    ic(bid_result)
    return jsonify(bid_result), 200

@app.route('/api/<path:path>', methods=['GET', 'POST'])
def serve_api(path):
    # send 200 OK
    print("API request: ", path)
    return Response(f"Hello from {path}", status=200)



@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def home():
   return send_from_directory('client/public', 'index.html')

@app.route('/<path:path>')
def all_routes(path):
    return send_from_directory('client/public', path)

if __name__ == "__main__":
    app.run(port=port)