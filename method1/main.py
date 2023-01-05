import undetected_chromedriver.v2 as uc
from match import *
from books.bet99 import *
from books.bodog import *
from books.pinnacle import *
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
    bet99Hockey(driver,matches)
    pinnacleHockey(driver, matches)
    bodogHockey(driver, matches)
    comparator(matches)
    print("done hockey")


def basketball():
    matches = defaultdict(pd.DataFrame)
    bet99Basketball(driver, matches)
    pinnacleBasketball(driver, matches)
    bodogBasketball(driver, matches)
    comparator(matches)
    print("done basketball")
    
def football():
    matches = defaultdict(pd.DataFrame)
    bet99Football(driver, matches)
    pinnacleFootball(driver, matches)
    bodogFootball(driver, matches)
    comparator(matches)
    print("done football")
    
def soccer():
    matches = defaultdict(pd.DataFrame)
    bet99Soccer(driver, matches)
    pinnacleSoccer(driver, matches)
    bodogSoccer(driver, matches)
    comparator(matches)
    print("done soccer")
op = webdriver.ChromeOptions()

driver = uc.Chrome(options=op)
driver.set_window_size(1440, 1440)
hockey()
basketball()
football()
soccer()