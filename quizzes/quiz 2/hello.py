from flask import Flask,request
import json

app= Flask(__name__)
user = {}
uid=1
@app.route("/")
def hello():
    return "hello world!"

@app.route('/users', methods=['POST'])
def users():
    if request.method == 'POST':
        name=request.form["name"]
        global user
        global uid
        user[uid]=name
        uid=uid+1
        #return json.dumps({"name":name})
        return json.dumps({'id':uid-1,'name':name}),201


@app.route("/users/<userid>")
def userid(userid):
	assert userid==request.view_args['userid']
	global user
	if (int(userid)<1) or (int(userid)>=uid):
		return json.dumps({"error":"invalid userid"})
	return json.dumps({"id":int(userid),"name":user[int(userid)]})


@app.route("/users/<userid>",methods=['DELETE'])
def deluser(userid):
	assert userid==request.view_args['userid']
	global user
	try:
		del user[int(userid)]
	except KeyError:
		return json.dumps({"msg":"key not found"}),204
	return json.dumps({"msg":"deleted"}),204
