# -*- coding: UTF8 -*-
#dit beschijft het bord van het schaakspel
import copy
from stukken import *

class Bord:
	rijen = 8
	kolommen = 8

	def __init__(self):
		self.stukken = {}

	def __str__(self):
		strBord = " ABCDEFGH\n"
		for r in reversed(range( Bord.rijen )):
			strBord += str( r+1 )
			for c in range( Bord.kolommen ) : 
				plek = (c,r)
				stuk = self.StukOpPlek( plek )
				if stuk == None:
					strBord += "⌞"
				else:
					strBord += str( stuk )
			
			strBord += "\n"  	
		return strBord


#
	def MogelijkeBorden( self, diep ):

		if( diep <= 0):
			return
		diep -= 1

		self.bordenlijst = []
		for van in self.stukken:
			stuk = self.stukken[ van ]

			if stuk.kleur != self.beurt:
				continue
			for naar in stuk.MogelijkePlekken( van, self ):
				print( VanPlekNaarTekst( van ) + " naar " + VanPlekNaarTekst( naar ) ) 
				b = Bord()
				b.beurt = Kleur.WIT if self.beurt == Kleur.ZWART else Kleur.ZWART
				b.stukken = self.stukken.copy()

				if naar in b.stukken:
			 		del( b.stukken[naar] )

	 			b.stukken[naar] = b.stukken[van]
	 			del( b.stukken[van] )
		
	 			b.MogelijkeBorden( diep )
	 			self.bordenlijst.append( b )
	 	


	#Hier controleeren of de plek nog op het bord i
	def IsPlekOpBord(self, plek):
		if( plek[1] < 0 or plek[1] >= self.rijen ):
			 return False
		if( plek[0] < 0 or plek[0] >= self.kolommen ):
			return False
		return True

	#Zet alle stukken in de begin stand
	def Opstellen(self):
		self.stukken = {}
		for k in range( 8 ):
			self.stukken[(k,1)] = Pion( Kleur.WIT )
			self.stukken[(k,6)] = Pion( Kleur.ZWART )
		for k in [0,7]:
			self.stukken[(k, 0)] = Toren( Kleur.WIT )
			self.stukken[(k, 7)] = Toren( Kleur.ZWART )
		for k in [1,6]:
			self.stukken[(k, 0)]= Paard( Kleur.WIT )
			self.stukken[(k, 7)]= Paard( Kleur.ZWART )
		for k in [2,5]:
			self.stukken[(k, 0)]= Loper( Kleur.WIT )
			self.stukken[(k, 7)]= Loper( Kleur.ZWART )	

		self.stukken[(3, 0)]= Koningin( Kleur.WIT )
		self.stukken[(3, 7)]= Koningin( Kleur.ZWART )

		self.stukken[(4, 0)]= Koning( Kleur.WIT )
		self.stukken[(4, 7)]= Koning( Kleur.ZWART )
		self.beurt = Kleur.WIT


	def HaalWaarde( self, kleur ):
		resultaat = 0
		for plek in self.stukken:
			stuk = self.stukken[plek]; 
			if  stuk.kleur == kleur: 
				resultaat += stuk.waarde
		return resultaat

	#Hiermee kan je zien welk stuk op de deze plek staat
	def StukOpPlek( self, plek ):
		if plek in self.stukken:
			return self.stukken[plek]
		else:
			return None

	# een zet is de verplaatsing van een stuk
	def Zet (self, van, naar):
		stuk = self.StukOpPlek(van)
		if stuk == None: 
			return "Daar staat niets"
		if stuk.kleur != self.beurt: 
			return "Niet aan andermans stukken zitten, vriend"

		if not naar in stuk.MogelijkePlekken(van, b):
		 	return "Dat kannie toch nie"
	 	
	 	if naar in self.stukken:
	 		del( self.stukken[naar] )

	 	self.stukken[naar] = self.stukken[van]
	 	del( self.stukken[van] )

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
