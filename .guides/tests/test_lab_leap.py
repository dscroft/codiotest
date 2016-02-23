from lab_leap import *
import unittest
import calendar

class LeapTest(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_not_leap(self):
		for year in [ i for i in range(1800,2101) if i % 4 != 0 ]:
			self.assertEqual( leap_year( year ), calendar.isleap( year ), 'Failed year %d test' % year )

	def test_every_four(self):
		for year in [ i for i in range(1800,2101) if i % 4 == 0 and i % 100 != 0 ]:
			self.assertEqual( leap_year( year ), calendar.isleap( year ), 'Failed year %d test' % year )

	def test_every_hundred(self):
		for year in [ i for i in range(1800,21001) if i % 100 == 0 and i % 400 != 0 ]:
			self.assertEqual( leap_year( year ), calendar.isleap( year ), 'Failed year %d test' % year )

	def test_every_four_hundred(self):
		for year in [ i for i in range(1800,21001) if i % 400 == 0 ]:
			self.assertEqual( leap_year( year ), calendar.isleap( year ), 'Failed year %d test' % year )

	def test_return_bool(self):
		self.assertEqual( type(leap_year(1900)), bool, "Doesn't return boolean" )

if __name__ == '__main__':
	unittest.main()



