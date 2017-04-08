from flask import Flask

app = Flask(__name__)

wsgi_app = app.wsgi_app
# DO NOT TOUCH IT!

from routes import *

# Launching our server
if __name__ == "__main__":
	import os
	HOST = os.environ.get('SERVER_HOST', 'localhost')
	try:
		PORT = int(os.environ.get('SERVER_PORT','5555'))
	except:
		PORT = 5555
	app.run(HOST, PORT)
