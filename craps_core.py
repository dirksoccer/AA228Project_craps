from numpy.random import randint as rnd
import qLearningFunctions as ql

#Function to execute next roll and return any rewards earned
def rollTheDice(wager,odds,point = 0):

	#Initialize flag to signal if round is over
	roundOver = 0

	#Initialize results of the round
	winnings = 0

	#Roll 2d6 and return total
	die1 = rnd(1,7)
	die2 = rnd(1,7)
	roll = die1+die2

	#Check for single roll bets
	if roll == 2:
		winnings += wager['snakeeyes']*(odds['snakeeyes']+1)
		winnings += wager['hiLo']*(odds['hiLo']+1)
		winnings += wager['anyCraps']*(odds['anyCraps']+1)
		winnings += wager['cAndE']*(odds['cAndE'][roll]+1)
		winnings += wager['field']*(odds['field'][roll]+1)
		winnings += wager['horn']*(odds['horn'][roll]+1)
		winnings += wager['world']*(odds['world'][roll]+1)

	elif roll == 3:
		winnings += wager['aceDuece']*(odds['aceDuece']+1)
		winnings += wager['anyCraps']*(odds['anyCraps']+1)
		winnings += wager['cAndE']*(odds['cAndE'][roll]+1)
		winnings += wager['field']*(odds['field'][roll]+1)
		winnings += wager['horn']*(odds['horn'][roll]+1)
		winnings += wager['world']*(odds['world'][roll]+1)

	elif roll == 4:
		winnings += wager['field']*(odds['field'][roll]+1)
		winnings += wager['place4']*(odds['place4']+1)
		winnings += wager['buy4']*(odds['buy4']+0.95)
		winnings += wager['lay4']*(odds['lay4']*0.95+1)

		if die1 == die2:
			winnings += wager['hard4']*(odds['hard4']+1)

	elif roll == 5:
		winnings += wager['place5']*(odds['place5']+1)
		winnings += wager['buy5']*(odds['buy5']+0.95)
		winnings += wager['lay5']*(odds['lay5']*0.95+1)

	elif roll == 6:
		winnings += wager['big6']*(odds['big6']+1)
		winnings += wager['place6']*(odds['place6']+1)
		winnings += wager['buy6']*(odds['buy6']+0.95)
		winnings += wager['lay6']*(odds['lay6']*0.95+1)

		if die1 == die2:
			winnings += wager['hard6']*(odds['hard6']+1)

	elif roll == 7:
		winnings += wager['bigRed']*(odds['bigRed']+1)
		winnings += wager['world']*(odds['world'][roll]+1)

	elif roll == 8:
		winnings += wager['big8']*(odds['big8']+1)
		winnings += wager['place8']*(odds['place8']+1)
		winnings += wager['buy8']*(odds['buy8']+0.95)
		winnings += wager['lay8']*(odds['lay8']*0.95+1)

		if die1 == die2:
			winnings += wager['hard8']*(odds['hard8']+1)

	elif roll == 9:
		winnings += wager['field']*(odds['field'][roll]+1)
		winnings += wager['place9']*(odds['place9']+1)
		winnings += wager['buy9']*(odds['buy9']+0.95)
		winnings += wager['lay9']*(odds['lay9']*0.95+1)

	elif roll == 10:
		winnings += wager['field']*(odds['field'][roll]+1)
		winnings += wager['place10']*(odds['place10']+1)
		winnings += wager['buy10']*(odds['buy10']+0.95)
		winnings += wager['lay10']*(odds['lay10']*0.95+1)

		if die1 == die2:
			winnings += wager['hard10']*(odds['hard10']+1)

	elif roll == 11:
		winnings += wager['yoleven']*(odds['yoleven']+1)
		winnings += wager['cAndE']*(odds['cAndE'][roll]+1)
		winnings += wager['field']*(odds['field'][roll]+1)
		winnings += wager['horn']*(odds['horn'][roll]+1)
		winnings += wager['world']*(odds['world'][roll]+1)

	elif roll == 12:
		winnings += wager['boxcars']*(odds['boxcars']+1)
		winnings += wager['hiLo']*(odds['hiLo']+1)
		winnings += wager['cAndE']*(odds['cAndE'][roll]+1)
		winnings += wager['field']*(odds['field'][roll]+1)
		winnings += wager['horn']*(odds['horn'][roll]+1)
		winnings += wager['world']*(odds['world'][roll]+1)


	#Handle "Come Out" roll
	if point == 0:

		#Check for "Natural"
		if roll in [7,11]:

			winnings += wager['pass']*(odds['pass']+1) #Calculate winnings
			roundOver = 1							 #Flag round is over
			return(roll,winnings,roundOver)

		#Check for "Craps"
		elif roll in [2,3,12]:

			winnings += wager['dontPass']*(odds['dontPass']+1)
			roundOver = 1
			return(roll,winnings,roundOver)

		#Establish Point
		else:

			return(roll,winnings,roundOver)

	#Handle "Point" rolls
	else:

		#Check for "Seven-Out"
		if roll == 7:

			winnings += wager['dontPass']*(odds['dontPass']+1)+wager['dontCome']*(odds['dontCome']+1)
			winnings += wager['dontPassOdds']*(odds['dontPassOdds'][point]+1)
			winnings += wager['dontComeOdds']*(odds['dontComeOdds'][point]+1)
			roundOver = 1
			return(roll,winnings,roundOver)

		#Check for "Hit"
		elif roll == point:

			winnings += wager['pass']*(odds['pass']+1)+wager['come']*(odds['come']+1)
			winnings += wager['passOdds']*(odds['passOdds'][point]+1)
			winnings += wager['comeOdds']*(odds['comeOdds'][point]+1)
			roundOver = 1
			return(roll,winnings,roundOver)

		#Continue round
		else:

			return(roll,winnings,roundOver)

#Clear all the wagers that win or lose in a single roll
def clearSingleRollWagers(wager):

	#Clear single roll bets
	for key in ['yoleven','aceDuece','snakeeyes','boxcars','hiLo','anyCraps','cAndE','bigRed','field','horn','world']:
		wager[key] = 0

	return(wager)

#Clear all wagers that only lose when certain things are rolled
def clearMultiRollWagers(wager,roll):

	#Clear multi roll bets based on number rolled
	if roll == 7:

		#Clear bets that lose on a 7
		for key in ['big6','big8','place4','place5','place6','place8','place9','place10','buy4','buy5','buy6','buy8','buy9','buy10']:
			wager[key] = 0

	#Clear 'Lay' and 'Hard Way' bets
	#	Note: if roll was done 'Hard Way', the winnings were already collected
	if roll == 4:
		wager['hard4'] == 0
		wager['lay4'] == 0
	
	if roll == 5:
		wager['lay5'] == 0

	if roll == 6:
		wager['lay6'] == 0
		wager['hard6'] == 0

	if roll == 8:
		wager['lay8'] == 0
		wager['hard8'] == 0

	if roll == 9:
		wager['lay9'] == 0

	if roll == 10:
		wager['lay10'] == 0
		wager['hard10'] == 0

	return(wager)


#Function to finish round with current wager
def finishRound(wager,odds,point = 0):

	#Execute first roll
	#	Separate to handle single roll bets
	roll,winnings,roundOver = rollTheDice(wager.copy(),odds,point)

	#	Clear single roll bets (winnings already included in winnings)
	wager = clearSingleRollWagers(wager.copy())

	#	Clear multi roll bets
	wager = clearMultiRollWagers(wager.copy(),roll)

	#If this first roll was the come out roll, establish point
	if point == 0:
		point = roll

	numRolls = 0

	#Finish round
	#	Note: if first roll ended round this section is skipped
	while not roundOver:

		#Roll the dice again
		roll,newWinnings,roundOver = rollTheDice(wager.copy(),odds,point)

		#Update winnings
		winnings += newWinnings

		#Clear multi roll bets
		wager = clearMultiRollWagers(wager.copy(),roll)

		#Count number of rolls (come out roll doesn't count)
		numRolls += 1

	return(wager,winnings,point,numRolls)

#Determine best action step by step via simulation
def findBestBruteForce(wager,odds,passDontPassBet = 5,pointBet = 10,numRounds = 100):

	#Initialize accumulating variables
	netWinnings = 0
	numRolls = 0

	tempWinnings = 0
	tempKey = ''

	#Try 'Pass' and 'Don't Pass' Bets
	for key in ['pass','dontPass']:

		#Place bet
		wager[key] = passDontPassBet

		#Simulate 1000 rounds and get avg winnings
		avgWinnings = 0
		for i in range(numRounds):
			winnings,point,numRolls = finishRound(wager.copy(),odds)[1:4]
			avgWinnings += winnings/numRounds

		#Save best of the 2 bets
		if avgWinnings > tempWinnings:
			tempWinnings = avgWinnings
			tempKey = key

		#Remove the bet
		wager[key] = 0

	#Place the better bet
	wager[tempKey] = passDontPassBet
	netWinnings -= passDontPassBet

	#Simulate the roll for real
	roll,addedWinnings,roundOver = rollTheDice(wager.copy(),odds)
	point = roll
	#print(point,roundOver)
	#print(tempKey)
	netWinnings += addedWinnings

	#Simulate the rest of the round
	while not roundOver:

		#Set a baseline of placing no additional bet
		for i in range(numRounds):
			addedWinnings = finishRound(wager.copy(),odds,point)[1]
			tempWinnings += addedWinnings/numRounds
		tempKey = ''

		#Try each bet that isn't 'Pass' or 'Don't Pass'
		for key in [x for x in wager.keys() if x not in ['pass','dontPass']]:

			#Place bet
			wager[key] = pointBet

			#Simulate 1000 rounds and get avg winnings
			avgWinnings = 0
			for i in range(numRounds):
				addedWinnings = finishRound(wager.copy(),odds,point)[1]
				avgWinnings += addedWinnings/numRounds

			#Save best bet
			if avgWinnings > tempWinnings:
				tempWinnings = avgWinnings
				tempKey = key

			#Remove the bet
			wager[key] = 0

		#Place the best bet
		if tempKey != '':
			wager[tempKey] = pointBet
			netWinnings -= pointBet
			#print(tempKey)

		#Simulate the next roll for real
		roll,addedWinnings,roundOver = rollTheDice(wager.copy(),odds,point)
		netWinnings += addedWinnings
		numRolls += 1

	#print('Result:',point,netWinnings,numRolls)
	#print('----------------')

	return(netWinnings)

#Determine best action step by step via simulation
def findBestBruteForceSingleWager(wager,odds,qFrame,passDontPassBet = 5,pointBet = 10,numRounds = 100):

	#Initialize accumulating variables
	netWinnings = 0
	numRolls = 0

	tempWinnings = 0
	tempKey = ''

	#Try 'Pass' and 'Don't Pass' Bets
	for key in ['pass','dontPass']:

		#Place bet
		wager[key] = passDontPassBet

		#Simulate 1000 rounds and get avg winnings
		avgWinnings = 0
		for i in range(numRounds):
			winnings,point,numRolls = finishRound(wager.copy(),odds)[1:4]
			avgWinnings += winnings/numRounds

		#Save best of the 2 bets
		if avgWinnings > tempWinnings:
			tempWinnings = avgWinnings
			tempKey = key

		#Remove the bet
		wager[key] = 0

	#Place the better bet
	wager[tempKey] = passDontPassBet
	netWinnings -= passDontPassBet

	#Simulate the roll for real
	roll,addedWinnings,roundOver = rollTheDice(wager.copy(),odds)
	point = roll
	netWinnings += addedWinnings
	#print(point,roundOver)
	#print(tempKey)


	if not roundOver:
		#Set a baseline of placing no additional bet
		for i in range(numRounds):
			addedWinnings = finishRound(wager.copy(),odds,point)[1]
			tempWinnings += addedWinnings/numRounds
		tempKey = ''

		#Try each bet that isn't 'Pass' or 'Don't Pass'
		for key in [x for x in wager.keys() if x not in ['pass','dontPass']]:

			#Place bet
			wager[key] = pointBet

			#Simulate 1000 rounds and get avg winnings
			avgWinnings = 0
			for i in range(numRounds):
				addedWinnings = finishRound(wager.copy(),odds,point)[1]
				avgWinnings += addedWinnings/numRounds

			#Save best bet
			if avgWinnings > tempWinnings:
				tempWinnings = avgWinnings
				tempKey = key

			#Remove the bet
			wager[key] = 0

		#Place the best bet
		if tempKey != '':
			wager[tempKey] = pointBet
			netWinnings -= pointBet
			#print(tempKey)

		#Simulate the rest of the round for real
		addedWinnings = finishRound(wager.copy(),odds,point)[1]
		netWinnings += addedWinnings

	qFrame = ql.updateQFrame(qFrame,point,wager,netWinnings)

	#print('Result:',point,netWinnings,numRolls)
	#print('----------------')

	return(netWinnings,qFrame)


#Handle execution of secondary functions
def main():

	#Initialize wager dictionary
	wager = {'pass':0,
			'dontPass':0,
			'passOdds':0,
			'dontPassOdds':0,
			'come':0,
			'dontCome':0,
			'comeOdds':0,
			'dontComeOdds':0,
			'place4':0,
			'place5':0,
			'place6':0,
			'place8':0,
			'place9':0,
			'place10':0,
			'buy4':0,
			'buy5':0,
			'buy6':0,
			'buy8':0,
			'buy9':0,
			'buy10':0,
			'lay4':0,
			'lay5':0,
			'lay6':0,
			'lay8':0,
			'lay9':0,
			'lay10':0,
			'putPass':0,
			'putCome':0,
			'hard4':0,
			'hard6':0,
			'hard8':0,
			'hard10':0,
			'big6':0,
			'big8':0,
			'snakeeyes':0,
			'aceDuece':0,
			'yoleven':0,
			'boxcars':0,
			'hiLo':0,
			'anyCraps':0,
			'cAndE':0,
			'bigRed':0,
			'horn':0,
			'world':0,
			'field':0}

	#Initialize odds dictionary
	odds = {'pass':1,
			'dontPass':1,
			'passOdds':{4:2,5:1.5,6:1.2,8:1.2,9:1.5,10:2},
			'dontPassOdds':{4:.5,5:(2.0/3),6:(5.0/6),8:(5.0/6),9:(2.0/3),10:.5},
			'come':1,
			'dontCome':1,
			'comeOdds':{4:2,5:1.5,6:1.2,8:1.2,9:1.5,10:2},
			'dontComeOdds':{4:.5,5:(2.0/3),6:(5.0/6),8:(5.0/6),9:(2.0/3),10:.5},
			'place4':1.8,
			'place5':1.4,
			'place6':(7.0/6),
			'place8':(7.0/6),
			'place9':1.4,
			'place10':1.8,
			'buy4':2,
			'buy5':1.5,
			'buy6':1.2,
			'buy8':1.2,
			'buy9':1.5,
			'buy10':2,
			'lay4':.5,
			'lay5':(2.0/3),
			'lay6':(5.0/6),
			'lay8':(5.0/6),
			'lay9':(2.0/3),
			'lay10':.5,
			'putPass':1,
			'putCome':1,
			'hard4':7,
			'hard6':9,
			'hard8':9,
			'hard10':7,
			'big6':1,
			'big8':1,
			'snakeeyes':30,
			'aceDuece':15,
			'yoleven':15,
			'boxcars':30,
			'hiLo':15,
			'anyCraps':7,
			'cAndE':{2:3,3:3,12:3,11:7},
			'bigRed':4,
			'horn':{2:(27.0/4),3:3,11:3,12:(27.0/4)},
			'world':{2:(26.0/5),3:(11.0/5),7:0,11:(11.0/5),12:(26.0/5)},
			'field':{2:2,3:1,4:1,9:1,10:1,11:1,12:2}}

	#Initialize q Learning data frame
	qFrame = ql.initializeQFrame()

	for passDontPassBet in range(5,30,5):

		for pointBet in range(5,30,5):

			print('Pass Bet: ',passDontPassBet,' -- Point Bet: ',pointBet)

			avgGrossWinnings = 0

			for i in range(1000):
				
				grossWinnings = 100

				for i in range(100):

					addedWinnings,qFrame = findBestBruteForceSingleWager(wager,odds,qFrame,passDontPassBet,pointBet)

					if grossWinnings < 75 and addedWinnings < 0:
						break

					if grossWinnings > 150 and addedWinnings < 0:
						break

					grossWinnings += addedWinnings

				#print(grossWinnings)
				#print('******************')

				avgGrossWinnings += grossWinnings/1000

			print(avgGrossWinnings)
			print('--------------------')

	ql.writeQFrame('qLearningData2.csv',qFrame)
	

if __name__ == '__main__':
    main()