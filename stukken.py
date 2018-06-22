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

	return ( k, r )

def VanPlekNaarTekst( plek ):
	return chr( ord("A") + plek[0] ) + str( plek[1] + 1)


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

	def __init__(self, kleur ):
		Stuk.__init__(self, kleur)
		self.wit = "♟"
		self.zwart = "♙"
	
	# Hier een lijst met alle mogelijke plekken waar
	# een pion heen gezet kan worden.
	def MogelijkePlekken(self, van, bord):
		lijst = []
		#Dit is voor de witte pionnen
		if self.kleur == Kleur.WIT:
			p = ( van[0], van[1] +1 )
			if bord.StukOpPlek(p) == None:
				lijst.append(p)
				#Pion in eersten zet mogelijk twee vooruit. 
				if( p[1] == 2 ):
					p = ( p[0], 3 ) 
					if bord.StukOpPlek(p) == None:
						lijst.append(p)
			#De schuine zet vooruit als de witte pion slaat 		
			schuin = [
				( van[0]+1, van[1] +1 ),
				( van[0]-1, van[1] +1 )
			]

			for p in schuin:
				slaan = bord.StukOpPlek(p)
				if slaan != None: 
					if slaan.kleur == Kleur.ZWART:
						lijst.append(p)


		else:
			#voor de zwarte stukken
			p = ( van[0], van[1] -1 )
			if bord.StukOpPlek(p) == None:
				lijst.append(p)
				#Pion in eerste zet mogelijk twee vooruit
				if( p[1] == 5 ):
					p = ( p[0], 4 ) 
					if bord.StukOpPlek(p) == None:
						lijst.append(p)
			#De schuine zet vooruit als de zwarte pion slaat
			schuin = [
				( van[0]+1, van[1] -1 ),
				( van[0]-1, van[1] -1 )
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
	def __init__(self, kleur ):
		Stuk.__init__(self, kleur)
		self.wit = "♜"
		self.zwart = "♖"
	
	def MogelijkePlekken(self, van, bord):
		lijst = []
		links = [ ( van[0]  - i, van[1]) for i in range( 1, bord.kolommen ) ]
		rechts= [ ( van[0]  + i, van[1]) for i in range( 1, bord.kolommen ) ]
		boven = [ ( van[0] , van[1] + i) for i in range( 1, bord.rijen  ) ]
		onder = [ ( van[0] , van[1] - i) for i in range( 1, bord.rijen  ) ]
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
	def __init__(self, kleur ):
		Stuk.__init__(self, kleur)
		self.wit = "♞"
		self.zwart = "♘"


	#lijst met de mo gelijke zetten van het paard
	def MogelijkePlekken(self, van, bord ):
		lijst = [
			( van[0]+1, van[1] +2 ),
			( van[0]-1, van[1] +2 ),
			( van[0]+1, van[1] -2 ),
			( van[0]-1, van[1] -2 ),
			( van[0]+2, van[1] +1 ),
			( van[0]+2, van[1] -1 ),
			( van[0]-2, van[1] +1 ),
			( van[0]-2, van[1] -1 )
		]
		# Ingewikkelde functie: eerst geef je bord mee. Dan
		# filter gebruikt functie MagNaarPlek om de lijst aan te
		#vullen met wat mag
		
		return filter( lambda p: MagNaarPlek( bord, self, p ), lijst)

	

#Dit is loper, een meer specifieke versie van stuk
class Loper( Stuk ):
	waarde = 3
	def __init__(self, kleur ):
		Stuk.__init__(self, kleur)
		self.wit = "♝"
		self.zwart = "♗"

	#Maak een lijstje van alle plekken op het bord waar dit stuk heen kan
	def MogelijkePlekken(self, van, bord):
		lijst = []
		maxstappen =  bord.kolommen if bord.kolommen > bord.rijen else bord.rijen
		rechtsboven = [ ( van[0] + i, van[1] + i) for i in range( 1, maxstappen ) ]
		linksboven  = [ ( van[0] - i, van[1] + i) for i in range( 1, maxstappen ) ]
		rechtsonder = [ ( van[0] + i, van[1] - i) for i in range( 1, maxstappen ) ]
		linksonder  = [ ( van[0] - i, van[1] - i) for i in range( 1, maxstappen ) ]
		
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
	def __init__(self, kleur ):
		Stuk.__init__(self, kleur)
		self.wit = "♛"
		self.zwart = "♕"

	def MogelijkePlekken(self, van, bord):
		lijst = []
		#voor naar beneden en naar boven
		links = [ ( van[0]  - i, van[1]) for i in range( 1, bord.kolommen ) ]
		rechts= [ ( van[0]  + i, van[1]) for i in range( 1, bord.kolommen ) ]
		boven = [ ( van[0] , van[1] + i) for i in range( 1, bord.rijen ) ]
		onder = [ ( van[0] , van[1] - i) for i in range( 1, bord.rijen ) ]

		#voor de schuine stappen
		maxstappen =  bord.kolommen if bord.kolommen > bord.rijen else bord.rijen
		rechtsboven = [ ( van[0] + i, van[1] + i) for i in range( 1, maxstappen ) ]
		linksboven  = [ ( van[0] - i, van[1] + i) for i in range( 1, maxstappen ) ]
		rechtsonder = [ ( van[0] + i, van[1] - i) for i in range( 1, maxstappen ) ]
		linksonder  = [ ( van[0] - i, van[1] - i) for i in range( 1, maxstappen ) ]
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
	def __init__(self, kleur ):
		Stuk.__init__(self, kleur)
		self.wit = "♚"
		self.zwart = "♔"

	def MogelijkePlekken(self, van, bord):
		lijst = []

#De richtingen van koning, 
		richtingen = [ 
			( van[0] - 1, van[1]),
			( van[0] + 1, van[1]),
			( van[0], van[1] + 1),
			( van[0], van[1] - 1),
			( van[0] + 1, van[1] + 1),
			( van[0] - 1, van[1] + 1),
			( van[0] + 1, van[1] - 1),
			( van[0] - 1, van[1] - 1)]

		for stap in richtingen: 
			if MagNaarPlek( bord, self, stap ):
				lijst.append( stap )

		return lijst


#TODO: rokkade
#TODO: Niet naar aangevallen plekken