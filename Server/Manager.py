import sys
import Database
import Tokenizer 
def __init__(self):
	sys.path.append(self)


def addUser(data):
	return Database.addUser(list(data)[0],data[list(data)[0]])

def checkUser(data):
	return Database.checkUser(list(data)[0], data[list(data)[0]])

def checkPassword(data,username,password):
	dataList = []

	for i in data:
		if type(i) == int:
			pass
		else:
			chars = ""
			for j in i:
				chars += str(j)

			dataList.append(chars)

	if dataList[1] == password:
		return genToken(username)

	else:
		return {"message":"Incorrect Password"}


def genToken(username):
	token = Tokenizer.genToken(username)
	return {"token":token}

def validate(token):
	return Tokenizer.validate(token)

def getData(data):
	username = data.get("user")
	
	return Database.getData(username)

def sendData(data):
	retrievedTextList = []
	retrievedStatus = []
	
	for i in data:
		chars = ""
		for j in i[2]:
			chars += j
		retrievedTextList.append(chars)

	for i in data:
		status = 0 
		status += i[3]
		retrievedStatus.append(status)

	
	values = ()

	for i in range(len(data)):
		values +=({retrievedTextList[i]:retrievedStatus[i]},)

	toSendDict = {"Data":values}

	return toSendDict

def addTodo(data,text):
	username = data.get("user")
	return Database.addTodo(username,text)



def delTodo(data,target):
	username = data.get("user")

	userTodos = Database.searchTarget(username)

	retrievedIdList = []

	for i in userTodos:
		chars = ""
		for j in i:
			chars += str(j)
		retrievedIdList.append(int(chars))

	for i in range(len(retrievedIdList)):
		if i == target - 1:
			Database.delTarget(retrievedIdList[i])
		else:
			pass



def changeStatus(data,target):
	username = data.get("user")
	userTodos = Database.searchTarget(username)
	retrievedIdList = []

	for i in userTodos:
		chars = ""
		for j in i:
			chars += str(j)
		retrievedIdList.append(int(chars))

	for i in range(len(retrievedIdList)):
		if i == target - 1:
			Database.changeStatus(retrievedIdList[i])
		else:
			pass


def checkIfPossible(username):
	return Database.checkIfPossible(username)