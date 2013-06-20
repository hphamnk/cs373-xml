import xml.etree.ElementTree as ET


# -------------
# XML_solve
# -------------

def xml_solve (r, w) :
    """
    r is a reader
    w is a writer
    """
    querry = ["Team", "Cooly"]

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
    for x in root.iter():
    	#print x.tag
    	if x.tag == querry[0]:
    		for elem in x.findall(querry[1]):
    			print elem.tag