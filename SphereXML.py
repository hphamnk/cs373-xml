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
			assert x.isspace()
			xml_string += "</hphamnk>"
			xml_printer(w, xml_handler(xml_string))
			xml_string = "<hphamnk>"
			assert xml_string == "<hphamnk>"

	else:
		xml_string += "</hphamnk>"
		xml_printer(w, xml_handler(xml_string))


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
	xml_string = xml_string.replace(" ", "")
	tree = ET.ElementTree(ET.fromstring(xml_string))
	treeRoot = tree.getroot()

	#print "invalid input" 
	#when given an input without a xml tree or query or both
	treeLength = len(treeRoot.getchildren())
	if treeLength == 0 or treeLength == 1 :
		return {0:0}

	assert treeLength > 1

	xmlAndQuery = {}
	xmlAndQueryCounter = 0
	for x in treeRoot.getchildren():
		xmlAndQuery[xmlAndQueryCounter] = x
		xmlAndQueryCounter += 1

	xml = xmlAndQuery[0]
	query = xmlAndQuery[1]

	queryLength = len(query)

	answer = {}
	occurCount = 0
	occurAtLine = 0
	occurSolve = 0 
	for x in xml.iter():
		occurAtLine += 1
		if x.tag == query.tag:
			assert x.tag == query.tag
			if queryLength == 0:
				assert queryLength == 0
				occurCount += 1
				answer[occurCount] = occurAtLine
			else:
				occurSolve = xml_solver(x, query)
				occurCount += occurSolve
				if occurSolve != 0:
					assert occurSolve != 0
					answer[occurCount] = occurAtLine
	
	answer[0] = occurCount
	return answer
	

# -----------
# xml_solver
# -----------
def xml_solver(xmlS, queryS, sibling = 0, sibling_num = 0, sibling_ChildrenList = 0):
	"""
	xmlS = xml tree
	queryS = query
	find children of queryS since the parent is found in xml_handler
	get the queryS_length
	find the element in xml tree that matches the child of queryS
		determine if we are looking for a child of queryS or a sibling of a child of queryS
			sibling:
				if sibling doesnt have kids nor siblings left
					return 1
				if sibling doesnt have kids and have siblings
					call xml_solve recursively on the next sibling
				if sibling have kids
					call xml_solve recursively on the kids of the sibling
			child:
				if child doesnt have kids nor siblings left
					return 1
				if child doesnt have kids and have siblings
					call xml_solve recursively on the next sibling
				if child have kids
					call xml_solve recursively on the kids of the child
		else, we didnt find anything
			return 0
	"""
	queryS_Children = {0:0}
	queryS_Children_count = 0
	for x in queryS.getchildren():
		queryS_Children[queryS_Children_count] = x
		queryS_Children_count += 1 

	queryS_length = 0
	for x in queryS.iter():
		queryS_length += 1

	children_count = 0
	last_child = queryS_Children_count -1
	for x in xmlS.getchildren():
		# if this xml_solver is for a sibling
		if sibling != 0:
			if x.tag == sibling.tag:
				# if sibling doesnt have children and current child x is last child
				if sibling.getchildren() == [] and sibling_num == last_child:
					return 1
				# if sibling doesnt have children and sibling is not last child
				elif sibling.getchildren() == [] and sibling_num != last_child:
					return xml_solver(xmlS, queryS, sibling_ChildrenList[sibling_num + 1], sibling_num + 1, sibling_ChildrenList)
				# if sibling has children
				elif queryS_length > 1:
					assert queryS_length > 1
					return xml_solver(x, queryS_Children[sibling_num])

		elif x.tag == queryS_Children[children_count].tag:
			assert x.tag == queryS_Children[children_count].tag
			# if child x doesnt have children and x is last child
			if queryS_Children[children_count].getchildren() == [] and children_count == last_child:
				assert queryS_Children[children_count].getchildren() == []
				return 1 
			# if child x doesnt have children and child x is not last child
			elif queryS_Children[children_count].getchildren() == [] and children_count != last_child:
				return xml_solver(xmlS, queryS, queryS_Children[children_count + 1], children_count + 1, queryS_Children)
			# if child x has children
			elif queryS_length > 1:
				assert queryS_length > 1
				return xml_solver(x, queryS_Children[children_count])
	else:
		return 0


#!/usr/bin/env python

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To run the program
    % python RunCollatz.py < RunCollatz.in > RunCollatz.out
    % chmod ugo+x RunCollatz.py
    % RunCollatz.py < RunCollatz.in > RunCollatz.out

To document the program
    % pydoc -w Collatz
"""

# -------
# imports
# -------

import sys
import xml.etree.ElementTree as ET

# ----
# main
# ----

xml_reader(sys.stdin, sys.stdout)
