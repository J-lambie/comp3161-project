from flask import Flask
import MySQLdb

HOST = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'meal_plan'

app = Flask(__name__)
mysql = MySQLdb.connect(HOST, USER, PASSWORD ,DATABASE)

import views
