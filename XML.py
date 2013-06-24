import xml.etree.ElementTree as ET


# -------------
# XML_solve
# -------------

def xml_handler (r, w) :
	"""
	r is a reader
	w is a writer
	"""
	tree = ET.ElementTree(ET.fromstring(r))
	root = tree.getroot()
	print "root: ", root
	print "root.tag: ", root.tag
	rootLength = len(root)
	print "rootLength:", rootLength

	query = ET.ElementTree(ET.fromstring(w))
	queryRoot = query.getroot()
	print "queryRoot:", queryRoot
	print "queryRoot.tag:", queryRoot.tag

	queryLastElement = ""
	queryLength = 0
	for x in queryRoot.iter():
		queryLength += 1
		print "queryItem #", queryLength, ":", x.tag
		queryLastElement = x.tag
	print "queryLastElement:", queryLastElement
	print "queryLength:", queryLength

	"""
	print "\nchildren of root (THU): "
	for elem in root.getchildren():
		print elem.tag
	getchildrenLength = len(root.getchildren())
	print "getchildrenLength:", getchildrenLength
	
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
	occurCount = 0
	occurAtLine = 0
	for x in root.iter():
		occurAtLine += 1
		#print "line:", occurAtLine, "item:", x.tag
		if x.tag == queryRoot.tag:
			#print "found:", x.tag, "==", queryRoot.tag
			if queryLength == 1:
				occurCount += 1
				print "occurAtLine:", occurAtLine
			else:
				occurCount += xml_solve(x, queryRoot,queryLastElement)
				print "occurAtLine:", occurAtLine
				print "occurCount:", occurCount
				#print "          ---------- xml_solve ends ----------     "
	
	print "final occurCount:", occurCount

#-------------------------------------------------------------------------------------------

def xml_solve(tree, target, lastTarget):
	print "\n-------------------- xml_solve starts --------------------"
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
			print "---------------found a match:", x.tag, "==", xml_solve_targetChildren[0]
			print "children of xml_solve_targetChildren[0]:", xml_solve_targetChildren[0].getchildren()
			#if x.tag == lastTarget:
			if xml_solve_targetChildren[0].getchildren() == []:
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