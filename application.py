from flask import Flask
import requests
application = Flask(__name__)


instanceid = urllib.request.urlopen('http://169.254.169.254/latest/meta-data/instance-id').read().decode()

@application.route('/')
def hello_world():
	return instanceid
