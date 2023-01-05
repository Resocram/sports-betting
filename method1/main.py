import undetected_chromedriver.v2 as uc
from match import *
from books.bet99 import *
from books.bodog import *
from books.pinnacle import *
from books.bet365 import *
from selenium import webdriver
from collections import defaultdict
import pandas as pd

def comparator(matches):
    for match in matches:
        odds = matches[match]
        if len(odds) > 1:
            calculateScore(match, odds) 

def hockey():
    matches = defaultdict(pd.DataFrame)
    try:
        bet99Hockey(driver,matches)
    except:
        pass
    try:
        pinnacleHockey(driver, matches)
    except:
        pass
    try:
        bodogHockey(driver, matches)
    except:
        pass
    try:
        bet365Hockey(driver,matches)
    except:
        pass
    comparator(matches)
    print("done hockey")


def basketball():
    matches = defaultdict(pd.DataFrame)
    try:
        bet99Basketball(driver,matches)
    except:
        pass
    try:
        pinnacleBasketball(driver, matches)
    except:
        pass
    try:
        bodogBasketball(driver, matches)
    except:
        pass
    try:
        bet365Basketball(driver,matches)
    except:
        pass
    print("done basketball")
    
def football():
    matches = defaultdict(pd.DataFrame)
    try:
        bet99Football(driver,matches)
    except:
        pass
    try:
        pinnacleFootball(driver, matches)
    except:
        pass
    try:
        bodogFootball(driver, matches)
    except:
        pass
    try:
        bet365Football(driver,matches)
    except:
        pass
    print("done football")
    
def soccer():
    matches = defaultdict(pd.DataFrame)
    try:
        bet99Soccer(driver,matches)
    except:
        pass
    try:
        pinnacleSoccer(driver, matches)
    except:
        pass
    try:
        bodogSoccer(driver, matches)
    except:
        pass
    try:
        bet365Soccer(driver,matches)
    except:
        pass
    print("done soccer")
op = webdriver.ChromeOptions()

driver = uc.Chrome(options=op)
driver.set_window_size(1440, 1440)
hockey()
basketball()
football()
soccer()