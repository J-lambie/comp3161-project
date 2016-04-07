from app import app
from flask import Flask, abort, request, jsonify, g, url_for, render_template

@app.route('/')
def home():
    return "I'm home"