import xml.etree.ElementTree as ET


# -------------
# XML_solve
# -------------

def xml_handler (r, w) :
	"""
	r is a reader
	w is a writer
	"""
	query = ["Team", "Cooly", "Amber"]
	queryLength = len(query)

	tree = ET.ElementTree(ET.fromstring(r))
	root = tree.getroot()
	print "root: ", root
	print "root.tag: ", root.tag

	query2 = ET.ElementTree(ET.fromstring(w))
	query2Root = query2.getroot()
	print "query2Root:", query2Root
	print "query2Root.tag:", query2Root.tag

	queryLastElement = ""
	for x in query2Root.iter():
		print x.tag
		queryLastElement = x.tag
	print "queryLastElement:", queryLastElement

	print "\nchildren of root (THU): "
	for elem in root.getchildren():
		print elem.tag
	getchildrenLength = len(root.getchildren())
	print "getchildrenLength:", getchildrenLength

	"""
	print "\nfind tag in children but not grandchildren"
	for elem in root.findall(query[0]):
		print elem.tag
	
	print "\nfind query 0 and 1"
	countOccur = 0
	countNumber = 0
	for x in root.iter():
		#print x.tag
		countNumber += 1
		if x.tag == query[0]:
			for elem in x.findall(query[1]):
				countOccur += 1
				print elem.tag
				print "counterNumber: ", countNumber
	print countOccur
	"""


	print "--------------------------------------------------------------"
	print "query:", query
	#print "last element of list:", query[-1]
	#print "next element of list:", query[1:]
	occurCount = 0
	occurAtLine = 0
	for x in root.iter():
		occurAtLine += 1
		print occurAtLine, x.tag
		if x.tag == query2Root.tag:
			if queryLength == 1:
				occurCount += 1
			else:
				print x.tag, x
				occurCount += xml_solve(x, query[1:],query[-1])
				print "occurAtLine:", occurAtLine
				print occurCount
	
	print occurCount

def xml_solve(tree, target, lastTarget):
	print "xml_solve starts here ------------------------------"
	targetLength = len(target)
	print "tree:", tree
	print "target:", target, "length:", targetLength 

	for x in tree.getchildren():
		print "tree:", x.tag
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
		#print "reader:", reader
		arrayReader[arrayCount] = reader
		arrayCount += 1

	root = "".join(arrayReader[0])
	root = root.strip("<")
	root = "</" + root
	print root

	xml = ""
	xmlCounter = 0
	targetString = ""
	for x in arrayReader:
		xml += "".join(arrayReader[x])
		xmlCounter += 1
		if root in arrayReader[x]:
			break

	arrayReaderLength = len(arrayReader)
	print "arrayReaderLength:", arrayReaderLength
	print "xmlCounter", xmlCounter

	for x in range(xmlCounter, arrayReaderLength, 1):
		targetString += "".join(arrayReader[x])

	print "xml:", xml
	print "targetString:", targetString

	xml_handler(xml,targetString)