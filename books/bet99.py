from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from match import *
import time
BET99_ODDS_SELECTOR = "._asb_events-table-row-markets"
BET99_TEAM_NAME_SELECTOR = "._asb_events-table-row-competitor-name"

def bet99(driver, url):
    while True:
        driver.get(url)
        time.sleep(5)
        if driver.current_url == url:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, BET99_TEAM_NAME_SELECTOR)))
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, BET99_ODDS_SELECTOR)))
            teamsBox = driver.find_elements(By.CSS_SELECTOR, BET99_TEAM_NAME_SELECTOR)
            oddsBox = driver.find_elements(By.CSS_SELECTOR, BET99_ODDS_SELECTOR)
            return teamsBox, oddsBox
        

def bet99Teams(teams):
    teamsParsed = teams.text.split("\n")
    if len(teamsParsed) == 2:
        teamA = teamsParsed[0]
        teamB = teamsParsed[1]
        return teamA, teamB
    return None, None

def bet99Odds(odds):
    oddsParsed = odds.text.split("\n")
    if len(oddsParsed) == 10:
        teamAOdds = americanToDecimal(int(oddsParsed[0])) 
        teamBOdds = americanToDecimal(int(oddsParsed[1])) 
        teamASpreadHandicap = float(oddsParsed[2]) 
        teamAOddsHandicap = americanToDecimal(int(oddsParsed[3])) 
        teamBSpreadHandicap = float(oddsParsed[4]) 
        teamBOddsHandicap = americanToDecimal(int(oddsParsed[5])) 
        overParsed = oddsParsed[6].split(" ")
        overPoints = float(overParsed[1])
        overOdds = americanToDecimal(int(oddsParsed[7])) 
        underParsed = oddsParsed[8].split(" ")
        underPoints = -float(underParsed[1])
        underOdds = americanToDecimal(int(oddsParsed[9])) 
        return teamAOdds, teamBOdds, teamASpreadHandicap, teamAOddsHandicap, teamBSpreadHandicap, teamBOddsHandicap, overPoints, overOdds, underPoints, underOdds
    return None, None, None, None, None, None, None, None, None, None

def bet99SoccerOdds(odds):
    oddsParsed = odds.text.split("\n")
    if len(oddsParsed) == 10:
        teamAOdds1x2 = 2 if oddsParsed[1] == "EVEN" else americanToDecimal(int(oddsParsed[1])) 
        drawOdds1x2 = 2 if oddsParsed[3] == "EVEN" else americanToDecimal(int(oddsParsed[3]))
        teamBOdds1x2 = 2 if oddsParsed[5] == "EVEN" else americanToDecimal(int(oddsParsed[5]))
        
        overParsed = oddsParsed[6].split(" ")
        overPoints = float(overParsed[1])
        overOdds = americanToDecimal(int(oddsParsed[7])) 
        underParsed = oddsParsed[8].split(" ")
        underPoints = -float(underParsed[1])
        underOdds = americanToDecimal(int(oddsParsed[9])) 
        return teamAOdds1x2, drawOdds1x2, teamBOdds1x2, overPoints, overOdds, underPoints, underOdds
    return None, None, None, None, None, None, None


# ===================== 
# Sports
# =====================

BET99_HOCKEY_URL = "https://bet99.com/en/sport-betting#/alltopevents/events/70"
BET99_BASKETBALL_URL = "https://bet99.com/en/sport-betting#/alltopevents/events/67"
BET99_FOOTBALL_URL = "https://bet99.com/en/sport-betting#/alltopevents/events/75"
BET99_SOCCER_URL = "https://bet99.com/en/sport-betting#/alltopevents/events/66"

def bet99Hockey(driver):
    matches = []
    teamsBox,oddsBox = bet99(driver,BET99_HOCKEY_URL)
    oddsIndex = 0
    for i in range(0,len(teamsBox),2):
        teamA, teamB = teamsBox[i].text, teamsBox[i+1].text
        oddsParsed = oddsBox[oddsIndex]
        teamAOdds, teamBOdds, teamASpreadHandicap, teamAOddsHandicap, teamBSpreadHandicap, teamBOddsHandicap, overPoints, overOdds, underPoints, underOdds = bet99Odds(oddsParsed)
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

def bet99Basketball(driver):
    matches = []
    teamsBox,oddsBox = bet99(driver,BET99_BASKETBALL_URL)
    oddsIndex = 0
    for i in range(0,len(teamsBox),2):
        teamA, teamB = teamsBox[i].text, teamsBox[i+1].text
        oddsParsed = oddsBox[oddsIndex]
        teamAOdds, teamBOdds, teamASpreadHandicap, teamAOddsHandicap, teamBSpreadHandicap, teamBOddsHandicap, overPoints, overOdds, underPoints, underOdds = bet99Odds(oddsParsed)
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

def bet99Football(driver):
    matches = []
    teamsBox,oddsBox = bet99(driver,BET99_FOOTBALL_URL)
    oddsIndex = 0
    for i in range(0,len(teamsBox),2):
        teamA, teamB = teamsBox[i].text, teamsBox[i+1].text
        oddsParsed = oddsBox[oddsIndex]
        teamAOdds, teamBOdds, teamASpreadHandicap, teamAOddsHandicap, teamBSpreadHandicap, teamBOddsHandicap, overPoints, overOdds, underPoints, underOdds = bet99Odds(oddsParsed)
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

def bet99Soccer(driver):
    matches = []
    teamsBox,oddsBox = bet99(driver,BET99_SOCCER_URL)
    oddsIndex = 0
    for i in range(0,len(teamsBox),2):
        
        teamA, teamB = teamsBox[i].text, teamsBox[i+1].text
        oddsParsed = oddsBox[oddsIndex]
        teamAOdds1x2, drawOdds1x2, teamBOdds1x2, overPoints, overOdds, underPoints, underOdds = bet99SoccerOdds(oddsParsed)
        match, odds = standardizeMatchOdds(
                            teamA,
                            teamB,
                            None,
                            None,
                            teamAOdds1x2,
                            drawOdds1x2,
                            teamBOdds1x2,
                            None,
                            None,
                            None,
                            None,
                            underPoints,
                            underOdds,
                            overPoints,
                            overOdds
                            )
        matches.append((match,odds))
        oddsIndex += 1 
    return matches