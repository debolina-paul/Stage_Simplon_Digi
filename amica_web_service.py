#python web service for amica

import json
import base64
import pymongo
dbclient = pymongo.MongoClient("mongodb://localhost:27017")
db = dbclient["amica_database"]
collection_auth = db["id_clients"]
collection_customer = db["customer"]	
collection_activity = db["activity_info"]
collection_total = db["total"]

from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
	return ("I am learning python and flask")

@app.route("/register")
def register():
	return render_template("sign_up.html")

@app.route("/auth/signup", methods=['POST'])
def auth_signup():
	base64_message = request.headers.get("Authorization").split(" ")[1]
	#print(base64_message)
	basic_auth = base64.b64decode(base64_message).decode("ascii")
	#print(basic_auth)
	name = basic_auth.split(":")[0]
	email = basic_auth.split(":")[1]
	password = basic_auth.split(":")[2]
	#print(name)
	#print(email)
	#print(password)
	
	signup_info = {'name':name, 'email':email, 'password':password}
	result = collection_auth.insert_one(signup_info)
	print(result)
	print(result.inserted_id)

	return jsonify('{"success":"true"}')
	
@app.route("/log_in")
def login():
	return render_template("log_in.html")

@app.route("/auth/login", methods=['POST'])
def auth_login():
	base64_message = request.headers.get("Authorization").split(" ")[1]
	#print(base64_message)
	basic_auth = base64.b64decode(base64_message).decode("ascii")
	#print(basic_auth)
	email = basic_auth.split(":")[0]
	password = basic_auth.split(":")[1]
	#print(email)
	#print(password)
	
	#check with the db
	query_find_user = {'email':email, 'password':password}
	match = collection_auth.find(query_find_user)
	print(match.count())
	if match.count() > 0:
		return jsonify('{"success":"true"}')
	else:
		return jsonify('{"success":"false"}')

#insert data into mongodb
@app.route("/postdata", methods=['POST'])
def postdata():
	get_collection_name = request.args.get('collection')
	content = request.get_json(silent=True)
	print(content)

	if get_collection_name == 'customer':
		collection_customer.insert_one(content)
	elif get_collection_name == 'activity':
		collection_activity.insert_one(content)
	else :
		collection_total.insert_one(content)
	
	return("request handled")
	
if __name__ == '__main__':
	app.run()
