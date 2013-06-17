#Brought to you by Jeremy Rubin, 2013

import Tool
import argparse
class NewHandler(object):
	def __init__(self, arg):
		opts = vars(args)
		send = {"name":arg,
				"target":"tornado_handlers",
				"template":"python/handler.pyt",
				"type":"Handler.py"}
		Tool.Tool(send)
		send = {"name":arg,
				"target":"tornado_models",
				"template":"python/model.pyt",
				"type":"Model.py"}
		Tool.Tool(send)

parser = argparse.ArgumentParser(description='Make a new handler')
parser.add_argument('name', metavar='n', type=str,
	help='the class name')
args = parser.parse_args()
NewHandler(args.name)