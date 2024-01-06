import jwt
import datetime 
import Manager

def __init__(self):
	sys.path.append(self)

secret_key = "Thesuperdupersecretkeybecausenocryptomoduleisinstalled"

def genToken(username):

	token = jwt.encode({'user':username, 'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes = 15)},secret_key)

	return token
	


def validate(token):
	try:
		data = jwt.decode(token, key = secret_key, algorithms = ['HS256',])
		return data
	except:
		return False

