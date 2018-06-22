
# -*- coding: UTF8 -*-
import unittest
from schaken import *

class TestSchaken( unittest.TestCase ): 
	def test_bord(self):
		b = Bord()
		b.Opstellen()

		#even kijken of de waarde van wit geliljk is aan de waarde van zwart. 
		self.assertTrue( b.beurt == Kleur.WIT )
		self.assertTrue( b.HaalWaarde( Kleur.WIT ) == b.HaalWaarde( Kleur.ZWART ) )

		b.MogelijkeBorden(4)
		

	def test_paard(self):
		b = Bord()
		b.Opstellen()
		#paard = Paard( Kleur.WIT, Plek(3,3))


if __name__ == '__main__':
    unittest.main()
    print("hall")

