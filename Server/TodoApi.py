import sys 
from flask import Flask
from flask_restful import Api, Resource, reqparse
import Manager

def __init__(self):
	sys.path.append(self)

app = Flask(__name__)
api = Api(app)

class Registration(Resource):
	#registers user 
	def put(self):
		data = reqparse.RequestParser()
		data.add_argument("Username", type = str, required = True)
		data.add_argument("Password", type = str, required = True)
		userData = data.parse_args()
		if Manager.checkIfPossible(userData["Username"]) == True:
			return Manager.addUser({userData["Username"]:userData["Password"]})

		else:
			return {"message":"Username already exists"}


class Login(Resource):
	#checks for credentials and passes token
	def put(self):
		data = reqparse.RequestParser()
		data.add_argument("Username", type = str, required = True)
		data.add_argument("Password", type = str, required = True)
		userData = data.parse_args()
	
		return Manager.checkUser({userData["Username"]:userData["Password"]})


class Todo(Resource):
	def get(self):
		data = reqparse.RequestParser()
		data.add_argument("token", type = str, required = True)
		tokenDict = data.parse_args()
		token = tokenDict.get("token")
		
		if Manager.validate(token) == False:
			return {"message":"Token has expired"}
		else:
			return Manager.getData(Manager.validate(token))


	def put(self):
		data = reqparse.RequestParser()
		data.add_argument("token", type = str, required = True)
		data.add_argument("text", type = str, required = True)

		parsedData = data.parse_args()

		token = parsedData.get("token")
		text = parsedData.get("text")

		if Manager.validate(token) == False:
			return {"message":"Token has expired"}
		else:
			Manager.addTodo(Manager.validate(token),text)


	def delete(self):
		data = reqparse.RequestParser()
		data.add_argument("token", type = str, required = True)
		data.add_argument("target", type = int, required = True)

		parsedData = data.parse_args()

		token = parsedData.get("token")
		target = parsedData.get("target")

		if Manager.validate(token) == False:
			return {"message":"Token has expired"}
		else:
			Manager.delTodo(Manager.validate(token),target)


	def patch(self):
		data = reqparse.RequestParser()
		data.add_argument("token", type =str, required = True)
		data.add_argument("target", type = int, required = True)

		parsedData = data.parse_args()

		token = parsedData.get("token")
		target = parsedData.get("target")

		if Manager.validate(token) == False:
			return {"message":"Token has expired"}
		else:
			Manager.changeStatus(Manager.validate(token),target)

api.add_resource(Registration, "/register")
api.add_resource(Login,"/login")
api.add_resource(Todo,"/")



if __name__ == "__main__":
	app.run(debug=True)



