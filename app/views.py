from app import app
from flask import Flask, abort, request, jsonify, g, url_for, render_template

@app.route('/')
def home():
    return "I'm home"

@app.route('/signup')
def signup():
    return render_template('signup.html')
