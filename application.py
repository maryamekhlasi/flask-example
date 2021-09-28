from flask import Flask
import requests
application = Flask(__name__)


response = requests.get('http://169.254.169.254/latest/meta-data/instance-id')
instance_id = response.text

@application.route('/')
def hello_world():
	return instance_id
