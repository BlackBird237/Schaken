# -*- coding: UTF8 -*-
#dit beschijft het bord van het schaakspel
class Bord:
	rijen = 8
	kolommen = 8

	def __init__(self):
		self.stukken = []

	def __str__(self):
		strBord = " ABCDEFGH\n"
		for r in reversed(range( Bord.rijen )):
			strBord += str( r+1 )
			for c in range( Bord.kolommen ) : 
				stuk = self.StukVanPlek( Plek(c,r) )
				if stuk == None:
					strBord += "-"
				else:
					strBord += str( stuk )
			
			strBord += "\n"  	
		return strBord

	#Hier controleeren of de plek nog op het bord is
	def IsPlekOpBord(self, plek):
		if( plek.rij < 0 or plek.rij >= self.rijen ):
			 return False
		if( plek.kolom < 0 or plek.kolom >= self.kolommen ):
			return False
		return True

	#Zet alle stukken in de begin stand
	def Opstellen(self):
		self.stukken = []
		for k in range( 8 ):
			self.stukken.append( Pion( Kleur.WIT,   Plek(k, 1) ))
			self.stukken.append( Pion( Kleur.ZWART, Plek(k, 6) ))
		for k in [0,7]:
			self.stukken.append( Toren( Kleur.WIT,   Plek(k, 0) ))
			self.stukken.append( Toren( Kleur.ZWART, Plek(k, 7) ))	
		for k in [1,6]:
			self.stukken.append( Paard( Kleur.WIT,   Plek(k, 0) ))
			self.stukken.append( Paard( Kleur.ZWART, Plek(k, 7) ))
		for k in [2,5]:
			self.stukken.append( Loper( Kleur.WIT,   Plek(k, 0) ))
			self.stukken.append( Loper( Kleur.ZWART, Plek(k, 7) ))	

		self.stukken.append( Koningin( Kleur.WIT,   Plek(3, 0) ))
		self.stukken.append( Koningin( Kleur.ZWART, Plek(3, 7) ))

		self.stukken.append( Koning( Kleur.WIT,   Plek(4, 0) ))
		self.stukken.append( Koning( Kleur.ZWART, Plek(4, 7) ))

	#Hiermee kan je zien welk stuk op de deze plek staat
	def StukVanPlek( self, plek ):
		for stuk in self.stukken:
			if stuk.plek.kolom == plek.kolom and stuk.plek.rij == plek.rij:
				return stuk
		return None


class Kleur:
	ZWART = 0
	WIT =1


class Plek:
	#De -1 betekend dat als je niks opgeeft, dat het stuk dan
	#naast het bord staat
	def __init__(self, kolom = -1, rij = -1):
		self.kolom = kolom
		self.rij = rij

	def __str__(self):
		return chr( ord("A") + self.kolom ) + str( self.rij + 1)


def VanTekstNaarPlek( tekst, bord ):
	tekst = tekst.lower()
	if( len(tekst) != 2 ):
		return None

	k = ord( tekst[0] ) - ord('a')
	r = ord( tekst[1] ) - ord('1')
	if( k < 0 or r < 0 ):
		return None
	if( k >= bord.kolommen or r >= bord.rijen ):
		return None

	return Plek( k, r )

#Hier volgen de stukkenif( k < 0 or r < 0 ):
class Stuk: 
	def __init__(self, kleur):
		self.kleur = kleur
		self.wit = " "
		self.zwart = " "

	def __str__(self):
		if( self.kleur == Kleur.WIT ):
			return self.wit
		else:
			return self.zwart


#dit is de pion, een meer specifieke versie van stuk
class Pion( Stuk ):
	def __init__(self, kleur, plek = Plek() ):
		Stuk.__init__(self, kleur)
		self.plek = plek
		self.wit = "♟"
		self.zwart = "♙"


#Dit is toren, een meer specifieke versie van stuk
class Toren( Stuk ):
	def __init__(self, kleur, plek = Plek () ):
		Stuk.__init__(self, kleur)
		self.plek = plek
		self.wit = "♜"
		self.zwart = "♖"

#Dit is paard, een meer specifieke versie van stuk
class Paard( Stuk ):
	def __init__(self, kleur, plek = Plek () ):
		Stuk.__init__(self, kleur)
		self.plek = plek
		self.wit = "♞"
		self.zwart = "♘"

#Dit is loper, een meer specifieke versie van stuk
class Loper( Stuk ):
	def __init__(self, kleur, plek = Plek () ):
		Stuk.__init__(self, kleur)
		self.plek = plek
		self.wit = "♝"
		self.zwart = "♗"

#Dit is Koningin, een meer specifieke versie van stuk
class Koningin( Stuk ):
	def __init__(self, kleur, plek = Plek () ):
		Stuk.__init__(self, kleur)
		self.plek = plek
		self.wit = "♛"
		self.zwart = "♕"

#Dit is Koning, een meer specifieke versie van stuk
class Koning( Stuk ):
	def __init__(self, kleur, plek = Plek () ):
		Stuk.__init__(self, kleur)
		self.plek = plek
		self.wit = "♚"
		self.zwart = "♔"


 

#hierder wat test code
b = Bord()
b.Opstellen()

doorgaan = True
while doorgaan:
	print( b )
	opdrachten = raw_input("Doe iets:").split()
	print( " ")
	if( opdrachten[0] == "stop" ):
		doorgaan = False

	p1 = VanTekstNaarPlek( opdrachten[0], b )
	p2 = VanTekstNaarPlek( opdrachten[1], b )

	if( p1 != None and p2 != None ):
		print( "Van " + str(p1) + " naar " + str(p2) )


exit()




  