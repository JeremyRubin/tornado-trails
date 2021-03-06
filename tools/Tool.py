#Brought to you by Jeremy Rubin, 2013

import tornado.template
import os

class Tool(object):
	def __init__(self, args):
		self.args = args
		self.type = args["type"]
		self.path = os.path.dirname(os.path.realpath(__file__))
		self.target = args['target']
		self.name = args['name']
		self.template = args['template']
		self.templater()
	def templater(self):
		loader = tornado.template.Loader("/templates")
		op = loader.load(os.path.join(self.path,
			"templates/", self.template))
		result = op.generate(**self.args)
		f = open(os.path.join(self.path, "targets",self.target,self.name+self.type), 'w')
		f.write(result)


