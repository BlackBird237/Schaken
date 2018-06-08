#dit beschijft het bord van het schaakspel
class Bord:
	rijen = 8
	colommen = 8

	def __init__(self):
		self.stukken = []

	def __str__(self):
		strBord = " ABCDEFGH\n"
		for r in range( Bord.rijen): 
			strBord += str( Bord.rijen - r)
			for c in range( Bord.colommen ) : 
				strBord += "-"
			strBord += "\n"  	
		return strBord

	#Hier controleeren of de plek nog op het bord is
	def IsPlekOpBord(self, plek):
		if( plek.rij < 0 | plek.rij >= self.rijen ) return False
		if( plek.colom < 0 | plek.colom >= self.colommen ) return False
		return True


class Kleur:
	ZWART = 0
	WIT =1


class Stuk: 
	def __init__(self, kleur):
		self.kleur = kleur





class Plek:
	def __init__(self, colom, rij):
		self.colom = colom
		self.rij = rij

	def __str__(self):
		return chr( ord("A") + self.colom ) + str( self.rij + 1)





#hierder wat test code
b = Bord()
pion = Stuk( Kleur.ZWART )

p = Plek(9,9)

print( p )

  