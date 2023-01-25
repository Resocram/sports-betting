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
import threading

def comparator(matches):
    for match in matches:
        odds = matches[match]
        if len(odds) > 1:
            calculateScore(match, odds) 

def compute(league, functions):
    matches = defaultdict(pd.DataFrame)
    threads = []
    for i in range(len(functions)):
        options = webdriver.ChromeOptions()
        if i != 1:
            options.add_argument('--headless') 
        driver = uc.Chrome(options=options,driver_executable_path="C:/Users/Marco/Desktop/Me/projects/starbucks/chromedriver_win32/chromedriver.exe")
        driver.set_window_size(1400, 1000)
        t = threading.Thread(target=functions[i],args=(driver,matches,league.name, league.teams,league.urls[i]))
        threads.append((t,driver))
        t.start()

    while len(threads) > 0:
        for thread,driver in threads:
            if not thread.is_alive():
                thread.join()
                driver.close()
                threads.remove((thread,driver))
    return matches

def hockey(league):
    functions = [stakeHockey, bet365Hockey, bet99Hockey, bodogHockey, pinnacleHockey]
    matches = compute(league,functions)
    comparator(matches)
    print("done " + league.name)
    return matches

def basketball(league):
    functions = [stakeBasketball, bet365Basketball, bet99Basketball, bodogBasketball, pinnacleBasketball]
    matches = compute(league,functions)
    comparator(matches)
    print("done " + league.name)
    return matches
    
def football(league):
    functions = [stakeFootball, bet365Football, bet99Football, bodogFootball,pinnacleFootball]
    matches = compute(league,functions)
    comparator(matches)
    print("done " + league.name)
    return matches

def soccer(league):
    functions = [stakeSoccer, bet365Soccer, bet99Soccer, bodogSoccer,pinnacleSoccer]
    matches = compute(league,functions)
    comparator(matches)
    print("done " + league.name)
    return matches

def printer(matches):
    for match in matches:
        print(match)
        print(matches[match])
while True:
    start = time.time()
    hockey(NHL)
    basketball(NBA)
    football(NFL)
    hockey(SHL)
    basketball(EUROLEAGUE)
    soccer(LALIGA)
    basketball(NBL)
    basketball(NCAAB)
    hockey(KHL)
    soccer(EPL)
    #basketball(CBA)
    basketball(CHINA_NBL)
    print("TAKEN: " + str(time.time()-start) +" seconds" )
        
    


