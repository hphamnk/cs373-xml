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
	rootLength = len(root)
	print "rootLength:", rootLength

	query2 = ET.ElementTree(ET.fromstring(w))
	query2Root = query2.getroot()
	print "query2:", query2
	print "query2Root:", query2Root
	print "query2Root.tag:", query2Root.tag
	query2Children = query2Root.getchildren
	print "query2Children:", query2Children 

	targetChildren = {}
	for x in query2Root.getchildren():
		targetChildren[x] = x.tag
		print "children x.tag:", x.tag

	for x in targetChildren:
		print "targetChildren[x]:", targetChildren[x]

	queryLastElement = ""
	query2Lengh = 0
	for x in query2Root.iter():
		print "query iter:", x.tag
		queryLastElement = x.tag
		query2Lengh += 1
	print "queryLastElement:", queryLastElement
	print "query2Lengh:", query2Lengh

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
	#print "query:", query
	#print "last element of list:", query[-1]
	#print "next element of list:", query[1:]
	occurCount = 0
	occurAtLine = 0
	for x in root.iter():
		occurAtLine += 1
		#print occurAtLine, x.tag
		if x.tag == query2Root.tag:
			if queryLength == 1:
				occurCount += 1
			else:
				print "x.tag:", x.tag, "x:", x
				#occurCount += xml_solve(x, query[1:],queryLastElement)
				occurCount += xml_solve(x, query2Root,queryLastElement)
				print "occurAtLine:", occurAtLine
				print "occurCount:", occurCount
	
	print "final occurCount:", occurCount

#-------------------------------------------------------------------------------------------

def xml_solve(tree, target, lastTarget):
	print "\nxml_solve starts here ------------------------------"
	targetLength = len(target)
	print "tree:", tree
	print "target:", target, "lastTarget:", lastTarget

	xml_solve_targetChildren = {0:0}
	targetKey = 0
	for x in target.getchildren():
		xml_solve_targetChildren[targetKey] = x
		#print x.list(elem)
		targetKey += 1 

	for x in xml_solve_targetChildren:
		print "xml_solve_targetChildren[x]:", xml_solve_targetChildren[x]

	"""
	targetGrandChild = 0
	for x in xml_solve_targetChildren[0].getchildren():
		targetGrandChild = x
		print "targetGrandChild:", targetGrandChild 
	"""

	targetTotalLength = 0
	print "children + grandchildren of target: "
	for x in target.iter():
		targetTotalLength += 1
		print x.tag
	print "targetTotalLength:", targetTotalLength

	""""  
	same level do later	
	while targetLength > 1
		xml_sol
	"""

	# assume there is only 1 child per level
	for x in tree.getchildren():
		if x.tag == xml_solve_targetChildren[0].tag:
			print "found a match:", x.tag, "==", xml_solve_targetChildren[0]
			if x.tag == lastTarget:
				print "found whole query"
				return 1 
			
			elif targetTotalLength > 1:
				print "call recursively"
				return xml_solve(x, xml_solve_targetChildren[0], lastTarget)
			
	else:
		print "didnt find anything"
		return 0

	"""
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
	"""

#-------------------------------------------------------------------------------------------

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