import undetected_chromedriver.v2 as uc
from match import *
from books.bet99 import *
from books.bodog import *
from books.pinnacle import *

from threading import Thread
def comparator(matchesA,matchesB,websiteA,websiteB):
    for matchA,oddsA in matchesA:
        for matchB, oddsB in matchesB:
            if similarTeam(matchA.teamA, matchB.teamA) and similarTeam(matchA.teamB,matchB.teamB):
                if calculateScore(matchA,matchB,oddsA,oddsB):
                    print(websiteA + " " + websiteB + "\n")
                    break
            elif similarTeam(matchA.teamA, matchB.teamB) and similarTeam(matchA.teamB,matchB.teamA):
                swappedMatchB, swappedOddsB = swapTeam(matchB,oddsB)
                if calculateScore(matchA,matchB,swappedMatchB,swappedOddsB):
                    print(websiteA + " " + websiteB + "\n")
                    break

def hockey():
    bet99Matches = bet99Hockey(driver)
    pinnacleMatches = pinnacleHockey(driver)
    bodogMatches = bodogHockey(driver)
    Thread(target=comparator,args=[bet99Matches, pinnacleMatches,"bet99","pinnacle"]).start()
    Thread(target=comparator,args=[bet99Matches,bodogMatches,"bet99","bodog"]).start()
    Thread(target=comparator,args=[bodogMatches,pinnacleMatches,"bodog","pinnacle"]).start()
    print("done hockey")


def basketball():

    bet99Matches = bet99Basketball(driver)
    pinnacleMatches = pinnacleBasketball(driver)
    bodogMatches = bodogBasketball(driver)
    Thread(target=comparator,args=[bet99Matches, pinnacleMatches,"bet99","pinnacle"]).start()
    Thread(target=comparator,args=[bet99Matches,bodogMatches,"bet99","bodog"]).start()
    Thread(target=comparator,args=[bodogMatches,pinnacleMatches,"bodog","pinnacle"]).start()
    print("done basketball")
    
def football():

    bet99Matches = bet99Football(driver)
    pinnacleMatches = pinnacleFootball(driver)
    bodogMatches = bodogFootball(driver)
    Thread(target=comparator,args=[bet99Matches, pinnacleMatches,"bet99","pinnacle"]).start()
    Thread(target=comparator,args=[bet99Matches,bodogMatches,"bet99","bodog"]).start()
    Thread(target=comparator,args=[bodogMatches,pinnacleMatches,"bodog","pinnacle"]).start()
    print("done football")
    
def soccer():
    bet99Matches = bet99Soccer(driver)
    pinnacleMatches = pinnacleSoccer(driver)
    bodogMatches = bodogSoccer(driver)
    Thread(target=comparator,args=[bet99Matches, pinnacleMatches,"bet99","pinnacle"]).start()
    Thread(target=comparator,args=[bet99Matches,bodogMatches,"bet99","bodog"]).start()
    Thread(target=comparator,args=[bodogMatches,pinnacleMatches,"bodog","pinnacle"]).start()
    print("done soccer")

driver = uc.Chrome()
while True:
    try:
        hockey()
    except:
        pass
    try:
        basketball()
    except:
        pass
    try:
        football()
    except:
        pass
    try:
        soccer()
    except:
        pass
# Thread(target=hockey).start()
# Thread(target=basketball).start()
# Thread(target=football).start()
# Thread(target=soccer).start()