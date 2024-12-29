from flask import Flask

import os
from flask import Flask, send_from_directory, jsonify, redirect, Response, request
from werkzeug.utils import secure_filename
from .models import db
#from icecream import ic

# SUPABASE SETUP
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

user = supabase.auth.sign_in_with_password({ "email": users_email, "password": users_password })
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'