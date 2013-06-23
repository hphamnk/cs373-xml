import xml.etree.ElementTree as ET


# -------------
# XML_solve
# -------------

def xml_handler (r, w) :
	"""
	r is a reader
	w is a writer
	"""
	querry = ["Team", "Cooly", "Amber"]

	tree = ET.parse(r)
	root = tree.getroot()
	print "root: ", root
	print "root.tag: ", root.tag
	
	print "\nchildren + grandchildren: "
	for x in root.iter():
		print x.tag

	print "\nchildren of root (THU): "
	for elem in root.getchildren():
		print elem.tag

	print "\nfind tag in children but not grandchildren"
	for elem in root.findall(querry[0]):
		print elem.tag
	print "\nfind querry 0 and 1"
	countOccur = 0
	countNumber = 0
	for x in root.iter():
		#print x.tag
		countNumber += 1
		if x.tag == querry[0]:
			for elem in x.findall(querry[1]):
				countOccur += 1
				print elem.tag
				print "counterNumber: ", countNumber


	print countOccur
	print "--------------------------------------------------------------"
	print "querry:", querry
	print "last element of list:", querry[-1]
	print "next element of list:", querry[1:]
	occurCount = 0
	occurAtLine = 0
	for x in root.iter():
		occurAtLine += 1
		if x.tag == querry[0]:
			print x
			occurCount += xml_solve(x, querry[1:],querry[-1])
			print "occurAtLine:", occurAtLine
	
	print occurCount

def xml_solve(tree, target, lastTarget):
	
	print "target:", target 
	targetLength = len(target)
	for x in tree.getchildren():
		print x.tag
		print target[0]
		if x.tag == target[0]:
			print "testing      ", x.tag, "==", target
			if target == lastTarget:
				return 1
			elif targetLength >1:
				return 0 + xml_solve(x, target[1:],lastTarget)
			else:
				return 0
		else:
			return 0

def xml_reader(r,w):
	arrayCount = 0
	arrayReader = {}
	for reader in r:
		print reader
		arrayReader[arrayCount] = reader
		arrayCount += 1

	root = "".join(arrayReader[0])
	root = root.strip("<")
	root = "</" + root
	print root

	xml = ""
	for x in arrayReader:
		xml += "".join(arrayReader[x])
		if root in arrayReader[x]:
			break 

	print xml