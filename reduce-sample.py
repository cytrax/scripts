#!/usr/local/bin/python3
from functools import reduce

class fox(object):
	def __init__(self, *args):

		print (reduce((lambda a,b: a + b), args))
f = fox(10, 20, 30, 40, 50)