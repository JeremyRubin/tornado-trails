import Tool
import argparse

parser = argparse.ArgumentParser(description='Make a new handler')
parser.add_argument('parent', metavar='p', type=str,
	help='the class parent')
parser.add_argument('name', metavar='n', type=str,
	help='the class name')

args = parser.parse_args()
class NewHandler(object):
	def __init__(self, args):
		send = {"args":vars(args), "target":"tornado_handlers", "template":"python/handler.pyt", "type":".py"}
		Tool.Tool(send)

NewHandler(args)