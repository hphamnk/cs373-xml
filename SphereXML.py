# -------------
# XML_solve
# -------------

def xml_handler (xmlString) :
	"""

	"""
	tree = ET.ElementTree(ET.fromstring(xmlString))
	treeRoot = tree.getroot()
#	print "treeRoot: ", treeRoot
	rootLength = len(treeRoot)
#	print "rootLength:", rootLength

	xmlAndQuery = {}
	xmlAndQueryCounter = 0
	for x in treeRoot.getchildren():
		xmlAndQuery[xmlAndQueryCounter] = x
		xmlAndQueryCounter += 1

	xml = xmlAndQuery[0]
	query = xmlAndQuery[1]
#	print xml
#	print query

	queryLength = len(query)
#	print "queryLength:", queryLength

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
#				print "occurAtLine:", occurAtLine
			else:
				occurSolve = xml_solve(x, query)
				occurCount += occurSolve
				if occurSolve != 0:
					answer[occurCount] = occurAtLine
#					print "---------------------occurAtLine:", occurAtLine, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
				#print "          ---------- xml_solve ends ----------     "
	
	answer[0] = occurCount
#	print "final occurCount:", occurCount

	return answer
	

#-------------------------------------------------------------------------------------------

def xml_solve(tree, target):
#	print "\n-------------------- xml_solve starts --------------------"
	targetLength = len(target)
#	print "tree:", tree
#	print "target:", target, "lastTarget:", lastTarget

	xml_solve_targetChildren = {0:0}
	targetChildrenNum = 0
	for x in target.getchildren():
		xml_solve_targetChildren[targetChildrenNum] = x
		#print x.list(elem)
		targetChildrenNum += 1 
#	print "targetChildrenNum:", targetChildrenNum 

	targetTotalLength = 0
#	print "children + grandchildren of target: "
	for x in target.iter():
#		print targetTotalLength, x.tag
		targetTotalLength += 1
#	print "targetTotalLength:", targetTotalLength


	# assume there is only 1 child per level
	for x in tree.getchildren():
		if x.tag == xml_solve_targetChildren[0].tag:
#			print "---------------found a match:", x.tag, "==", xml_solve_targetChildren[0]
			if xml_solve_targetChildren[0].getchildren() == []:
#				print "found whole query"
				return 1 
			elif targetTotalLength > 1:
#				print "call recursively"
				return xml_solve(x, xml_solve_targetChildren[0])
	else:
#		print "didnt find anything"
		return 0

#-------------------------------------------------------------------------------------------

def xml_reader (r,w):


	arrayCount = 0
	xmlString = "<hphamnk>"
	for x in r:
		arrayCount += 1
		xmlString += x
		if x.isspace():
			xmlString += "</hphamnk>"
			#print "blank line at:", arrayCount, "\n", xmlString
			#answer = xml_handler(xmlString)
			#print answer
			xml_printer(w, xml_handler(xmlString), "\n")
			xmlString = "<hphamnk>"
	else:
		xmlString += "</hphamnk>"
		xml_printer(w, xml_handler(xmlString), "")
		#answer = xml_handler(xmlString)
		#print answer

def xml_printer (w, answer, newline):
	for x in answer:
		w.write(str(answer[x]) + "\n")
	w.write(newline)


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
