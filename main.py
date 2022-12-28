import time
import undetected_chromedriver.v2 as uc
from match import *
from collections import defaultdict
from books.bet99 import *
from books.bodog import *
from books.pinnacle import *
driver = uc.Chrome()

def comparator(matchesA,matchesB):
    for matchA,oddsA in matchesA:
        for matchB, oddsB in matchesB:
            if matchA.similar(matchB):
                calculateScore(matchA,matchB,oddsA,oddsB)

def hockey():
    bet99Matches = bet99Hockey(driver)
    pinnacleMatches = pinnacleHockey(driver)
    bodogMatches = bodogHockey(driver)
    comparator(bet99Matches,pinnacleMatches)
    comparator(bet99Matches,bodogMatches)
    comparator(bodogMatches,pinnacleMatches)
    print("done :)")


def basketball():
    bet99Matches = bet99Basketball(driver)
    pinnacleMatches = pinnacleBasketball(driver)
    bodogMatches = bodogBasketball(driver)
    comparator(bet99Matches,pinnacleMatches)
    comparator(bet99Matches,bodogMatches)
    comparator(bodogMatches,pinnacleMatches)
    print("done :)")
    
def football():
    bet99Matches = bet99Football(driver)
    pinnacleMatches = pinnacleFootball(driver)
    bodogMatches = bodogFootball(driver)
    comparator(bet99Matches,pinnacleMatches)
    comparator(bet99Matches,bodogMatches)
    comparator(bodogMatches,pinnacleMatches)
    print("done :)")
    
def soccer():
    bet99Matches = bet99Soccer(driver)
    pinnacleMatches = pinnacleSoccer(driver)
    bodogMatches = bodogSoccer(driver)
    comparator(bet99Matches,pinnacleMatches)
    comparator(bet99Matches,bodogMatches)
    comparator(bodogMatches,pinnacleMatches)
    print("done :)")
hockey()
basketball()
football()
soccer()
