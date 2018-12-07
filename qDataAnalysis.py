import pandas as pd
import qLearningFunctions as qlf
import matplotlib.pyplot as plt

def main():

	qData = qlf.initializeQFrame('qLearningData3.csv')

	#Win percentage of 'Pass' and 'Dont Pass' bets on Come Out roll
	print('Come out roll wins/losses:')
	dontPass_711losses = sum(qData[(qData.DontPass != 0) & (qData.betName == 'None') & (qData.Point.isin([2,3,7,11,12])) & (qData.Q < 0)].N)
	dontPass_crapOutWins = sum(qData[(qData.DontPass != 0) & (qData.betName == 'None') & (qData.Point.isin([2,3,7,11,12])) & (qData.Q > 0)].N)
	print('Dont Pass Win Pct: ',dontPass_crapOutWins/(dontPass_crapOutWins+dontPass_711losses))

	pass_711wins = sum(qData[(qData.Pass != 0) & (qData.betName == 'None') & (qData.Point.isin([2,3,7,11,12])) & (qData.Q > 0)].N)
	pass_crapOutlosses = sum(qData[(qData.Pass != 0) & (qData.betName == 'None') & (qData.Point.isin([2,3,7,11,12])) & (qData.Q < 0)].N)
	print('Pass Win Pct: ',pass_711wins/(pass_711wins+pass_crapOutlosses))

	#Win percentage of 'Pass' and 'Dont Pass' bets once point established (with no other bet laid)
	print('\nPoint rolls wins/losses:')
	dontPass_roundLosses = sum(.5*qData[(qData.DontPass != 0) & (qData.betName == 'None') & (~qData.Point.isin([2,3,7,11,12]))].N*(1 - qData[(qData.DontPass != 0) & (qData.betName == 'None') & (~qData.Point.isin([2,3,7,11,12]))].Q/qData[(qData.DontPass != 0) & (qData.betName == 'None') & (~qData.Point.isin([2,3,7,11,12]))].DontPass))
	dontPass_roundWins = sum(.5*qData[(qData.DontPass != 0) & (qData.betName == 'None') & (~qData.Point.isin([2,3,7,11,12]))].N*(1 + qData[(qData.DontPass != 0) & (qData.betName == 'None') & (~qData.Point.isin([2,3,7,11,12]))].Q/qData[(qData.DontPass != 0) & (qData.betName == 'None') & (~qData.Point.isin([2,3,7,11,12]))].DontPass))
	print(dontPass_roundLosses)
	print(dontPass_roundWins)
	print('Dont Pass Win Pct: ',dontPass_roundWins/(dontPass_roundWins+dontPass_roundLosses))

	pass_roundWins = sum(.5*qData[(qData.Pass != 0) & (qData.betName == 'None') & (~qData.Point.isin([2,3,7,11,12]))].N*(1 + qData[(qData.Pass != 0) & (qData.betName == 'None') & (~qData.Point.isin([2,3,7,11,12]))].Q/qData[(qData.Pass != 0) & (qData.betName == 'None') & (~qData.Point.isin([2,3,7,11,12]))].Pass))
	pass_roundLosses = sum(.5*qData[(qData.Pass != 0) & (qData.betName == 'None') & (~qData.Point.isin([2,3,7,11,12]))].N*(1 - qData[(qData.Pass != 0) & (qData.betName == 'None') & (~qData.Point.isin([2,3,7,11,12]))].Q/qData[(qData.Pass != 0) & (qData.betName == 'None') & (~qData.Point.isin([2,3,7,11,12]))].Pass))
	print(pass_roundWins)
	print(pass_roundLosses)
	print('Pass Win Pct: ',pass_roundWins/(pass_roundWins+pass_roundLosses))

	#Win percentag of 'Pass' and 'Dont Pass' bets overall
	print('\nOverall wins/losses:')
	print('Dont Pass Win Pct: ',(dontPass_roundWins+dontPass_crapOutWins)/(dontPass_711losses+dontPass_crapOutWins+dontPass_roundWins+dontPass_roundLosses))
	print('Pass Win Pct: ',(pass_roundWins+pass_711wins)/(pass_roundWins+pass_roundLosses+pass_711wins+pass_crapOutlosses))

	#Net return on 'Pass' and 'Dont Pass' bets (alone)
	print('\nOverall return per round:')
	print('Dont Pass return: ',sum(qData[(qData.DontPass != 0) & (qData.betName == 'None')].Q*qData[(qData.DontPass != 0) & (qData.betName == 'None')].N)/sum(qData[(qData.DontPass != 0) & (qData.betName == 'None')].N))
	print('Pass return: ',sum(qData[(qData.Pass != 0) & (qData.betName == 'None')].Q*qData[(qData.Pass != 0) & (qData.betName == 'None')].N)/sum(qData[(qData.Pass != 0) & (qData.betName == 'None')].N))

	#Most common bets during round
	print('\nMost common bet after come out roll:')
	print(qData[(~qData.Point.isin([2,3,7,11,12]))].sort_values(by='N',ascending=False).head(25))

	print('\nMost common bet after come out roll [not None]:')
	print(qData[(qData.betName != 'None') & (~qData.Point.isin([2,3,7,11,12]))].sort_values(by='N',ascending=False).head(25))

	print('\nMost common bet after come out roll [not boxcars, snakeeyes, or None]:')
	print(qData[(~qData.betName.isin(['boxcars','snakeeyes','None'])) & (~qData.Point.isin([2,3,7,11,12]))].sort_values(by='N',ascending=False).head(25))

	print('\nBet with best return [excluding N < 1% of bets]:')
	print(qData[(qData.N > 3600)].sort_values(by='Q',ascending=False).head(25))

	print(sum(qData.N)*0.01)

	print('\n')
	tempData = qData.copy()
	tempData['OpeningBet'] = tempData.Pass+tempData.DontPass
	for i in range(5,26,5):
		title = 'Top 10 Most Frequent Bets\n($'+str(i)+' buy in)'
		plotData = tempData[(tempData.OpeningBet == i)].groupby(['OpeningBet','betName','betAmt'])[['N']].sum().sort_values(by='N',ascending=False).head(10).reset_index()
		plotData['sectionTitle'] = plotData['betName']+' '+plotData['betAmt'].map(str)
		plotData.plot.pie(title=title,y='N',labels=plotData['sectionTitle'],legend=False)
		plt.savefig('popularBets_opening'+str(i)+'_pie.png')
		plotData.plot.bar(title=title,y='N',x='sectionTitle',legend=False)
		plt.savefig('popularBets_opening'+str(i)+'_bar.png')



if __name__ == '__main__':
    main()