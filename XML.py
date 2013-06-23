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
	querryLength = len(querry)

	tree = ET.ElementTree(ET.fromstring(r))
	root = tree.getroot()
	print "root: ", root
	print "root.tag: ", root.tag
	
	"""
	print "\nchildren + grandchildren: "
	for x in root.iter():
		print x.tag

	print "\nchildren of root (THU): "
	for elem in root.getchildren():
		print elem.tag

	print "\nfind tag in children but not grandchildren"
	for elem in root.findall(querry[0]):
		print elem.tag
	"""

	"""
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
	"""


	print "--------------------------------------------------------------"
	print "querry:", querry
	#print "last element of list:", querry[-1]
	#print "next element of list:", querry[1:]
	occurCount = 0
	occurAtLine = 0
	for x in root.iter():
		occurAtLine += 1
		if x.tag == querry[0]:
			if querryLength == 1:
				occurCount += 1
			else:
				print x.tag, x
				occurCount += xml_solve(x, querry[1:],querry[-1])
				print "occurAtLine:", occurAtLine
				print occurCount
	
	print occurCount

def xml_solve(tree, target, lastTarget):
	print "xml_solve starts here ------------------------------"
	targetLength = len(target)
	print "tree:", tree
	print "target:", target, "length:", targetLength 

	for x in tree.getchildren():
		if x.tag == target[0]:
			print x.tag, "==", target[0]
			if x.tag == lastTarget:
				print "found"
				return 1
			elif targetLength > 1:
				print "recursive call"
				return xml_solve(x, target[1:],lastTarget)
	else:
		print "did not find anything"
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
	xml_handler(xml,w)