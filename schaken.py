# -*- coding: UTF8 -*-
#dit beschijft het bord van het schaakspel
from stukken import *

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
				stuk = self.StukOpPlek( Plek(c,r) )
				if stuk == None:
					strBord += "-"
				else:
					strBord += str( stuk )
			
			strBord += "\n"  	
		return strBord

	#Hier controleeren of de plek nog op het bord i
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

		self.beurt = Kleur.WIT

	#Hiermee kan je zien welk stuk op de deze plek staat
	def StukOpPlek( self, plek ):
		for stuk in self.stukken:
			if stuk.plek.kolom == plek.kolom and stuk.plek.rij == plek.rij:
				return stuk
		return None
	# een zet is de verplaatsing van een stuk
	def Zet (self, van, naar):
		stuk = self.StukOpPlek(van)
		if stuk == None: 
			return "Daar staat niets"
		if stuk.kleur != self.beurt: 
			return "Niet aan andermans stukken zitten, zak"

		if not naar in stuk.MogelijkePlekken(b):
		 	return "Dat kan kannie toch nie"
	 	slaan = self.StukOpPlek(naar)
	 	if slaan != None:
	 		self.stukken.remove(slaan)
	 	stuk.plek = naar

	 	self.beurt = Kleur.ZWART if self.beurt == Kleur.WIT else Kleur.WIT


#Hier waarde kleuren
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


	#Dit is nodig om een plek in een set te gebruiken
	#Plekken moeten met elkaar kunnen wordern vergeleken	
	def __eq__(self, other):
		if  other == None :
			return False
		if( self.kolom != other.kolom ):
			return False
		if( self.rij != other.rij ):
			return False
		return True
	
	def __ne__(self,other):
		return False == self.__eq__(other)

	
#Hierdoor kan de computer een stuk text omzetten naar een plek
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




if __name__ == '__main__':

	#hieronder wat testcode, (wat je komt te zien)
	b = Bord()
	b.Opstellen()

	doorgaan = True
	while doorgaan:
		print( b )
		opdrachten = raw_input("Doe iets:").split()
		if( opdrachten[0] == "stop" ):
			doorgaan = False

		if (len(opdrachten)>= 2):
			van = VanTekstNaarPlek( opdrachten[0], b )
			naar = VanTekstNaarPlek( opdrachten[1], b )

			if( van != None and naar != None ):
				print(b.Zet(van, naar))
