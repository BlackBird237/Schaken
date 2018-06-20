# -*- coding: UTF8 -*-
#dit beschijft het bord van het schaakspel
import copy
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
					strBord += "⌞"
				else:
					strBord += str( stuk )
			
			strBord += "\n"  	
		return strBord


#
	def MogelijkeBorden(self, diep ):

		if( diep <= 0):
			return
		diep -= 1

		self.bordenlijst = []
		for stuk in self.stukken:
			if stuk.kleur != self.beurt:
				continue
			for plek in stuk.MogelijkePlekken(self):
				b = Bord()
				b.beurt = Kleur.WIT if self.beurt == Kleur.ZWART else Kleur.ZWART
				b.stukken = copy.deepcopy(self.stukken)
				slaan = b.StukOpPlek(plek)
		 		if slaan != None:
	 				b.stukken.remove(slaan)
	 			stukcopy = b.StukOpPlek( stuk.plek )
	 			stukcopy.plek = plek

	 			b.MogelijkeBorden( diep )
	 			self.bordenlijst.append( b )
	 	print( diep )


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


	def HaalWaarde( self, kleur ):
		resultaat = 0
		for stuk in self.stukken:
			if stuk.kleur == kleur: 
				resultaat += stuk.waarde
		return resultaat

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
			return "Niet aan andermans stukken zitten, vriend"

		if not naar in stuk.MogelijkePlekken(b):
		 	return "Dat kannie toch nie"
	 	slaan = self.StukOpPlek(naar)
	 	if slaan != None:
	 		self.stukken.remove(slaan)
	 	stuk.plek = naar

	 	self.beurt = Kleur.ZWART if self.beurt == Kleur.WIT else Kleur.WIT
	 	return "Daar!"




if __name__ == '__main__':

	#hieronder wat testcode, (wat je komt te zien)
	b = Bord()
	b.Opstellen()

	doorgaan = True
	while doorgaan:
		print( b )

		aanzet = "wit" if b.beurt == Kleur.WIT else "zwart"
		opdrachten = raw_input( aanzet + " is aan zet:").split()

		if len( opdrachten ) ==1: 
			if( opdrachten[0] == "stop" ):
				doorgaan = False

		if (len(opdrachten)>= 2):
			van = VanTekstNaarPlek( opdrachten[0], b )
			naar = VanTekstNaarPlek( opdrachten[1], b )

			if( van != None and naar != None ):
				print(b.Zet(van, naar))
