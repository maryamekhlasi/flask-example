from flask import Flask
import urllib.request
application = Flask(__name__)

instanceid = urllib.request.urlopen('http://44.197.248.209/latest/meta-data/instance-id').read().decode()

@application.route('/')
def hello_world():
	return instanceid
