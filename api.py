import time
from flask import Flask

app = Flask(__name__, static_folder='client/build', static_url_path='')

@app.route('/api')
def Welcome():
    return "Welcome to the API!!!"

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}
	
@app.route('/')
def index():
	return app.send_static_file('index.html')
	
if __name__ == '__main__':
    app.run(host='0.0.0.0')