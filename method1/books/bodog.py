from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from match import *
from teams.teams import *
from teams.normalize import findTeams
import pandas as pd
BODOG_PLUS_SELECTOR = ".icon.header-collapsible__icon.league-header-collapsible__icon.icon-plus"
BODOG_TEAM_NAME_SELECTOR = ".competitors"
BODOG_ODDS_SELECTOR = ".markets-container"
BODOG_LIVE_SELECTOR_XPATH = "//span[contains(text(), 'Live Betting Odds')]"
BODOG_SHOW_MORE_SELECTOR_ID = "showMore"

def bodog(driver, url):
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, BODOG_TEAM_NAME_SELECTOR)))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, BODOG_ODDS_SELECTOR)))

        teamsBox = driver.find_elements(By.CSS_SELECTOR, BODOG_TEAM_NAME_SELECTOR)
        oddsBox = driver.find_elements(By.CSS_SELECTOR, BODOG_ODDS_SELECTOR)
        return teamsBox, oddsBox
    except:
        return bodog(driver,url)
    
def bodogOddsHandicap(oddsHandicapBox):
    oddsHandicapBoxParsed = oddsHandicapBox.split(" ")
    if len(oddsHandicapBoxParsed) == 2:
        teamASpreadHandicap = float(oddsHandicapBoxParsed[0])
        teamAOddsHandicap = 2 if oddsHandicapBoxParsed[1][1:-1] == "EVEN" else americanToDecimal(int(oddsHandicapBoxParsed[1][1:-1]))
        return teamASpreadHandicap, teamAOddsHandicap
    return None, None

def bodogOddsMoneyline(oddsMoneylineParsed):
    teamXOdds = 2 if oddsMoneylineParsed == "EVEN" else americanToDecimal(int(oddsMoneylineParsed)) 
    return teamXOdds

def bodogOddsOverUnder(oddsOverUnderBox):
    oddsOverUnderBoxParsed = oddsOverUnderBox.split(" ")
    if len(oddsOverUnderBoxParsed) == 3:
        overUnderPoints = float(oddsOverUnderBoxParsed[1])
        overUnderOdds = 2 if oddsOverUnderBoxParsed[2][1:-1] == "EVEN" else americanToDecimal(int(oddsOverUnderBoxParsed[2][1:-1]))
        return overUnderPoints, overUnderOdds
    elif len(oddsOverUnderBoxParsed) == 4:
        overUnderPoints1 = float(oddsOverUnderBoxParsed[1][:-1]) 
        overUnderPoints2 = float(oddsOverUnderBoxParsed[2])
        overUnderPoints = (overUnderPoints1+overUnderPoints2)/2
        overUnderOdds = 2 if oddsOverUnderBoxParsed[3][1:-1] == "EVEN" else americanToDecimal(int(oddsOverUnderBoxParsed[3][1:-1]))
        return overUnderPoints, overUnderOdds
    return None, None

def bodogsOdds1x2(odds1x2Box):
    teamXOdds1x2 = 2 if odds1x2Box == "EVEN" else americanToDecimal(int(odds1x2Box)) 
    return teamXOdds1x2

def bodogOdds(odds):
    oddsParsed = odds.text.split("\n")
    if len(oddsParsed) == 6:
        teamASpreadHandicap, teamAOddsHandicap = bodogOddsHandicap(oddsParsed[0])
        teamBSpreadHandicap, teamBOddsHandicap = bodogOddsHandicap(oddsParsed[1])

        teamAOdds = bodogOddsMoneyline(oddsParsed[2])
        teamBOdds = bodogOddsMoneyline(oddsParsed[3])
        
        overPoints, overOdds = bodogOddsOverUnder(oddsParsed[4])                                                     
        underPoints, underOdds = bodogOddsOverUnder(oddsParsed[5])    

        return teamASpreadHandicap, teamAOddsHandicap, teamBSpreadHandicap, teamBOddsHandicap, teamAOdds, teamBOdds, overPoints, overOdds, underPoints, underOdds
    
    return None, None, None, None, None, None, None, None, None, None

def bodogSoccerOdds(odds):
    oddsParsed = odds.text.split("\n")
    if len(oddsParsed) == 7:
        teamASpreadHandicap, teamAOddsHandicap = bodogOddsHandicap(oddsParsed[0])
        teamBSpreadHandicap, teamBOddsHandicap = bodogOddsHandicap(oddsParsed[1])

        teamAOdds1x2 = bodogsOdds1x2(oddsParsed[2])
        teamBOdds1x2 = bodogsOdds1x2(oddsParsed[3])
        drawOdds1x2 = bodogsOdds1x2(oddsParsed[4])
        
        overPoints, overOdds = bodogOddsOverUnder(oddsParsed[5])
        underPoints, underOdds = bodogOddsOverUnder(oddsParsed[6])
        
        return teamASpreadHandicap, teamAOddsHandicap, teamBSpreadHandicap, teamBOddsHandicap, teamAOdds1x2, drawOdds1x2, teamBOdds1x2, overPoints, overOdds, underPoints, underOdds
    
    return None, None, None, None, None, None, None, None, None, None, None

def bodogTeams(teams,numTeams=2):
    teamsParsed = teams.text.split("\n")
    if len(teamsParsed) == numTeams:
        teamA = teamsParsed[0]
        teamB = teamsParsed[1]
        return teamA, teamB
    return None, None

# ===================== 
# Sports
# =====================

BODOG_NHL_URL = "https://www.bodog.eu/sports/hockey/nhl"
BODOG_NBA_URL = "https://www.bodog.eu/sports/basketball/nba"
BODOG_NFL_URL = "https://www.bodog.eu/sports/football/nfl"
BODOG_EPL_URL = "https://www.bodog.eu/sports/soccer/europe/england/premier-league"

def bodogHockey(driver,matches):
    teamsBox,oddsBox = bodog(driver,BODOG_NHL_URL)
    oddsIndex = 0
    for team in teamsBox:
        teamA, teamB = bodogTeams(team)
        if teamA is None or teamB is None:
            oddsIndex += 1
            continue
        teamA, teamB = findTeams(teamA,teamB,NHL_TEAMS)
        oddsParsed = oddsBox[oddsIndex]
        teamASpreadHandicap, teamAOddsHandicap, teamBSpreadHandicap, teamBOddsHandicap, teamAOdds, teamBOdds, overPoints, overOdds, underPoints, underOdds = bodogOdds(oddsParsed)
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
        oddsDf = pd.DataFrame.from_records([odds.__dict__],index=["bodog"])
        matches[match] = pd.concat([matches[match],oddsDf])
        oddsIndex += 1  

def bodogBasketball(driver, matches):
    teamsBox,oddsBox = bodog(driver,BODOG_NBA_URL)
    oddsIndex = 0
    for team in teamsBox:
        teamA, teamB = bodogTeams(team)
        if teamA is None or teamB is None:
            oddsIndex += 1
            continue
        teamA, teamB = findTeams(teamA,teamB,NBA_TEAMS)
        oddsParsed = oddsBox[oddsIndex]
        teamASpreadHandicap, teamAOddsHandicap, teamBSpreadHandicap, teamBOddsHandicap, teamAOdds, teamBOdds, overPoints, overOdds, underPoints, underOdds = bodogOdds(oddsParsed)
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
        oddsDf = pd.DataFrame.from_records([odds.__dict__],index=["bodog"])
        matches[match] = pd.concat([matches[match],oddsDf])
        oddsIndex += 1  

def bodogFootball(driver, matches):
    teamsBox,oddsBox = bodog(driver,BODOG_NFL_URL)
    oddsIndex = 0
    for team in teamsBox:
        teamA, teamB = bodogTeams(team)
        if teamA is None or teamB is None:
            oddsIndex += 1
            continue
        teamA, teamB = findTeams(teamA,teamB,NFL_TEAMS)
        oddsParsed = oddsBox[oddsIndex]
        teamASpreadHandicap, teamAOddsHandicap, teamBSpreadHandicap, teamBOddsHandicap, teamAOdds, teamBOdds, overPoints, overOdds, underPoints, underOdds = bodogOdds(oddsParsed)
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
        oddsDf = pd.DataFrame.from_records([odds.__dict__],index=["bodog"])
        matches[match] = pd.concat([matches[match],oddsDf])
        oddsIndex += 1  

def bodogSoccer(driver, matches):
    teamsBox,oddsBox = bodog(driver,BODOG_EPL_URL)
    oddsIndex = 0
    for team in teamsBox:
        teamA, teamB = bodogTeams(team,3)
        if teamA is None or teamB is None:
            oddsIndex += 1
            continue
        teamA, teamB = findTeams(teamA,teamB,EPL_TEAMS)
        oddsParsed = oddsBox[oddsIndex]
        teamASpreadHandicap, teamAOddsHandicap, teamBSpreadHandicap, teamBOddsHandicap, teamAOdds1x2, drawOdds1x2, teamBOdds1x2, overPoints, overOdds, underPoints, underOdds = bodogSoccerOdds(oddsParsed)
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
        oddsDf = pd.DataFrame.from_records([odds.__dict__],index=["bodog"])
        matches[match] = pd.concat([matches[match],oddsDf])
        oddsIndex += 1  