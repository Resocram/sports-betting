
import random
freeCash = 100
actualCash = 0
betAmount = 20
import time 
print("Free Balance: " + str(freeCash) + " Actual Balance: " + str(actualCash))
while freeCash + actualCash > betAmount and freeCash != 0:
    total = freeCash + actualCash
    freePercentage = freeCash/total
    actualPercentage = actualCash/total
    freeBetAmount = round(freePercentage * betAmount,2)
    print(freeBetAmount)
    actualBetAmount = round(actualPercentage * betAmount,2)
    print(actualBetAmount)
    odds = random.randint(1,10)
    # 2.5 odds [5,6,7,8,9,10] i lose=
    freeCash = round(freeCash - freeBetAmount,2)
    actualCash = round(actualCash - actualBetAmount,2)
    
    if odds <= 4:
        print("Won")
        actualCash += round(actualBetAmount * 2.5 + freeBetAmount * 1.5,2)
    else:
        print("Lost")
    print("Free Balance: " + str(freeCash) + " Actual Balance: " + str(actualCash))
    
    