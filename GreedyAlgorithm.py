cash=int(input('Enter summ: '))

coinCosts=[3,25,10,5,1]

coinsList=dict()
coinCount=0

coinCosts.sort(reverse=True)

for i in range(0,len(coinCosts)):
    c=cash//coinCosts[i]
    coinCount+=c
    if(c!=0):
        coinsList[coinCosts[i]]=c
    cash=cash%coinCosts[i]


print(coinsList,coinCount)