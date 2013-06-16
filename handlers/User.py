#Brought to you by Jeremy Rubin, 2013
from App import *
class Password(object):
	def __init__(self, password, salt=str(os.urandom(32).encode('hex'))):
		self.password = password
		self.salt = salt
		self.hashed = hashlib.sha512(password+salt).hexdigest()
	def value(self):
		return self.hashed

class AddUserHandler(BaseHandler):
	def get(self):
		self.render("main.html")
	@tornado.web.asynchronous
	@tornado.gen.engine
	def post(self):
		username = self.get_argument("username")
		password = Password(self.get_argument("password"))

		user = {"username":username, "salt":password.salt}

		self.db.users.find(user, limit=1,callback=(yield tornado.gen.Callback("user")))
		user_response = yield tornado.gen.Wait("user")

		if user_response[1]["error"]:
			raise tornado.web.HTTPError(500)
		preexisting_user = user_response[0][0]
		if preexisting_user:
			raise tornado.web.HTTPError(500)


		self.db.users.insert(user, callback=(yield tornado.gen.Callback("add_user")))
		add_user_response = yield tornado.gen.Wait("add_user")
		if add_user_response[1]["error"]:
			raise tornado.web.HTTPError(500)

		self.db.passwords.insert({"username":username, "hashed":password.hashed}, callback=(yield tornado.gen.Callback("add_hash")))
		add_hash_response = yield tornado.gen.Wait("add_hash")
		if add_hash_response[1]["error"]:
			raise tornado.web.HTTPError(500)

		self.set_secure_cookie('user',tornado.escape.json_encode(user))
		self.redirect("/")
			
class LoginHandler(BaseHandler):
	def get(self):
		self.redirect("/")
	@tornado.web.asynchronous
	@tornado.gen.engine
	def post(self):
		username = self.get_argument("username")
		password = self.get_argument("password")

		self.db.users.find({"username":username},{"_id":0},limit=1,callback=(yield tornado.gen.Callback("user")))
		user_response = yield tornado.gen.Wait("user")
		if user_response[1]["error"]:
			raise tornado.web.HTTPError(500)
		try:
			user = user_response[0][0][0]
		except IndexError:
			self.redirect("/")
		password = Password(password, salt=user["salt"])

		self.db.passwords.find({"username":username},{"_id":0},limit=1,callback=(yield tornado.gen.Callback("password")))
		check_response = yield tornado.gen.Wait("password")
		if check_response[1]["error"]:
			raise tornado.web.HTTPError(500)
		check = check_response[0][0][0]

		print check

		if check["hashed"] == password.hashed:
			self.set_secure_cookie('user',tornado.escape.json_encode(user))
			self.redirect("/")
		else:
			self.redirect("/login")

class LogoutHandler(BaseHandler):
	def get(self):
		self.clear_cookie("user")
		self.redirect("/")