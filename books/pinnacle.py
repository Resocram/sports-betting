from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from books.bet99 import *

PINNACLE_TEAMS_SELECTOR = ".style_matchupMetadata__Ey_nj"
PINNACLE_ODDS_SELECTOR = ".style_buttons__XEQem"

def pinnacle(driver, url):
    driver.get(url)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, PINNACLE_TEAMS_SELECTOR)))
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, PINNACLE_ODDS_SELECTOR)))
    teamsBox = driver.find_elements(By.CSS_SELECTOR, PINNACLE_TEAMS_SELECTOR)
    oddsBox = driver.find_elements(By.CSS_SELECTOR, PINNACLE_ODDS_SELECTOR)
    return teamsBox,oddsBox

def pinnacleTeams(teams):
    teamA, teamB, date = teams.split("\n")
    return teamA, teamB, date

def pinnacleOdds1x2(odds1x2Box):
    odds1x2BoxParsed = odds1x2Box.text.split("\n")
    if len(odds1x2BoxParsed) == 3:
        teamAOdds1x2 = float(odds1x2BoxParsed[0])
        drawOdds1x2 = float(odds1x2BoxParsed[1])
        teamBOdds1x2 = float(odds1x2BoxParsed[2])
        return teamAOdds1x2,drawOdds1x2,teamBOdds1x2
    return None, None, None

def pinnacleOddsHandicap(oddsHandicapBox):
    oddsHandicapBoxParsed = oddsHandicapBox.text.split("\n")
    if len(oddsHandicapBoxParsed) == 4:
        teamASpreadHandicap = float(oddsHandicapBoxParsed[0])
        teamAOddsHandicap = float(oddsHandicapBoxParsed[1])
        teamBSpreadHandicap = float(oddsHandicapBoxParsed[2])
        teamBOddsHandicap = float(oddsHandicapBoxParsed[3])
        return teamASpreadHandicap,teamAOddsHandicap,teamBSpreadHandicap,teamBOddsHandicap
    return None, None, None, None

def pinnacleOddsOverUnder(oddsOverUnderBox):
    oddsOverUnderBoxParsed = oddsOverUnderBox.text.split("\n")
    if len(oddsOverUnderBoxParsed) == 4:
        overPoints = float(oddsOverUnderBoxParsed[0])
        overOdds = float(oddsOverUnderBoxParsed[1])
        underPoints = float(oddsOverUnderBoxParsed[2])
        underOdds = float(oddsOverUnderBoxParsed[3])
        return overPoints,overOdds,underPoints,underOdds
    return None, None, None, None

def pinnacleOddsMoneyline(oddsMoneylineBox):
    oddsMoneylineBoxParsed = oddsMoneylineBox.text.split("\n")
    if len(oddsMoneylineBoxParsed) == 2:
        teamAOdds = float(oddsMoneylineBoxParsed[0])
        teamBOdds = float(oddsMoneylineBoxParsed[1])
        return teamAOdds, teamBOdds
    return None, None

# ===================== 
# Sports
# =====================

PINNACLE_HOCKEY_URL = "https://www.pinnacle.com/en/hockey/matchups"
PINNACLE_BASKETBALL_URL = "https://www.pinnacle.com/en/basketball/matchups"
PINNABLE_FOOTBALL_URL = "https://www.pinnacle.com/en/football/matchups"
PINNACLE_SOCCER_URL = "https://www.pinnacle.com/en/soccer/matchups/highlights"


def pinnacleHockey(driver):
    matches = []
    teamsBox,oddsBox = pinnacle(driver,PINNACLE_HOCKEY_URL)
    oddsIndex = 0
    for teams in teamsBox:
        teamA,teamB,date = pinnacleTeams(teams.text)
        
        while oddsBox[oddsIndex].text == "1\nX\n2" or oddsBox[oddsIndex].text == "HANDICAP" or oddsBox[oddsIndex].text == "MONEY LINE":
            oddsIndex += 3
        if "Live" in date:
            oddsIndex += 3
            continue
        teamAOdds, teamBOdds = pinnacleOddsMoneyline(oddsBox[oddsIndex])
        teamASpreadHandicap,teamAOddsHandicap,teamBSpreadHandicap,teamBOddsHandicap = pinnacleOddsHandicap(oddsBox[oddsIndex+1])
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
                         teamBOddsHandicap
                         )
        odds.overPoints, odds.overOdds, odds.underPoints, odds.underOdds = pinnacleOddsOverUnder(oddsBox[oddsIndex+2])
        matches.append((match,odds))
        oddsIndex += 3
    return matches

def pinnacleBasketball(driver):
    matches = []
    teamsBox,oddsBox = pinnacle(driver,PINNACLE_BASKETBALL_URL)
    oddsIndex = 0
    
    for teams in teamsBox:
        teamA,teamB,date = pinnacleTeams(teams.text)
        while oddsBox[oddsIndex].text == "1\nX\n2" or oddsBox[oddsIndex].text == "HANDICAP" or oddsBox[oddsIndex].text == "MONEY LINE":
            oddsIndex += 3
        if "Live" in date:
            oddsIndex += 3
            continue
        teamASpreadHandicap,teamAOddsHandicap,teamBSpreadHandicap,teamBOddsHandicap = pinnacleOddsHandicap(oddsBox[oddsIndex])
        teamAOdds, teamBOdds = pinnacleOddsMoneyline(oddsBox[oddsIndex+1])
        overPoints, overOdds, underPoints, underOdds = pinnacleOddsOverUnder(oddsBox[oddsIndex+2])
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
        oddsIndex += 3
    return matches

def pinnacleFootball(driver):
    matches = []
    teamsBox,oddsBox = pinnacle(driver,PINNABLE_FOOTBALL_URL)
    oddsIndex = 0
    
    for teams in teamsBox:
        teamA,teamB,date = pinnacleTeams(teams.text)
        while oddsBox[oddsIndex].text == "1\nX\n2" or oddsBox[oddsIndex].text == "HANDICAP" or oddsBox[oddsIndex].text == "MONEY LINE":
            oddsIndex += 3
        if "Live" in date:
            oddsIndex += 3
            continue
        teamASpreadHandicap,teamAOddsHandicap,teamBSpreadHandicap,teamBOddsHandicap = pinnacleOddsHandicap(oddsBox[oddsIndex])
        teamAOdds, teamBOdds = pinnacleOddsMoneyline(oddsBox[oddsIndex+1])
        overPoints, overOdds, underPoints,underOdds = pinnacleOddsOverUnder(oddsBox[oddsIndex+2])
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
        oddsIndex += 3
    return matches

def pinnacleSoccer(driver):
    matches = []
    teamsBox,oddsBox = pinnacle(driver,PINNACLE_SOCCER_URL)
    oddsIndex = 0
    
    for teams in teamsBox:
        teamA,teamB,date = pinnacleTeams(teams.text)
        while oddsBox[oddsIndex].text == "1\nX\n2" or oddsBox[oddsIndex].text == "HANDICAP" or oddsBox[oddsIndex].text == "MONEY LINE":
            oddsIndex += 3
        if "Live" in date:
            oddsIndex += 3
            continue
        teamAOdds1x2,drawOdds1x2,teamBOdds1x2 = pinnacleOdds1x2(oddsBox[oddsIndex])
        teamASpreadHandicap,teamAOddsHandicap,teamBSpreadHandicap,teamBOddsHandicap = pinnacleOddsHandicap(oddsBox[oddsIndex+1])        
        overPoints, overOdds, underPoints, underOdds = pinnacleOddsOverUnder(oddsBox[oddsIndex+2])
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
        oddsIndex += 3
    return matches