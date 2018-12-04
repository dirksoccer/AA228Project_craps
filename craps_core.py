from numpy.random import randint as rnd

#Function to execute next roll and return any rewards earned
def rollTheDice(wager,odds,point = 0):

	#Initialize flag to signal if round is over
	roundOver = 0

	#Roll 2d6 and return total
	roll = rnd(1,7)+rnd(1,7)

	#Handle "Come Out" roll
	if point == 0:

		#Check for "Natural"
		if roll in [7,11]:

			result = wager['pass']-wager['dontPass'] #Calculate winnings
			roundOver = 1							 #Flag round is over
			return(roll,result,roundOver)

		#Check for "Craps"
		elif roll in [2,3,12]:

			result = wager['dontPass']-wager['pass']
			roundOver = 1
			return(roll,result,roundOver)

		#Establish Point
		else:
			result = 0
			return(roll,result,roundOver)

	#Handle "Point" rolls
	else:

		#Check for "Seven-Out"
		if roll == 7:

			result = wager['dontPass']-wager['pass']+wager['dontCome']-wager['come']
			roundOver = 1
			return(roll,result,roundOver)

		#Check for "Hit"
		elif roll == point:

			result = wager['pass']-wager['dontPass']
			roundOver = 1
			return(roll,result,roundOver)


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
			'putPass':0,
			'putCome':0,
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

	rollTheDice(wager,odds)