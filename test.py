
# -*- coding: UTF8 -*-
import unittest
import schaken

class TestSchaken( unittest.TestCase ): 
	def test_bord(self):
		b = schaken.Bord()
		b.Opstellen()

		self.assertTrue( b.beurt == schaken.Kleur.WIT )


	def test_plek(self):
		p1 = schaken.Plek( 1,1 )
		p2 = schaken.Plek( 1,1 )
		self.assertTrue( p1 == p2 )


if __name__ == '__main__':
    unittest.main()
    print("hall")

