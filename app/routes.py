"""
Routes.py
For defining HTTP routes for the app

26/10/21
"""

from app import app, logic
from flask import jsonify, request


# Index route
@app.route('/')
def index():
	return jsonify(message="Hello world")


# Name route (GET)
@app.route('/name')
def name():
	# Simply return a JSON dictionary name: "Angus"
	return jsonify(name=logic.getName())


# Play route (POST)
@app.route('/play', methods=['POST'])
def play():
	data = request.json
	return jsonify(scoreList=logic.playMove(int(data["playerCount"]), int(data["score"])))
