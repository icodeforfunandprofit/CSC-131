def myMoney(cash=0, debt=0):
	return cash - debt

print(myMoney())
print(myMoney(50))
print(myMoney(120, 50))
print(myMoney(debt=250, cash=25))
