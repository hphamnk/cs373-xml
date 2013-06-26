import xml.etree.ElementTree as ET

# -------------
# xml_reader
# -------------

def xml_reader (r,w):
	"""
	r = reader
	w = writer
	concatenate every line in the file into a string until empty line
		1. wrap <hphamnk> and </hphamnk> around the string
		2. <hphamnk> is the new root, with xml tree as child 0 and query as child 1
		3. then pass that string into xml_handler
		4. print the answer from xml_handler
		5. clear the string for the next set of input
	then do step 1-4 again to get the last input from the file
	"""
	arrayCount = 0
	xml_string = "<hphamnk>"
	for x in r:
		arrayCount += 1
		xml_string += x
		if x.isspace():
			xml_string += "</hphamnk>"
			xml_printer(w, xml_handler(xml_string))
			xml_string = "<hphamnk>"
			#answer = xml_handler(xml_string)
			#print answer
	else:
		xml_string += "</hphamnk>"
		xml_printer(w, xml_handler(xml_string))
		#answer = xml_handler(xml_string)
		#print answer


# -------------
# xml_printer
# -------------

def xml_printer (w, answer):
	"""
	w = writer
	answer = dictionary that holds the items to print
	go through answer and print out every item in that dictionary
	"""
	for x in answer:
		w.write(str(answer[x]) + "\n")
	w.write("\n")


# -------------
# xml_handler
# -------------

def xml_handler (xml_string) :
	"""
	xml_string = string that holds the input
	convert xml_string into a tree
	get its children
	child 0 = xml tree, child 1 = query
	occurCount = occurences of query in xml tree
	occurAtLine = query occurs at line
	if query has only 1 item
		check for that item in xml tree 
		keep track of occurCount, occurAtLine
	if query has more than 1 item
		check for the first item in xml tree
		call xml_solver, pass in current x element in xml tree and query
		if xml_solver sees that current x element has all items in the query
			keep track occurCount, occurAtLine
	return occurCount and occurAtLine

	"""
	tree = ET.ElementTree(ET.fromstring(xml_string))
	treeRoot = tree.getroot()
	#print "treeRoot: ", treeRoot

	#print "invalid input" 
	#when given an input without a xml tree or query or both
	if len(treeRoot.getchildren()) == 0 or len(treeRoot.getchildren()) == 1 :
		return {0:0}

	xmlAndQuery = {}
	xmlAndQueryCounter = 0
	for x in treeRoot.getchildren():
		xmlAndQuery[xmlAndQueryCounter] = x
		xmlAndQueryCounter += 1

	xml = xmlAndQuery[0]
	query = xmlAndQuery[1]
	#print "xml:", xml
	#print "query:", query

	queryLength = len(query)
	#print "queryLength:", queryLength

	answer = {}
	occurCount = 0
	occurAtLine = 0
	occurSolve = 0 
	for x in xml.iter():
		occurAtLine += 1
		#print "line:", occurAtLine, "item:", x.tag
		if x.tag == query.tag:
			#print "found:", x.tag, "==", query.tag
			if queryLength == 0:
				occurCount += 1
				answer[occurCount] = occurAtLine
				#print "occurAtLine:", occurAtLine
			else:
				occurSolve = xml_solver(x, query)
				occurCount += occurSolve
				if occurSolve != 0:
					answer[occurCount] = occurAtLine
					#print "occurAtLine:", occurAtLine
	
	answer[0] = occurCount
	#print "final occurCount:", occurCount
	#print answer
	return answer
	

# -----------
# xml_solver
# -----------
def xml_solver(xmlS, queryS):
	"""
	xmlS = xml tree
	querryS = querry
	find children of querryS since the parent is found in xml_handler
	get the querryS_length
	find the element in xml tree that matches the child of queryS
		if child of queryS has no children then we are at the end of query
			return 1
		if queryS_length is more than 1, we still have more elements to search for
			call xml_solver recursively, passing in the chilren of queryS
		else, we didnt find anything
			return 0
	"""
	#print "\n-------------------- xml_solver starts --------------------"
	#print "xmlS:", xmlS
	#print "queryS:", queryS

	queryS_Children = {0:0}
	queryS_Children_count = 0
	for x in queryS.getchildren():
		queryS_Children[queryS_Children_count] = x
		queryS_Children_count += 1 
	#print "queryS_Children_count:", queryS_Children_count 

	queryS_length = 0
	#print "children + grandchildren of queryS:"
	for x in queryS.iter():
		#print queryS_length, x.tag
		queryS_length += 1
	#print "queryS_length:", queryS_length

	for x in xmlS.getchildren():
		if x.tag == queryS_Children[0].tag:
			#print "found a match:", x.tag, "==", queryS_Children[0]
			if queryS_Children[0].getchildren() == []:
				#print "found whole query"
				return 1 
			elif queryS_length > 1:
				#print "call recursively"
				return xml_solver(x, queryS_Children[0])
	else:
		#print "didnt find anything"
		return 0


