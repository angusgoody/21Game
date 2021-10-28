"""
21 Project Thing
Angus Goody
25/10/21

use the following in terminal to test GET requests...
curl http://127.0.0.1:5000/name
"""

from flask import Flask
app = Flask(__name__)
from app import routes



