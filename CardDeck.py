
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
	def __init__(self, suit, rank, value):
		self.suit = suit
		self.rank = rank
		self.value = value

	def __str__(self, suit, rank):
		print ('{} of {}'.format(rank,suit))

class Deck:
	myDeck = {}
	def __init__(self):
		self.suits = suits
		self.ranks = ranks
		self.values = values
		
	def CreateDeck(self):
		'''
		Function to Create the deck of cards
		'''
		for suit in self.suits:
			for rank in self.ranks:
				for rank in self.values:
					Deck.myDeck.update({'{} of {}'.format(rank, suit): values[rank]}) 
				

	def ShuffleDeck(self,myDeck):
		'''
		Function to shuffle the deck of cards
		'''

		a1 = list(self.myDeck.items())
		random.shuffle(a1)
		self.myDeck = dict(a1)

		# for card, value in self.myDeck.items():
		# 	print(card, value)	

