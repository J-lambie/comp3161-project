from app import app
from flask import Flask, abort, request, jsonify, g, url_for, render_template

@app.route('/')
def home():
    return render_template("home.html")