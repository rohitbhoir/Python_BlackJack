from CardDeck import Deck


startGame = True
move='Player'
playertotal = 0
dealertotal = 0

class Player():
	"""docstring for ClassName"""
	def __init__(self, playerType, mycards, points=0):
		self.playerType = playerType
		self.mycards = mycards
		self.points = points

	def dealCards(self, carddeck, noofcards):
		# self.mycards = mycards
		# print('current cards ', self.mycards)
		tempcards={}
		for key, value in carddeck.items():
			if noofcards >= 1:
				tempcards.update({key:value})
				noofcards -= 1
			self.mycards.update(tempcards.copy())

		for key in tempcards:
			if key in carddeck:
				carddeck.pop(key)
		
		tempcards.clear()

	def displayCards(self):
		print ('{}'.format(self.playerType), self.mycards)

	def calpoints(self):
		self.points=0
		for key, value in self.mycards.items():
			self.points += value
		print('{} Points: {}'.format(self.playerType, self.points)) 
		
		
class GameManager():
	"""docstring for GameManager"""
	def __init__(self, deck, player, dealer):	
		startGame = True
		move = 'Player'
		self.deck = deck
		self.player = player
		self.dealer = dealer
		deck.CreateDeck()
		deck.ShuffleDeck(d.myDeck)

		#Deal player and Dealer 2 cards
		dealer.dealCards(carddeck=d.myDeck,noofcards=2)
		dealer.displayCards()
		dealer.calpoints()

		player.dealCards(carddeck=d.myDeck,noofcards=2)
		player.displayCards()
		player.calpoints()

		
		
	def switchMove(self, move):
		self.move = move
		move = 'Player' if move == 'Dealer' else 'Dealer'
	

d = Deck()
#Create Player and Dealer
player = Player(playerType = 'Card Player', mycards={})
dealer = Player(playerType = 'Dealer', mycards={})
g = GameManager(deck=d,player=player, dealer=dealer)
passes = 0



while startGame:

	if move == 'Player':	
		playermove = input('Choose a move: (H)it (S)tay: ')
		# insert validation for input here
		# checkMove(playermove=playermove, move=move)
		if playermove.lower() == 'h':
			player.dealCards(carddeck=d.myDeck,noofcards=1)
			player.displayCards()
			player.calpoints()
			if(player.points > 21):
				print(' Player has {}, Dealer Wins!!!'.format(player.points))
				startGame=False
				break;
		elif playermove.lower() == 's':
			passes += 1
			print('Player Passes.....')
			move = 'Dealer'
			continue
		else:
			print('Please enter a valid input')
			continue
	elif move=='Dealer':
		if dealer.points <= 17:
			print('Dealer takes a card...')
			dealer.dealCards(carddeck=d.myDeck,noofcards=1)
			dealer.displayCards()
			dealer.calpoints()
			if(dealer.points > 21):
				print(' Dealer has {}, Player Wins!!!'.format(dealer.points))
				startGame=False
				break;
		else:
			passes += 1
			print ('Dealer Passes.....')
			move='Player'

	if passes >= 2:
		if player.points > dealer.points:
			print('Player Wins!!!')
		else:
			print('Dealer Wins!!!')

		startGame = False
			


	

