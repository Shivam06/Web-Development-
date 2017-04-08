from flask import Flask, url_for, request, render_template
from app import app;
import sqlite3

conn = sqlite3.connect('QA.db')
def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY,title TEXT, question TEXT, answer TEXT)")
c = conn.cursor()
# server/
@app.route('/')
def hello():
	""" Renders a sample page"""
	return "<a href = '" + url_for('create') + "'>Create question</a>"

# server/create
@app.route('/create', methods=['GET', 'POST'])
def create():
	if request.method == 'GET':
		# send user the form
		return render_template('CreateQuestion.html');

	elif request.method == 'POST':
		# read form data and save it
		title = request.form['title']
		question = request.form['question']
		answer = request.form['answer']
		# Store data in data store.
		create_table()
		c.execute("INSERT INTO data(title, question, answer) VALUES(?,?,?)",(title, question, answer))
		return render_template('CreatedQuestion.html', question = question);
	else:
		return "<h2>Invalid request! </h2>";

# server/question/<title>
@app.route('/question/<title>', methods=['GET', 'POST'])
def question(title):
	if request.method == 'GET':
		# send the user the form
		c.execute("SELECT question FROM data WHERE title = ?", (title,))
		question = c.fetchone()[0]
		if ~len(question):
			return "<h2>Invalid Input</h2>"
		# Read the question from data store
		return render_template('AnswerQuestion.html', question = question)

	if request.method == 'POST':
		submittedAnswer = request.form['submittedAnswer']
		#Read answer from data source
		c.execute("SELECT question FROM data WHERE title = ?", (title,))
		question = (c.fetchone()[0],)
		c.execute("SELECT answer FROM data WHERE question = ?", question)
		answer = c.fetchone()[0]
		if submittedAnswer == answer:
			return render_template('Correct.html')
		else:
			return render_template('Incorrect.html', submittedAnswer = submittedAnswer, answer = answer)
		
	else:
		return "<h2>Invalid request</h2>"
	c.close()
	conn.close()
