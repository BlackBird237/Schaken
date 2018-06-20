# -*- coding: UTF8 -*-

def MagNaarPlek( bord, stuk, plek ):
	if not bord.IsPlekOpBord( plek ):
		return False

	stukWatErAlStond = bord.StukOpPlek( plek )
	if stukWatErAlStond != None:
		if stukWatErAlStond.kleur == stuk.kleur:
			return False
	return True


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



#Hier de eigenschappen die elk stuk hebben
#Stukken, 
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
	waarde = 1

	def __init__(self, kleur, plek = Plek() ):
		Stuk.__init__(self, kleur)
		self.plek = plek
		self.wit = "♟"
		self.zwart = "♙"
	
	# Hier een lijst met alle mogelijke plekken waar
	# een pion heen gezet kan worden.
	def MogelijkePlekken(self, bord):
		lijst = []
		#Dit is voor de witte pionnen
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

#TODO: pion aan overkant -> koningin of paard ervoor terug


#Dit is toren, een meer specifieke versie van stuk
class Toren( Stuk ):
	waarde = 5
	def __init__(self, kleur, plek = Plek () ):
		Stuk.__init__(self, kleur)
		self.plek = plek
		self.wit = "♜"
		self.zwart = "♖"
	
	def MogelijkePlekken(self, bord):
		lijst = []
		links = [ Plek( self.plek.kolom  - i, self.plek.rij) for i in range( 1, bord.kolommen ) ]
		rechts= [ Plek( self.plek.kolom  + i, self.plek.rij) for i in range( 1, bord.kolommen ) ]
		boven = [ Plek( self.plek.kolom , self.plek.rij + i) for i in range( 1, bord.rijen  ) ]
		onder = [ Plek( self.plek.kolom , self.plek.rij - i) for i in range( 1, bord.rijen  ) ]
		richtingen = [ links, rechts, boven, onder ]
		for richting in richtingen: 
			for stap in richting:
				if not MagNaarPlek( bord, self, stap ):
					break
				lijst.append( stap ) 
		return lijst

#TODO: Rokkade?



#Dit is paard, een meer specifieke versie van stuk
class Paard( Stuk ):
	waarde = 3
	def __init__(self, kleur, plek = Plek () ):
		Stuk.__init__(self, kleur)
		self.plek = plek
		self.wit = "♞"
		self.zwart = "♘"

	def MagNaarPlek( self, plek ):
		return MagNaarPlek( self.bord, self, plek )

	#def MagPaardNaarPlek( bord, stuk, plek ):
	#if not bord.IsPlekOpBord( plek ):
	#	return False

	#	if stukWatErAlStond.kleur == stuk.kleur:
	#	return False
	#return True

	#lijst met de mo gelijke zetten van het paard
	def MogelijkePlekken(self, bord ):
		lijst = [
			Plek( self.plek.kolom+1, self.plek.rij +2 ),
			Plek( self.plek.kolom-1, self.plek.rij +2 ),
			Plek( self.plek.kolom+1, self.plek.rij -2 ),
			Plek( self.plek.kolom-1, self.plek.rij -2 ),
			Plek( self.plek.kolom+2, self.plek.rij +1 ),
			Plek( self.plek.kolom+2, self.plek.rij -1 ),
			Plek( self.plek.kolom-2, self.plek.rij +1 ),
			Plek( self.plek.kolom-2, self.plek.rij -1 )
		]
		# Ingewikkelde functie: eerst geef je bord mee. Dan
		# filter gebruikt functie MagNaarPlek om de lijst aan te
		#vullen met wat mag
		self.bord = bord
		return filter( self.MagNaarPlek ,lijst)

	

#Dit is loper, een meer specifieke versie van stuk
class Loper( Stuk ):
	waarde = 3
	def __init__(self, kleur, plek = Plek () ):
		Stuk.__init__(self, kleur)
		self.plek = plek
		self.wit = "♝"
		self.zwart = "♗"

	#Maak een lijstje van alle plekken op het bord waar dit stuk heen kan
	def MogelijkePlekken(self, bord):
		lijst = []
		maxstappen =  bord.kolommen if bord.kolommen > bord.rijen else bord.rijen
		rechtsboven = [ Plek( self.plek.kolom + i, self.plek.rij + i) for i in range( 1, maxstappen ) ]
		linksboven  = [ Plek( self.plek.kolom - i, self.plek.rij + i) for i in range( 1, maxstappen ) ]
		rechtsonder = [ Plek( self.plek.kolom + i, self.plek.rij - i) for i in range( 1, maxstappen ) ]
		linksonder  = [ Plek( self.plek.kolom - i, self.plek.rij - i) for i in range( 1, maxstappen ) ]
		
		richtingen = [ linksboven, rechtsboven, rechtsonder, linksonder ]
		for richting in richtingen: 
			for stap in richting:
				if not MagNaarPlek( bord, self, stap ):
					break
				lijst.append( stap ) 
		return lijst

#Dit is Koningin, een meer specifieke versie van stuk
class Koningin( Stuk ):
	waarde = 9
	def __init__(self, kleur, plek = Plek () ):
		Stuk.__init__(self, kleur)
		self.plek = plek
		self.wit = "♛"
		self.zwart = "♕"

	def MogelijkePlekken(self, bord):
		lijst = []
		#voor naar beneden en naar boven
		links = [ Plek( self.plek.kolom  - i, self.plek.rij) for i in range( 1, bord.kolommen ) ]
		rechts= [ Plek( self.plek.kolom  + i, self.plek.rij) for i in range( 1, bord.kolommen ) ]
		boven = [ Plek( self.plek.kolom , self.plek.rij + i) for i in range( 1, bord.rijen ) ]
		onder = [ Plek( self.plek.kolom , self.plek.rij - i) for i in range( 1, bord.rijen ) ]

		#voor de schuine stappen
		maxstappen =  bord.kolommen if bord.kolommen > bord.rijen else bord.rijen
		rechtsboven = [ Plek( self.plek.kolom + i, self.plek.rij + i) for i in range( 1, maxstappen ) ]
		linksboven  = [ Plek( self.plek.kolom - i, self.plek.rij + i) for i in range( 1, maxstappen ) ]
		rechtsonder = [ Plek( self.plek.kolom + i, self.plek.rij - i) for i in range( 1, maxstappen ) ]
		linksonder  = [ Plek( self.plek.kolom - i, self.plek.rij - i) for i in range( 1, maxstappen ) ]
		richtingen = [ links, rechts, boven, onder, rechtsboven, linksboven, rechtsonder, linksonder ]
		for richting in richtingen: 
			for stap in richting:
				if not MagNaarPlek( bord, self, stap ):
					break
				lijst.append( stap ) 
		return lijst

#Dit is Koning, een meer specifieke versie van stuk
class Koning( Stuk ):
	waarde = 39
	def __init__(self, kleur, plek = Plek () ):
		Stuk.__init__(self, kleur)
		self.plek = plek
		self.wit = "♚"
		self.zwart = "♔"

	def MogelijkePlekken(self, bord):
		lijst = []

#De richtingen van koning, 
		richtingen = [ 
			Plek( self.plek.kolom - 1, self.plek.rij),
			Plek( self.plek.kolom + 1, self.plek.rij),
			Plek( self.plek.kolom, self.plek.rij + 1),
			Plek( self.plek.kolom, self.plek.rij - 1),
			Plek( self.plek.kolom + 1, self.plek.rij + 1),
			Plek( self.plek.kolom - 1, self.plek.rij + 1),
			Plek( self.plek.kolom + 1, self.plek.rij - 1),
			Plek( self.plek.kolom - 1, self.plek.rij - 1)]

		for stap in richtingen: 
			if MagNaarPlek( bord, self, stap ):
				lijst.append( stap )

		return lijst


#TODO: rokkade
#TODO: Niet naar aangevallen plekken