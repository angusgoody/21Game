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
	return render_template('index.html.j2')

# Second route
@app.route('/queue')
def queue():
	return render_template('queue.html.j2')


# Name route (GET)
@app.route('/name')
def name():
	# Simply return a JSON dictionary name: "Angus"
	return jsonify(name=logic.getName())

# Name route (GET)
@app.route('/test')
def test():
	return render_template('tester.html.j2')


# Play route (POST)
@app.route('/play', methods=['POST'])
def play():
	data = request.json
	return jsonify(scoreList=logic.playMove(int(data["playerCount"]), int(data["score"])))
