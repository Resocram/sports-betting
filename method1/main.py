import undetected_chromedriver.v2 as uc
from match import *
from books.bet99 import *
from books.bodog import *
from books.pinnacle import *
from books.bet365 import *
from books.stake import *
from selenium import webdriver
from collections import defaultdict
from leagues.league import *

websites = ["stake", "bet365", "bet99", "bodog", "pinnacle"]

def comparator(matches):
    for match in matches:
        odds = matches[match]
        if len(odds) > 1:
            calculateScore(match, odds) 

def compute(league, websites, functions):
    matches = defaultdict(pd.DataFrame)
    for i in range(len(functions)):
        try:
            functions[i](driver,matches,league.teams,league.urls[i])
        except:
            print("Did not do " + league.name + " on " + websites[i])
    return matches

def hockey(league):
    functions = [stakeHockey, bet365Hockey, bet99Hockey, bodogHockey,pinnacleHockey]
    matches = compute(league,websites,functions)
    comparator(matches)
    print("done " + league.name)
    return matches

def basketball(league):
    functions = [stakeBasketball, bet365Basketball, bet99Basketball, bodogBasketball,pinnacleBasketball]
    matches = compute(league,websites,functions)
    comparator(matches)
    print("done " + league.name)
    return matches
    
def football(league):
    functions = [stakeFootball, bet365Football, bet99Football, bodogFootball, pinnacleFootball]
    matches = compute(league,websites,functions)
    comparator(matches)
    print("done " + league.name)
    return matches

def soccer(league):
    functions = [stakeSoccer, bet365Soccer, bet99Soccer, bodogSoccer, pinnacleSoccer]
    matches = compute(league,websites,functions)
    comparator(matches)
    print("done " + league.name)
    return matches

op = webdriver.ChromeOptions()

driver = uc.Chrome(options=op)
driver.set_window_size(1440, 1440)

while True:
    hockey(LIIGA)
    hockey(SHL)
    basketball(EUROLEAGUE)
    hockey(KHL)
    soccer(LALIGA)
    hockey(NHL)
    basketball(NBA)
    basketball(NCAAB)
    football(NFL)
    soccer(EPL)
    basketball(CBA)
        
    


