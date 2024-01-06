import sys
import sqlite3
import Manager

def __init__(self):
	sys.path.append(self)


def addUser(username,password):
	dataTuple = (username,password,)
	connection = sqlite3.connect("Database.db")
	cursor = connection.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS Users(id integer primary key autoincrement,
					Username text,
					Password text,
					Status integer)""")
	cursor.execute("""INSERT INTO Users(Username,Password) VALUES (?,?)""", dataTuple)
	connection.commit()
	connection.close()

	return {"Message":"User Added"}

def checkUser(username,password):
	connection = sqlite3.connect("Database.db")
	cursor = connection.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS Users(id integer primary key autoincrement,
						Username text,
						Password text,
						Status integer)""")
	cursor.execute("SELECT * FROM Users WHERE Username = '{}'".format(username))
	userData = cursor.fetchone()
	connection.commit()
	connection.close()
	if userData == None:
		return {"message":"Invalid Username"}
	else:
		return Manager.checkPassword(userData,username,password)


def getData(username):
	connection = sqlite3.connect("Database.db")
	cursor = connection.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS Todos(id integer primary key autoincrement, Username text, Todo text, Status integer)")
	cursor.execute("SELECT * FROM Todos WHERE Username = '{}' ORDER BY id DESC limit -10".format(username))
	userTodoList = cursor.fetchmany(10)
	connection.commit()
	connection.close()

	return Manager.sendData(userTodoList)


def addTodo(username,text):
	tupleText = (username,text,0,)
	connection = sqlite3.connect("Database.db")
	cursor = connection.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS Todos(id integer primary key autoincrement, Username text, Todo text, Status integer)")
	cursor.execute("INSERT INTO Todos(Username,Todo,Status) VALUES (?,?,?)",tupleText)
	connection.commit()
	connection.close()



def searchTarget(username):
	connection = sqlite3.connect("Database.db")
	cursor = connection.cursor()
	cursor.execute("SELECT id FROM Todos WHERE Username = '{}' ORDER BY id DESC limit -10".format(username))
	userTodoList = cursor.fetchmany(10)
	connection.commit()
	connection.close()

	return userTodoList

def delTarget(target):
	connection = sqlite3.connect("Database.db")
	cursor = connection.cursor()
	cursor.execute("DELETE FROM Todos WHERE id = '{}'".format(target))
	connection.commit()
	connection.close()

def changeStatus(target):
	connection = sqlite3.connect("Database.db")
	cursor = connection.cursor()
	cursor.execute("UPDATE Todos SET Status = 1 WHERE id = '{}'".format(target))
	connection.commit()
	connection.close()


def checkIfPossible(username):
	connection = sqlite3.connect("Database.db")
	cursor = connection.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS Todos(id integer primary key autoincrement, Username text, Todo text, Status integer)")
	cursor.execute("SELECT * FROM Todos WHERE Username = '{}'".format(username))
	answer = cursor.fetchall()
	connection.commit()
	connection.close()
	if answer == []:
		return True
	else:
		return False
