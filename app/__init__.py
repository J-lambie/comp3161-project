from flask import Flask
from flask.ext.mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

import views