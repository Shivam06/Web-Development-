from flask import Flask, render_template, request, url_for
app = Flask(__name__)
wsgi_app = app.wsgi_app

@app.route('/', methods = ['GET', 'POST'])
def index():
	if request.method == 'GET':
		css_url = url_for('static', filename='css/main.css')
		return render_template('index.html', css_url = css_url)


@app.route('/update')
def update():
	return render_template('update.html')

if __name__ == "__main__":
	app.run()
	"""HOST = os.environ.get('SERVER_HOST','localhost')
	try:
		PORT = int(os.environ.get('SERVER_PORT', '5555'))
	except:
		PORT = 5555 
	app.run(HOST, PORT)"""