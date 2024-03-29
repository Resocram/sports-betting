from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from match import *
from leagues.normalize import *
import pandas as pd
import sys

STAKE_TEAM_NAME_SELECTOR = ".teams.stacked"
STAKE_ODDS_SELECTOR = ".outcomes"
STAKE_BUTTON_SELECTOR = '//*[@data-analytics="threeway-enable-button"]'
RETRY_TIMES = 5

def stake(driver,url, leagueName):
    
    retrytimes = 0
    while retrytimes < RETRY_TIMES:
        try:
            driver.get(url)
            time.sleep(5)
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, STAKE_BUTTON_SELECTOR)))
                buttonBox = driver.find_element(By.XPATH, STAKE_BUTTON_SELECTOR)
                buttonBox.click()
            except:
                pass
            time.sleep(5)
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, STAKE_TEAM_NAME_SELECTOR)))
            teamsBox = driver.find_elements(By.CSS_SELECTOR, STAKE_TEAM_NAME_SELECTOR)
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, STAKE_ODDS_SELECTOR)))
            oddsBox = driver.find_elements(By.CSS_SELECTOR, STAKE_ODDS_SELECTOR)
            return teamsBox, oddsBox
        except:
            retrytimes += 1
    print("Stake retried " + str(RETRY_TIMES) + " times for " + leagueName)
    sys.exit()

def stakeTeams(teams):
    teamsParsed = teams.text.split("\n")
    if len(teamsParsed) == 2:
        teamA = teamsParsed[0]
        teamB = teamsParsed[1]
        return teamA, teamB
    return None, None

def stakeMoneyline(oddsBox):
    oddsParsed = oddsBox.text.split("\n")
    if len(oddsParsed) == 4:
        teamAOdds = None if oddsParsed[1] == "Suspended" else float(oddsParsed[1])
        teamBOdds = None if oddsParsed[3] == "Suspended" else float(oddsParsed[3])
        return teamAOdds, teamBOdds
    return None, None

def stakeHandicap(oddsBox):
    oddsParsed = oddsBox.text.split("\n")
    if len(oddsParsed) == 4:
        teamASpreadHandicap = None if oddsParsed[0] == "Suspended" else float(oddsParsed[0])
        teamAOddsHandicap = None if oddsParsed[1] == "Suspended" else float(oddsParsed[1])
        teamBSpreadHandicap = None if oddsParsed[2] == "Suspended" else float(oddsParsed[2])
        teamBOddsHandicap = None if oddsParsed[3] == "Suspended" else float(oddsParsed[3])
        return teamASpreadHandicap, teamAOddsHandicap, teamBSpreadHandicap, teamBOddsHandicap
    return None, None, None, None

def stakeTotal(oddsBox):
    oddsParsed = oddsBox.text.split("\n")
    if len(oddsParsed) == 4:
        overPoints = None if oddsParsed[0] == "Suspended" else float(oddsParsed[0].split(" ")[1])
        overOdds = None if oddsParsed[1] == "Suspended" else float(oddsParsed[1])
        underPoints = None if oddsParsed[2] == "Suspended" else float(oddsParsed[2].split(" ")[1])
        underOdds = None if oddsParsed[3] == "Suspended" else float(oddsParsed[3])
        return overPoints, overOdds, underPoints, underOdds
    return None, None, None, None

def stake1x2(oddsBox):
    oddsParsed = oddsBox.text.split("\n")
    if len(oddsParsed) == 6:
        teamAOdds1x2 = None if oddsParsed[1] == "Suspended" else float(oddsParsed[1])
        drawOdds1x2 = None if oddsParsed[3] == "Suspended" else float(oddsParsed[3])
        teamBOdds1x2 = None if oddsParsed[5] == "Suspended" else float(oddsParsed[5])
        return teamAOdds1x2, drawOdds1x2, teamBOdds1x2
    return None, None, None


def stakeBasketball(driver,matches, leagueName,leagueTeams,url):
    teamsBox, oddsBox = stake(driver,url, leagueName)
    oddsIndex = 0
    for i in range(0,len(teamsBox)):
        teamA, teamB = stakeTeams(teamsBox[i])
        teamA, teamB = findTeams(teamA,teamB,leagueTeams)
        teamAOdds, teamBOdds = stakeMoneyline(oddsBox[oddsIndex])
        teamASpreadHandicap, teamAOddsHandicap, teamBSpreadHandicap, teamBOddsHandicap = stakeHandicap(oddsBox[oddsIndex+1])
        overPoints, overOdds, underPoints, underOdds = stakeTotal(oddsBox[oddsIndex+2])
        match, odds = standardizeMatchOdds(
                            teamA,
                            teamB,
                            teamAOdds,
                            teamBOdds,
                            None,
                            None,
                            None,
                            teamASpreadHandicap,
                            teamAOddsHandicap,
                            teamBSpreadHandicap,
                            teamBOddsHandicap,
                            underPoints,
                            underOdds,
                            overPoints,
                            overOdds
                            )
        oddsDf = pd.DataFrame.from_records([odds.__dict__],index=["stake"])
        matches[match] = pd.concat([matches[match],oddsDf])
        oddsIndex += 3
        
        
def stakeFootball(driver,matches, leagueName,leagueTeams,url):
    teamsBox, oddsBox = stake(driver,url, leagueName)
    oddsIndex = 0
    for i in range(0,len(teamsBox)):
        teamA, teamB = stakeTeams(teamsBox[i])
        teamA, teamB = findTeams(teamA,teamB,leagueTeams)
        teamAOdds, teamBOdds = stakeMoneyline(oddsBox[oddsIndex+2])
        teamASpreadHandicap, teamAOddsHandicap, teamBSpreadHandicap, teamBOddsHandicap = stakeHandicap(oddsBox[oddsIndex+1])
        overPoints, overOdds, underPoints, underOdds = stakeTotal(oddsBox[oddsIndex])
        match, odds = standardizeMatchOdds(
                            teamA,
                            teamB,
                            teamAOdds,
                            teamBOdds,
                            None,
                            None,
                            None,
                            teamASpreadHandicap,
                            teamAOddsHandicap,
                            teamBSpreadHandicap,
                            teamBOddsHandicap,
                            underPoints,
                            underOdds,
                            overPoints,
                            overOdds
                            )
        oddsDf = pd.DataFrame.from_records([odds.__dict__],index=["stake"])
        matches[match] = pd.concat([matches[match],oddsDf])
        oddsIndex += 3
        
def stakeHockey(driver,matches, leagueName,leagueTeams,url):
    teamsBox, oddsBox = stake(driver,url, leagueName)
    oddsIndex = 0
    for i in range(0,len(teamsBox)):
        teamA, teamB = stakeTeams(teamsBox[i])
        teamA, teamB = findTeams(teamA,teamB,leagueTeams)
        # Noone compares 1x2 for hockey lol
        teamAOdds1x2, drawOdds1x2, teamBOdds1x2 = stake1x2(oddsBox[oddsIndex+2])
        teamASpreadHandicap, teamAOddsHandicap, teamBSpreadHandicap, teamBOddsHandicap = stakeHandicap(oddsBox[oddsIndex])
        overPoints, overOdds, underPoints, underOdds = stakeTotal(oddsBox[oddsIndex+1])
        match, odds = standardizeMatchOdds(
                            teamA,
                            teamB,
                            None,
                            None,
                            teamAOdds1x2,
                            drawOdds1x2,
                            teamBOdds1x2,
                            teamASpreadHandicap,
                            teamAOddsHandicap,
                            teamBSpreadHandicap,
                            teamBOddsHandicap,
                            underPoints,
                            underOdds,
                            overPoints,
                            overOdds
                            )
        oddsDf = pd.DataFrame.from_records([odds.__dict__],index=["stake"])
        matches[match] = pd.concat([matches[match],oddsDf])
        oddsIndex += 3
        
def stakeSoccer(driver,matches, leagueName,leagueTeams,url):
    teamsBox, oddsBox = stake(driver,url, leagueName)
    oddsIndex = 0
    for i in range(0,len(teamsBox)):
        teamA, teamB = stakeTeams(teamsBox[i])
        teamA, teamB = findTeams(teamA,teamB,leagueTeams)
        teamAOdds1x2, drawOdds1x2, teamBOdds1x2 = stake1x2(oddsBox[oddsIndex+1])
        teamASpreadHandicap, teamAOddsHandicap, teamBSpreadHandicap, teamBOddsHandicap = stakeHandicap(oddsBox[oddsIndex+2])
        overPoints, overOdds, underPoints, underOdds = stakeTotal(oddsBox[oddsIndex])
        match, odds = standardizeMatchOdds(
                            teamA,
                            teamB,
                            None,
                            None,
                            teamAOdds1x2,
                            drawOdds1x2,
                            teamBOdds1x2,
                            teamASpreadHandicap,
                            teamAOddsHandicap,
                            teamBSpreadHandicap,
                            teamBOddsHandicap,
                            underPoints,
                            underOdds,
                            overPoints,
                            overOdds
                            )
        oddsDf = pd.DataFrame.from_records([odds.__dict__],index=["stake"])
        matches[match] = pd.concat([matches[match],oddsDf])
        oddsIndex += 3