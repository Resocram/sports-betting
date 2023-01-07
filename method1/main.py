import undetected_chromedriver.v2 as uc
from match import *
from books.bet99 import *
from books.bodog import *
from books.pinnacle import *
from books.bet365 import *
from selenium import webdriver
from collections import defaultdict
from leagues.league import *

websites = ["bet365", "bet99", "bodog", "pinnacle"]

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
    functions = [bet365Hockey, bet99Hockey, bodogHockey,pinnacleHockey]
    matches = compute(league,websites,functions)
    comparator(matches)
    print("done " + league.name)

def basketball(league):
    functions = [bet365Basketball, bet99Basketball, bodogBasketball,pinnacleBasketball]
    matches = compute(league,websites,functions)
    comparator(matches)
    print("done " + league.name)
    
def football(league):
    functions = [bet365Football, bet99Football, bodogFootball, pinnacleFootball]
    matches = compute(league,websites,functions)
    comparator(matches)
    print("done " + league.name)

def soccer(league):
    functions = [bet365Soccer, bodogSoccer, bodogSoccer, pinnacleSoccer]
    matches = compute(league,websites,functions)
    comparator(matches)
    print("done " + league.name)

op = webdriver.ChromeOptions()

driver = uc.Chrome(options=op)
driver.set_window_size(1440, 1440)

while True:
    #basketball(EUROLEAGUE)
    soccer(LALIGA)
    hockey(NHL)
    basketball(NBA)
    basketball(NCAAB)
    football(NFL)
    soccer(EPL)
    #basketball(CBA)
        
    


