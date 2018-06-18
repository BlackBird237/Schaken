
# -*- coding: UTF8 -*-
import unittest
from schaken import *

class TestSchaken( unittest.TestCase ): 
	def test_bord(self):
		b = Bord()
		b.Opstellen()

		self.assertTrue( b.beurt == Kleur.WIT )


	def test_plek(self):
		p1 = Plek( 1,1 )
		p2 = Plek( 1,1 )
		self.assertTrue( p1 == p2 )

	def test_paard(self):
		b = Bord()
		b.Opstellen()

		paard = Paard( Kleur.WIT, Plek(3,3))




if __name__ == '__main__':
    unittest.main()
    print("hall")

