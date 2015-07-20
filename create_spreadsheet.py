#!/usr/bin/python
#to execute: ./create_spreadsheet.py "library name"

import sys
from parse_lib import parse_lib

library = sys.argv[1]
myLib = parse_lib(library)
if myLib.parseLib():
	myLib.writeCSV()
else:
	print("Library is not valid")
myLib.closeFile()
