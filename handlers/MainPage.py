from App import *
class MainPage(BaseHandler):
	def get(self):
		print 'seen'
		self.render("main.html")
