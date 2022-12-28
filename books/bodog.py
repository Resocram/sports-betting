from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from match import *


BODOG_PLUS_SELECTOR = ".icon.header-collapsible__icon.league-header-collapsible__icon.icon-plus"
BODOG_TEAM_NAME_SELECTOR = ".competitors"
BODOG_ODDS_SELECTOR = ".markets-container"
BODOG_LIVE_SELECTOR_XPATH = "//span[contains(text(), 'Live Betting Odds')]"
BODOG_SHOW_MORE_SELECTOR_ID = "showMore"

def bodog(driver, url):
    driver.get(url)
    # If we want live or not
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, BODOG_LIVE_SELECTOR_XPATH)))
        liveBox = driver.find_element(By.XPATH,BODOG_LIVE_SELECTOR_XPATH)
        liveBox.click()
    except Exception as e:
        pass
    try:
        while True:
            # Click show more to see more games
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, BODOG_SHOW_MORE_SELECTOR_ID)))
            showMoreBox = driver.find_element(By.ID, BODOG_SHOW_MORE_SELECTOR_ID)
            action = ActionChains(driver)
            action.move_to_element(showMoreBox).click()
            action.perform()
    except Exception as e:
        pass
    try:
        while True:
            # Click to see drop down menu
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, BODOG_PLUS_SELECTOR)))
            arrowBox = driver.find_element(By.CSS_SELECTOR, BODOG_PLUS_SELECTOR)
            action = ActionChains(driver)
            action.move_to_element(arrowBox).click()
            action.perform()
    except Exception as e:
        pass
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, BODOG_TEAM_NAME_SELECTOR)))
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, BODOG_ODDS_SELECTOR)))

    teamsBox = driver.find_elements(By.CSS_SELECTOR, BODOG_TEAM_NAME_SELECTOR)
    oddsBox = driver.find_elements(By.CSS_SELECTOR, BODOG_ODDS_SELECTOR)
    return teamsBox, oddsBox
    
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

BODOG_HOCKEY_URL = "https://www.bodog.eu/sports/hockey"
BODOG_BASKETBALL_URL = "https://www.bodog.eu/sports/basketball"
BODOG_FOOTBALL_URL = "https://www.bodog.eu/sports/football"
BODOG_SOCCER_URL = "https://www.bodog.eu/sports/soccer"

def bodogHockey(driver):
    matches = []
    teamsBox,oddsBox = bodog(driver,BODOG_HOCKEY_URL)
    oddsIndex = 0
    for team in teamsBox:
        teamA, teamB = bodogTeams(team)
        if teamA is None or teamB is None:
            oddsIndex += 1
            continue
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
        matches.append((match,odds))
        oddsIndex += 1  
    return matches

def bodogBasketball(driver):
    matches = []
    teamsBox,oddsBox = bodog(driver,BODOG_BASKETBALL_URL)
    oddsIndex = 0
    for team in teamsBox:
        teamA, teamB = bodogTeams(team)
        if teamA is None or teamB is None:
            oddsIndex += 1
            continue
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
        matches.append((match,odds))
        oddsIndex += 1  

    return matches

def bodogFootball(driver):
    matches = []
    teamsBox,oddsBox = bodog(driver,BODOG_FOOTBALL_URL)
    oddsIndex = 0
    for team in teamsBox:
        teamA, teamB = bodogTeams(team)
        if teamA is None or teamB is None:
            oddsIndex += 1
            continue
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
        matches.append((match,odds))
        oddsIndex += 1  
    return matches

def bodogSoccer(driver):
    matches = []
    teamsBox,oddsBox = bodog(driver,BODOG_SOCCER_URL)
    oddsIndex = 0
    matches = []
    for team in teamsBox:
        teamA, teamB = bodogTeams(team,3)
        if teamA is None or teamB is None:
            oddsIndex += 1
            continue
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
        matches.append((match,odds))
        oddsIndex += 1  
    return matches