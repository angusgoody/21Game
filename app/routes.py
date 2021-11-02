"""
Routes.py
For defining HTTP routes for the app

26/10/21
"""

from app import app, logic
from flask import jsonify, request, render_template


# Index route
@app.route('/')
def index():
	return render_template('index.html')

# Second route
@app.route('/second')
def second():
	return render_template('second.html')


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
