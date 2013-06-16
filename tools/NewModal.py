#Brought to you by Jeremy Rubin, 2013

import Tool
import argparse

parser = argparse.ArgumentParser(description='Make a new handler')
parser.add_argument('name', metavar='n', type=str,
	help='the modal name')
parser.add_argument('title', metavar='t', type=str,
	help='the modal title')
parser.add_argument('modalID', metavar='id', type=str,
	help='the modal ID')
parser.add_argument('modalLabel', metavar='l', type=str,
	help='the modal label')
parser.add_argument('modalContent', metavar='c', type=str,
	help='the modal content')

args = parser.parse_args()
class NewModal(object):
	def __init__(self, args):
		send = {"args":vars(args), "target":"bootstrap_modals", "template":"html/modal.html", "type":".html"}
		Tool.Tool(send)

NewModal(args)