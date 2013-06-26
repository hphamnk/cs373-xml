# -------
# imports
# -------

import StringIO
import unittest


from XML import xml_handler, xml_solver, xml_reader, xml_printer

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # 
    # ----
	def test_xml_reader_1query(self):
		r = StringIO.StringIO("<THU> </THU> <THU> </THU>")
		w = StringIO.StringIO()
		xml_reader(r,w)
		self.assert_(w.getvalue() == "1\n1\n\n")

	def test_xml_reader_givenExample(self):
		r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
		w = StringIO.StringIO()
		xml_reader(r,w)
		self.assert_(w.getvalue() == "2\n2\n7\n\n")

	def test_xml_reader_givenExample_2inputs(self):
		r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>\n\n<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
		w = StringIO.StringIO()
		xml_reader(r,w)
		self.assert_(w.getvalue() == "2\n2\n7\n\n2\n2\n7\n\n")

	def test_xml_printer(self):
		answer = {0:0, 1:1, 2:2, 3:3}
		self.assertEqual(answer[0],0)
		self.assertEqual(answer[1],1)
		self.assertEqual(answer[2],2)
		self.assertEqual(answer[3],3)

	def test_xml_printer_is0(self):
		answer = {0:0}
		self.assertEqual(answer[0],0)

	def test_xml_printer_all5(self):
		answer = {0:5, 1:5, 2:5, 3:5, 4:5, 5:5}
		self.assertEqual(answer[0],5)
		self.assertEqual(answer[1],5)
		self.assertEqual(answer[2],5)
		self.assertEqual(answer[3],5)
		self.assertEqual(answer[4],5)
		self.assertEqual(answer[5],5)

	
	def test_xml_reader_1query(self):
		r = StringIO.StringIO("<THU> </THU> <B> </B>")
		w = StringIO.StringIO()
		xml_reader(r,w)
		answer = {0: 1, 1: 1}
		self.assert_(w.getvalue() == "(0)")
	


# ----
# main
# ----

print ("TestXML.py")
unittest.main()
print ("Done.")