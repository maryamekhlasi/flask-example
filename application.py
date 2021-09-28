from flask import Flask
import boto3
application = Flask(__name__)


ec2 = boto3.client('ec2')
response = ec2.describe_instances()



@application.route('/')
def hello_world():
	return response["Reservations"][0]["Instances"][0]["InstanceId"]
