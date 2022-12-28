import time
import undetected_chromedriver.v2 as uc
from match import *
from collections import defaultdict
from books.bet99 import *
from books.bodog import *
from books.pinnacle import *
driver = uc.Chrome()

def hockey():
    bet99Matches = bet99Hockey(driver)
    print("Scraped bet99")
    pinnacleMatches = pinnacleHockey(driver)
    print("Scraped pinnacle")
    bodogMatches = bodogHockey(driver)
    print("Scraped bodog")
    for matchA in bet99Matches:
        print(matchA[0])
    print("-------")
    for matchB in pinnacleMatches:
        print(matchB[0])
    print("+++++++++++-")
    for matchC in bodogMatches:
        print(matchC[0])
        
    for matchA in bet99Matches:
        for matchB in pinnacleMatches:
            for matchC in bodogMatches:
                if matchA[0].similar(matchB[0]) and matchB[0].similar(matchC[0]):
                    calculateScore(matchA[0],[matchA[1],matchB[1]])
    print("done :)")

hockey()
def basketball():
    pinnacleMatches = bet99Basketball()
    print("Scraped pinnacle")
    bodogMatches = bodogBasketball()
    print("Scraped bodog")
    for matchA in pinnacleMatches:
        for matchB in bodogMatches:
            if matchA[0].similar(matchB[0]):
                calculateScore(matchA[0],[matchA[1],matchB[1]])
    print("done :)")
    


def football():
    pinnacleMatches = bet99Football()
    print("Scraped pinnacle")
    bodogMatches = bodogFootball()
    print("Scraped bodog")
    for matchA in pinnacleMatches:
        for matchB in bodogMatches:
            if matchA[0].similar(matchB[0]):
                calculateScore(matchA[0],[matchA[1],matchB[1]])
    print("done :)")
    
def soccer():
    bet99Matches = bet99Soccer()
    print("Scraped bet99Matches")
    bodogMatches = bodogSoccer()
    print("Scraped bodog")
    for matchA in bet99Matches:
        for matchB in bodogMatches:
            if matchA[0].similar(matchB[0]):
                print(matchA[0])
                print(matchA[1].__dict__)
                print(matchB[1].__dict__)
                calculateScore(matchA[0],[matchA[1],matchB[1]])

    print("done :)")
#hockey()
#basketball()
#football()
#soccer()

time.sleep(1000)