import re
import itertools

class parse_lib:

	def __init__(self, library):
		self.libFile = open(library)
		self.cellnames = []
		self.leakpower = []
		self.combined = []
		self.LibIsValid = False

	def parseLib(self):
		for line in self.libFile.readlines():
			if re.match("(.*^\s+)cell\(", line):
				self.cellnames.append(line[line.find("(")+1:line.find(")")])

			if re.match("(.*^\s+)cell_leakage_power", line):
				self.leakpower.append(line.split(":")[-1])
				self.LibIsValid = True
				
		if self.LibIsValid:
			return True
		else:
			return False

	def writeCSV(self):
		cellDict = dict(itertools.izip(self.cellnames, self.leakpower))
		for cellname, leakage in cellDict.iteritems():
			self.combined.append('%s: %s' %(str(cellname), str(leakage)))
		final_list = open('combined_list.csv', 'w')
		final_list.write('\t'.join(self.combined))

	def closeFile(self):
		self.libFile.close()
