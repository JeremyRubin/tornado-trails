#Brought to you by Jeremy Rubin, 2013
from App import *
class MainPage(BaseHandler):
	def get(self):
		self.render("main.html")
