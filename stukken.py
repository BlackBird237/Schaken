# -*- coding: UTF8 -*-
from schaken import *

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


#Dit is de pion, een meer specifieke versie van stuk
class Pion( Stuk ):
	def __init__(self, kleur, plek = Plek() ):
		Stuk.__init__(self, kleur)
		self.plek = plek
		self.wit = "♟"
		self.zwart = "♙"
	# Hier een lijst met alle mogelijke plekken waar
	# een pion heen gezet kan worden.
	def MogelijkePlekken(self, bord):
		lijst = []
		#Dit is voor de witte stukken
		if self.kleur == Kleur.WIT:
			p = Plek( self.plek.kolom, self.plek.rij +1 )
			if bord.StukOpPlek(p) == None:
				lijst.append(p)
				#Pion in eersten zet mogelijk twee vooruit. 
				if( p.rij == 2 ):
					p = Plek( p.kolom, 3 ) 
					if bord.StukOpPlek(p) == None:
						lijst.append(p)
			#De schuine zet vooruit als de witte pion slaat 		
			schuin = [
				Plek( self.plek.kolom+1, self.plek.rij +1 ),
				Plek( self.plek.kolom-1, self.plek.rij +1 )
			]

			for p in schuin:
				slaan = bord.StukOpPlek(p)
				if slaan != None: 
					if slaan.kleur == Kleur.ZWART:
						lijst.append(p)


		else:
			#voor de zwarte stukken
			p = Plek( self.plek.kolom, self.plek.rij -1 )
			if bord.StukOpPlek(p) == None:
				lijst.append(p)
				#Pion in eerste zet mogelijk twee vooruit
				if( p.rij == 5 ):
					p = Plek( p.kolom, 4 ) 
					if bord.StukOpPlek(p) == None:
						lijst.append(p)
			#De schuine zet vooruit als de zwarte pion slaat
			schuin = [
				Plek( self.plek.kolom+1, self.plek.rij -1 ),
				Plek( self.plek.kolom-1, self.plek.rij -1 )
			]

			for p in schuin:
				slaan = bord.StukOpPlek(p)
				if slaan != None: 
					if slaan.kleur == Kleur.WIT:
						lijst.append(p)

		return lijst




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