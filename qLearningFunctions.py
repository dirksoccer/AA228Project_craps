import pandas as pd

def updateQFrame(qFrame,point,wager,reward):

	#Extract 'Pass/Dont Pass' bet from wager
	passBet = wager['pass']
	dontPassBet = wager['dontPass']

	betName = 'None'
	betAmt = 0

	#Extract other bet and key
	for key in [x for x in wager.keys() if x not in ['pass','dontPass']]:

		if wager[key] != 0:

			betName = key
			betAmt = wager[key]

	#Get count and Q from qFrame if present
	try:
		currentQ = qFrame[(qFrame.Point == point) & (qFrame.Pass == passBet) & (qFrame.DontPass == dontPassBet) & (qFrame.betName == betName) & (qFrame.betAmt == betAmt)].Q.item()
		currentN = qFrame[(qFrame.Point == point) & (qFrame.Pass == passBet) & (qFrame.DontPass == dontPassBet) & (qFrame.betName == betName) & (qFrame.betAmt == betAmt)].N.item()

		newN = currentN+1
		newQ = currentQ + (1.0/newN)*(reward-currentQ)

		qFrame.loc[(qFrame.Point == point) & (qFrame.Pass == passBet) & (qFrame.DontPass == dontPassBet) & (qFrame.betName == betName) & (qFrame.betAmt == betAmt),'Q'] = newQ
		qFrame.loc[(qFrame.Point == point) & (qFrame.Pass == passBet) & (qFrame.DontPass == dontPassBet) & (qFrame.betName == betName) & (qFrame.betAmt == betAmt),'N'] = newN

	#If row doesn't exist, initialize
	except:
		qFrame = qFrame.append({'Point':point,'Pass':passBet,'DontPass':dontPassBet,'betName':betName,'betAmt':betAmt,'Q':reward,'N':1},ignore_index=True)

	return(qFrame)

def writeQFrame(outFileName,qFrame):
	qFrame.to_csv(outFileName)

def initializeQFrame(infile = None):

	#Read qFrame from file if called for
	if infile:
		qFrame = pd.read_csv(infile)

	else:
		#Initialize qFrame
		qFrame = pd.DataFrame(columns = ['Point','Pass','DontPass','betName','betAmt','Q','N'])

	return(qFrame)