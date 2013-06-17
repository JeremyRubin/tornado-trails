#Brought to you by Jeremy Rubin, 2013
from App import *
class Password(object):
	def __init__(self, password, user=None, salt=str(os.urandom(32).encode('hex'))):
		self.password = password
		self.salt = salt
		self.hashed = hashlib.sha512(password+salt).hexdigest()
		self.passdict = {"username":user, "hashed":self.hashed}
	def value(self):
		return self.hashed
	def same(self,other):
		return self.password == other.password

class AddUserHandler(BaseHandler):
	def get(self):
		self.render("main.html")
	@tornado.web.asynchronous
	@tornado.gen.engine
	def post(self):
		username = self.get_argument("username")
		password = Password(self.get_argument("password"),user=username)
		verify_password = Password(self.get_argument("verify_password"))
		if not password.same(verify_password):
			raise tornado.web.HTTPError(500)

		user = {"username":username, "salt":password.salt}
		use = {"username":username, "salt":password.salt}
		
		cursor = self.db.users.find(user).limit(1)
		user_response = yield motor.Op(cursor.to_list)
		if user_response:
			raise tornado.web.HTTPError(500)

		user_success = yield motor.Op(self.db.users.insert, user)
		password_success = yield motor.Op(self.db.passwords.insert,
										  password.passdict)
		self.set_secure_cookie('user',tornado.escape.json_encode(use))
		self.redirect("/")
			
class LoginHandler(BaseHandler):
	def get(self):
		self.redirect("/")
	@tornado.web.asynchronous
	@tornado.gen.engine
	def post(self):
		username = self.get_argument("username")
		password = self.get_argument("password")

		cursor = self.db.users.find({"username":username},{"_id":0}).limit(1)
		user = yield motor.Op(cursor.to_list)
		if not user:
			self.redirect("/login")

		password = Password(password, salt=user[0]["salt"])

		cursor = self.db.passwords.find({"username":username},{"_id":0}).limit(1)
		passdict = yield motor.Op(cursor.to_list)

		if passdict[0]["hashed"] == password.hashed:
			self.set_secure_cookie('user',tornado.escape.json_encode(user))
			self.redirect("/")
		else:
			self.redirect("/login")

class LogoutHandler(BaseHandler):
	def get(self):
		self.clear_cookie("user")
		self.redirect("/")