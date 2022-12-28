from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from match import *
SPORTSBET_ARROW_SELECTOR = ".summary__IconWrapper-sc-cevddz-3.YFxom"
SPORTSBET_ODDS_SELECTOR = ".market__MarketWrapper-sc-sghgv3-0.gTahDT"
SPORTSBET_TEAM_NAME_SELECTOR = ".EuropeanEventInfo__Name-sc-1bgjk1r-1.fTgRfn"

PINNACLE_TEAMS_SELECTOR = ".style_matchupMetadata__Ey_nj"
PINNACLE_ODDS_SELECTOR = ".style_buttons__XEQem"

BODOG_PLUS_SELECTOR = ".icon.header-collapsible__icon.league-header-collapsible__icon.icon-plus"
BODOG_TEAM_NAME_SELECTOR = ".competitors"
BODOG_ODDS_SELECTOR = ".markets-container"
BODOG_LIVE_SELECTOR_XPATH = "//span[contains(text(), 'Live Betting Odds')]"
BODOG_SHOW_MORE_SELECTOR_ID = "showMore"

#BET99_ODDS_SELECTOR = ".asb-flex.asb-unshrink._asb_prices-markets-americanSportsWithLogo._asb_events-table-row-markets"
#BET99_TEAM_NAME_SELECTOR = ".asb-flex-col.asb-pos-stretch.asb-flex-sc"
BET99_ODDS_SELECTOR = "._asb_events-table-row-markets"
BET99_TEAM_NAME_SELECTOR = "._asb_events-table-row-competitor-name"
def sportsbet(driver, url):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, SPORTSBET_ARROW_SELECTOR)))
    try:
        while True:
            # Click all the drop down menu
            arrowBox = driver.find_element(By.CSS_SELECTOR, SPORTSBET_ARROW_SELECTOR)
            action = ActionChains(driver)
            action.move_to_element(arrowBox).click()
            action.perform()
    except Exception as e:
        pass
    time.sleep(5)
    teamsBox = driver.find_elements(By.CSS_SELECTOR, SPORTSBET_TEAM_NAME_SELECTOR)
    oddsBox = driver.find_elements(By.CSS_SELECTOR, SPORTSBET_ODDS_SELECTOR)
    return teamsBox,oddsBox

def sportsbetOdds1x2(odds1x2Box):
    odds1x2BoxParsed = odds1x2Box.text.split("\n")
    if len(odds1x2BoxParsed) == 3:
        teamAOdds1x2 = americanToDecimal(int(odds1x2BoxParsed[0]))
        drawOdds1x2 = americanToDecimal(int(odds1x2BoxParsed[1]))
        teamBOdds1x2 = americanToDecimal(int(odds1x2BoxParsed[2]))
        return teamAOdds1x2,drawOdds1x2,teamBOdds1x2
    else:
        return None, None, None

def sportsbetOddsHandicap(oddsHandicapBox):
    oddsHandicapBoxParsed = oddsHandicapBox.text.split("\n")
    if len(oddsHandicapBoxParsed) == 4:
        teamASpreadHandicap = float(oddsHandicapBoxParsed[0][1:-1])
        teamAOddsHandicap = americanToDecimal(int(oddsHandicapBoxParsed[1]))
        teamBSpreadHandicap = float(oddsHandicapBoxParsed[2][1:-1])
        teamBOddsHandicap = americanToDecimal(int(oddsHandicapBoxParsed[3]))
        return teamASpreadHandicap,teamAOddsHandicap,teamBSpreadHandicap,teamBOddsHandicap
    return None, None, None, None

def sportsbetOddsOverUnder(oddsOverUnderBox):
    oddsOverUnderBoxParsed = oddsOverUnderBox.text.split("\n")
    if len(oddsOverUnderBoxParsed) == 4:
        overPoints = float(oddsOverUnderBoxParsed[0][1:])
        overOdds = americanToDecimal(int(oddsOverUnderBoxParsed[1]))
        underPoints = float(oddsOverUnderBoxParsed[2][1:])
        underOdds = americanToDecimal(int(oddsOverUnderBoxParsed[3]))
        return overPoints,overOdds,underPoints,underOdds
    return None, None, None, None

def sportsbetOddsMoneyline(oddsMoneylineBox):
    oddsMoneylineBoxParsed = oddsMoneylineBox.text.split("\n")
    if len(oddsMoneylineBoxParsed) == 2:
        teamAOdds = americanToDecimal(int(oddsMoneylineBoxParsed[0]))
        teamBOdds = americanToDecimal(int(oddsMoneylineBoxParsed[1]))
        return teamAOdds, teamBOdds
    return None, None

def pinnacle(driver, url):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, PINNACLE_TEAMS_SELECTOR)))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, PINNACLE_ODDS_SELECTOR)))
    time.sleep(5)
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

def bodog(driver, url):
    driver.get(url)
    # If we want live or not
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, BODOG_LIVE_SELECTOR_XPATH)))
        liveBox = driver.find_element(By.XPATH,BODOG_LIVE_SELECTOR_XPATH)
        liveBox.click()
    except Exception as e:
        pass
    # try:
    #     while True:
    #         # Click all the drop down menu to get all hockey games
    #         WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, BODOG_SHOW_MORE_SELECTOR_ID)))
    #         showMoreBox = driver.find_element(By.ID, BODOG_SHOW_MORE_SELECTOR_ID)
    #         action = ActionChains(driver)
    #         action.move_to_element(showMoreBox).click()
    #         action.perform()
    # except Exception as e:
    #     pass
    try:
        while True:
            # Click all the drop down menu to get all hockey games
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, BODOG_PLUS_SELECTOR)))
            arrowBox = driver.find_element(By.CSS_SELECTOR, BODOG_PLUS_SELECTOR)
            action = ActionChains(driver)
            action.move_to_element(arrowBox).click()
            action.perform()
    except Exception as e:
        pass
    time.sleep(5)
    teamsBox = driver.find_elements(By.CSS_SELECTOR, BODOG_TEAM_NAME_SELECTOR)
    oddsBox = driver.find_elements(By.CSS_SELECTOR, BODOG_ODDS_SELECTOR)
    return teamsBox, oddsBox
    
def bodogOdds(odds):
    oddsParsed = odds.text.split("\n")
    if len(oddsParsed) == 6:
        teamAParsed = oddsParsed[0].split(" ")
        teamASpreadHandicap = float(teamAParsed[0]) if len(teamAParsed) == 2 else None
        teamAOddsHandicap = 2 if teamAParsed[1][1:-1] == "EVEN" else americanToDecimal(int(teamAParsed[1][1:-1])) if len(teamAParsed) == 2 else None

        teamBParsed = oddsParsed[1].split(" ")
        teamBSpreadHandicap = float(teamBParsed[0]) if len(teamBParsed) == 2 else None
        teamBOddsHandicap = 2 if teamBParsed[1][1:-1] == "EVEN" else americanToDecimal(int(teamBParsed[1][1:-1])) if len(teamBParsed) == 2 else None

        teamAOdds = 2 if oddsParsed[2] == "EVEN" else americanToDecimal(int(oddsParsed[2])) 
        teamBOdds = 2 if oddsParsed[3] == "EVEN" else americanToDecimal(int(oddsParsed[3]))
                                                                        
        overParsed = oddsParsed[4].split(" ")
        overPoints = float(overParsed[1]) if len(overParsed) == 3 else None
        overOdds = 2 if overParsed[2][1:-1] == "EVEN" else americanToDecimal(int(overParsed[2][1:-1])) if len(overParsed) == 3 else None

        underParsed = oddsParsed[5].split(" ")
        underPoints = float(underParsed[1]) if len(underParsed) == 3 else None
        underOdds = 2 if underParsed[2][1:-1] == "EVEN" else americanToDecimal(int(underParsed[2][1:-1])) if len(underParsed) == 3 else None
        return teamASpreadHandicap, teamAOddsHandicap, teamBSpreadHandicap, teamBOddsHandicap, teamAOdds, teamBOdds, overPoints, overOdds, underPoints, underOdds
    
    return None, None, None, None, None, None, None, None, None, None

def bodogSoccerOdds(odds):
    oddsParsed = odds.text.split("\n")
    if len(oddsParsed) == 7:
        teamAParsed = oddsParsed[0].split(" ")
        teamASpreadHandicap = float(teamAParsed[0]) if len(teamAParsed) == 2 else None
        teamAOddsHandicap = 2 if teamAParsed[1][1:-1] == "EVEN" else americanToDecimal(int(teamAParsed[1][1:-1])) if len(teamAParsed) == 2 else None

        teamBParsed = oddsParsed[1].split(" ")
        teamBSpreadHandicap = float(teamBParsed[0]) if len(teamBParsed) == 2 else None
        teamBOddsHandicap = 2 if teamBParsed[1][1:-1] == "EVEN" else americanToDecimal(int(teamBParsed[1][1:-1])) if len(teamBParsed) == 2 else None

        teamAOdds1x2 = 2 if oddsParsed[2] == "EVEN" else americanToDecimal(int(oddsParsed[2])) 
        teamBOdds1x2 = 2 if oddsParsed[3] == "EVEN" else americanToDecimal(int(oddsParsed[3]))
        drawOdds1x2 = 2 if oddsParsed[3] == "EVEN" else americanToDecimal(int(oddsParsed[4]))
        
                                                                        
        overParsed = oddsParsed[5].split(" ")
        if len(overParsed) == 3:
            overPoints = float(overParsed[1])
            overOdds = 2 if overParsed[2][1:-1] == "EVEN" else americanToDecimal(int(overParsed[2][1:-1])) if len(overParsed) == 3 else None
        elif len(overParsed) == 4:
            overPoints1 = float(overParsed[1][:-1]) 
            overPoints2 = float(overParsed[2])
            overPoints = (overPoints1+overPoints2)/2
            overOdds = 2 if overParsed[3][1:-1] == "EVEN" else americanToDecimal(int(overParsed[3][1:-1]))

        underParsed = oddsParsed[6].split(" ")
        if len(underParsed) == 3:
            underPoints = float(underParsed[1])
            underOdds = 2 if underParsed[2][1:-1] == "EVEN" else americanToDecimal(int(underParsed[2][1:-1])) if len(underParsed) == 3 else None
        elif len(underParsed) == 4:
            underPoints1 = float(underParsed[1][:-1]) 
            underPoints2 = float(underParsed[2])
            underPoints = (underPoints1+underPoints2)/2
            underOdds = 2 if underParsed[3][1:-1] == "EVEN" else americanToDecimal(int(underParsed[3][1:-1]))

        return teamASpreadHandicap, teamAOddsHandicap, teamBSpreadHandicap, teamBOddsHandicap, teamAOdds1x2, drawOdds1x2, teamBOdds1x2, overPoints, overOdds, underPoints, underOdds
    
    return None, None, None, None, None, None, None, None, None, None, None

def bodogTeams(teams,numTeams=2):
    teamsParsed = teams.text.split("\n")
    if len(teamsParsed) == numTeams:
        teamA = teamsParsed[0]
        teamB = teamsParsed[1]
        return teamA, teamB
    return None, None

def bet99(driver, url):
    driver.get(url)
    time.sleep(2)
    driver.get(url)
    time.sleep(5)
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
        underPoints = float(underParsed[1])
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
        underPoints = float(underParsed[1])
        underOdds = americanToDecimal(int(oddsParsed[9])) 
        return teamAOdds1x2, drawOdds1x2, teamBOdds1x2, overPoints, overOdds, underPoints, underOdds
    return None, None, None, None, None, None, None