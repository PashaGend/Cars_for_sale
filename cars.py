from flask import Flask
import json
import cars_db
from flask import request
from prometheus_client import make_wsgi_app, Counter, Histogram
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)
# Create counter metric to track number of requests for all cars list
all_cars_requests = Counter('all_cars_requests','Number of requests for all cars')
app.wsgi_app=DispatcherMiddleware(app.wsgi_app,{'/metrics': make_wsgi_app()})

@app.route('/')
def hello_world():
    return 'Welcome to Flask API!!!!'

@app.route('/cars')
def get_all_tasks():
     all_cars_requests.inc()
     return json.dumps(cars_db.all_cars())

@app.route('/cars/<int:car_id>', methods=['GET'])
def get_specific_task(car_id):
     return json.dumps(cars_db.specific_car(car_id))

@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_one_task(car_id):
     return json.dumps(cars_db.delete_car(car_id))

@app.route('/cars', methods=[ 'POST'])
def add_new_task():
     data = request.get_json()  # Extract data from the request
     return json.dumps(cars_db.add_car(data))  # Pass data to add_task function

# @app.route('/cars', methods=['PUT'])
# def update_tasks(car_id):
#      return json.dumps(car_id)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)