#Brought to you by Jeremy Rubin, 2013

import Tool
import argparse
import fileinput
import os
import sys
class NewHandler(object):
	def __init__(self, arg):
		opts = vars(args)
		send = {"name":arg.name,
				"target":"tornado_handlers",
				"template":"python/handler.pyt",
				"type":"Handler.py"}
		print "Creating: "+str(send)
		Tool.Tool(send)
		send = {"name":arg.name,
				"target":"tornado_models",
				"template":"python/model.pyt",
				"type":"Model.py"}
		print "Creating: "+str(send)
		Tool.Tool(send)
		self.path = os.path.dirname(os.path.realpath(__file__))
		self.add_links(arg.url, arg.name)
		self.add_imports(arg.name)
		print "Finished generating!"
	def add_links(self, rel_url, name):

		path = os.path.join(self.path, "targets/routes.py")
		f = open(path, "r")
		lines = [line for line in f]
		lines.insert(3, ('(r"'+rel_url+'/?", '+name+'Handler),').rstrip()+"\n")
		f2 = open(path, "w")
		[f2.write(line) for line in lines]
		print "Links Added"
	def add_imports(self, name):
		path = os.path.join(self.path, "targets/handlers_list.py")
		f = open(path, "a")
		f.write("\nfrom handlers."+name+"Handler import "+name+"Handler")

		path = os.path.join(self.path, "targets/models_list.py")
		f = open(path, "a")
		f.write("\nfrom models."+name+"Model import "+name+"Model")
		print "Imports Added"


parser = argparse.ArgumentParser(description='Make a new handler')
parser.add_argument('name', metavar='n', type=str,
	help='the class name')
parser.add_argument('--url', metavar='u', type=str,
	help='the url')
args = parser.parse_args()
NewHandler(args)