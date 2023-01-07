from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from match import *
from leagues.normalize import *
import pandas as pd
BET365_NFL_TEAM_NAME_SELECTOR = ".sac-ParticipantFixtureDetailsHigherAmericanFootball_Team"
BET365_NHL_TEAM_NAME_SELECTOR = ".sci-ParticipantFixtureDetailsHigherIceHockey_Team"
BET365_NBA_TEAM_NAME_SELECTOR = ".scb-ParticipantFixtureDetailsHigherBasketball_Team"
BET365_EPL_TEAM_NAME_SELECTOR = ".rcl-ParticipantFixtureDetailsTeam_TeamName"
BET365_ODDS_SELECTOR = ".gl-Participant_General.gl-Market_General-cn1"


def bet365(driver, url, teamNameSelector):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, teamNameSelector)))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, BET365_ODDS_SELECTOR)))
    teamsBox = driver.find_elements(By.CSS_SELECTOR, teamNameSelector)
    oddsBox = driver.find_elements(By.CSS_SELECTOR, BET365_ODDS_SELECTOR)
    return teamsBox, oddsBox

def bet365Spread(oddsBox):
    try:
        oddsParsed = oddsBox.split("\n")
        teamSpreadHandicap = float(oddsParsed[0])
        teamOddsHandicap = americanToDecimal(int(oddsParsed[1]))
        return teamSpreadHandicap, teamOddsHandicap
    except:
        return None, None

def bet365Total(oddsBox):
    try:
        oddsParsed = oddsBox.split("\n")
        overUnderTotal = float(oddsParsed[0].split(" ")[1])
        overUnderOdds = americanToDecimal(int(oddsParsed[1]))
        return overUnderTotal, overUnderOdds
    except:
        return None, None

def bet365Moneyline(oddsBox):
    try:
        moneyline = americanToDecimal(int(oddsBox))
        return moneyline
    except:
        return None
def bet3651x2(oddsBox):
    try:
        moneyline = americanToDecimal(int(oddsBox))
        return moneyline
    except:
        return None


# ===================== 
# Sports
# =====================


def bet365Hockey(driver, matches,leagueTeams, url):
    teamsBox,oddsBox = bet365(driver,url,BET365_NHL_TEAM_NAME_SELECTOR)
    oddsIndex = 0
    matchesTmp = []
    for i in range(0,len(teamsBox),2):
        teamA, teamB = findTeams(teamsBox[i].text,teamsBox[i+1].text,leagueTeams)
        matchesTmp.append(Match(teamA,teamB))

    odds = [Odds() for i in range(len(matchesTmp))] 
    oddsIndex = 0
    for i in range(0,len(teamsBox),2):
        odds[oddsIndex].teamAOdds = bet365Moneyline(oddsBox[i].text)
        odds[oddsIndex].teamBOdds = bet365Moneyline(oddsBox[i+1].text)
        oddsIndex += 1
    oddsIndex = 0
    for i in range(len(teamsBox),2*len(teamsBox),2):
        odds[oddsIndex].overPoints,odds[oddsIndex].overOdds = bet365Total(oddsBox[i].text)
        odds[oddsIndex].underPoints,odds[oddsIndex].underOdds = bet365Total(oddsBox[i+1].text)
        oddsIndex += 1
    oddsIndex = 0
    for i in range(2*len(teamsBox),3*len(teamsBox),2):
        odds[oddsIndex].teamASpreadHandicap,odds[oddsIndex].teamAOddsHandicap = bet365Spread(oddsBox[i].text)
        odds[oddsIndex].teamBSpreadHandicap,odds[oddsIndex].teamBOddsHandicap = bet365Spread(oddsBox[i+1].text)
        oddsIndex += 1
    
    for i in range(len(matchesTmp)):
        match, odd = standardizeMatchOdds(matchesTmp[i].teamA,matchesTmp[i].teamB,odds[i].teamAOdds,odds[i].teamBOdds,odds[i].teamAOdds1x2,odds[i].drawOdds1x2,odds[i].teamBOdds1x2,odds[i].teamASpreadHandicap,odds[i].teamAOddsHandicap,odds[i].teamBSpreadHandicap,odds[i].teamBOddsHandicap,odds[i].underPoints,odds[i].underOdds,odds[i].overPoints,odds[i].overOdds)
        oddsDf = pd.DataFrame.from_records([odd.__dict__],index=["bet365"])
        matches[match] = pd.concat([matches[match],oddsDf])

def bet365Basketball(driver, matches, leagueTeams, url):
    teamsBox,oddsBox = bet365(driver,url,BET365_NBA_TEAM_NAME_SELECTOR)
    oddsIndex = 0
    matchesTmp = []
    for i in range(0,len(teamsBox),2):
        teamA, teamB = findTeams(teamsBox[i].text,teamsBox[i+1].text,leagueTeams)
        matchesTmp.append(Match(teamA,teamB))

    odds = [Odds() for i in range(len(matchesTmp))] 
    oddsIndex = 0
    for i in range(0,len(teamsBox),2):
        odds[oddsIndex].teamASpreadHandicap,odds[oddsIndex].teamAOddsHandicap = bet365Spread(oddsBox[i].text)
        odds[oddsIndex].teamBSpreadHandicap,odds[oddsIndex].teamBOddsHandicap = bet365Spread(oddsBox[i+1].text)
        oddsIndex += 1
    oddsIndex = 0
    for i in range(len(teamsBox),2*len(teamsBox),2):
        odds[oddsIndex].overPoints,odds[oddsIndex].overOdds = bet365Total(oddsBox[i].text)
        odds[oddsIndex].underPoints,odds[oddsIndex].underOdds = bet365Total(oddsBox[i+1].text)
        oddsIndex += 1
    oddsIndex = 0
    for i in range(2*len(teamsBox),3*len(teamsBox),2):
        odds[oddsIndex].teamAOdds = bet365Moneyline(oddsBox[i].text)
        odds[oddsIndex].teamBOdds = bet365Moneyline(oddsBox[i+1].text)
        oddsIndex += 1
    for i in range(len(matchesTmp)):
        match, odd = standardizeMatchOdds(matchesTmp[i].teamA,matchesTmp[i].teamB,odds[i].teamAOdds,odds[i].teamBOdds,odds[i].teamAOdds1x2,odds[i].drawOdds1x2,odds[i].teamBOdds1x2,odds[i].teamASpreadHandicap,odds[i].teamAOddsHandicap,odds[i].teamBSpreadHandicap,odds[i].teamBOddsHandicap,odds[i].underPoints,odds[i].underOdds,odds[i].overPoints,odds[i].overOdds)
        oddsDf = pd.DataFrame.from_records([odd.__dict__],index=["bet365"])
        matches[match] = pd.concat([matches[match],oddsDf])
        
def bet365Football(driver, matches, leagueTeams, url):
    teamsBox,oddsBox = bet365(driver,url,BET365_NFL_TEAM_NAME_SELECTOR)
    oddsIndex = 0
    matchesTmp = []
    for i in range(0,len(teamsBox),2):
        teamA, teamB = findTeams(teamsBox[i].text,teamsBox[i+1].text,leagueTeams)
        matchesTmp.append(Match(teamA,teamB))

    odds = [Odds() for i in range(len(matchesTmp))] 
    oddsIndex = 0
    for i in range(0,len(teamsBox),2):
        odds[oddsIndex].teamASpreadHandicap,odds[oddsIndex].teamAOddsHandicap = bet365Spread(oddsBox[i].text)
        odds[oddsIndex].teamBSpreadHandicap,odds[oddsIndex].teamBOddsHandicap = bet365Spread(oddsBox[i+1].text)
        oddsIndex += 1
    oddsIndex = 0
    for i in range(len(teamsBox),2*len(teamsBox),2):
        odds[oddsIndex].overPoints,odds[oddsIndex].overOdds = bet365Total(oddsBox[i].text)
        odds[oddsIndex].underPoints,odds[oddsIndex].underOdds = bet365Total(oddsBox[i+1].text)
        oddsIndex += 1
    oddsIndex = 0
    for i in range(2*len(teamsBox),3*len(teamsBox),2):
        odds[oddsIndex].teamAOdds = bet365Moneyline(oddsBox[i].text)
        odds[oddsIndex].teamBOdds = bet365Moneyline(oddsBox[i+1].text)
        oddsIndex += 1
    for i in range(len(matchesTmp)):
        match, odd = standardizeMatchOdds(matchesTmp[i].teamA,matchesTmp[i].teamB,odds[i].teamAOdds,odds[i].teamBOdds,odds[i].teamAOdds1x2,odds[i].drawOdds1x2,odds[i].teamBOdds1x2,odds[i].teamASpreadHandicap,odds[i].teamAOddsHandicap,odds[i].teamBSpreadHandicap,odds[i].teamBOddsHandicap,odds[i].underPoints,odds[i].underOdds,odds[i].overPoints,odds[i].overOdds)
        oddsDf = pd.DataFrame.from_records([odd.__dict__],index=["bet365"])
        matches[match] = pd.concat([matches[match],oddsDf])

def bet365Soccer(driver, matches, leagueTeams, url):
    teamsBox,oddsBox = bet365(driver,url,BET365_EPL_TEAM_NAME_SELECTOR)
    oddsIndex = 0
    matchesTmp = []
    for i in range(0,len(teamsBox),2):
        teamA, teamB = findTeams(teamsBox[i].text,teamsBox[i+1].text,leagueTeams)
        matchesTmp.append(Match(teamA,teamB))

    odds = [Odds() for i in range(len(matchesTmp))] 
    oddsIndex = 0
    for i in range(0,int(len(teamsBox)/2)):
        odds[oddsIndex].teamAOdds1x2 = bet3651x2(oddsBox[i].text)
        oddsIndex += 1
    oddsIndex = 0
    for i in range(int(len(teamsBox)/2),len(teamsBox)):
        odds[oddsIndex].drawOdds1x2 = bet3651x2(oddsBox[i].text)
        oddsIndex += 1
    oddsIndex = 0
    for i in range((len(teamsBox)),3*int(len(teamsBox)/2)):
        odds[oddsIndex].teamBOdds1x2 = bet3651x2(oddsBox[i].text)
        oddsIndex += 1
    for i in range(len(matchesTmp)):
        match, odd = standardizeMatchOdds(matchesTmp[i].teamA,matchesTmp[i].teamB,odds[i].teamAOdds,odds[i].teamBOdds,odds[i].teamAOdds1x2,odds[i].drawOdds1x2,odds[i].teamBOdds1x2,odds[i].teamASpreadHandicap,odds[i].teamAOddsHandicap,odds[i].teamBSpreadHandicap,odds[i].teamBOddsHandicap,odds[i].underPoints,odds[i].underOdds,odds[i].overPoints,odds[i].overOdds)
        oddsDf = pd.DataFrame.from_records([odd.__dict__],index=["bet365"])
        matches[match] = pd.concat([matches[match],oddsDf])