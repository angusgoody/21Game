"""
21 Project Thing
Angus Goody
25/10/21

use the following in terminal to test GET requests...
curl http://127.0.0.1:5000/name
"""

from flask import Flask

#Setup app
app = Flask(__name__)
app.debug=True #Debug mode on

from app import routes



