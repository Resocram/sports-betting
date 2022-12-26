from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import undetected_chromedriver.v2 as uc
from match import *
from collections import defaultdict
from sportsbet import *
driver = uc.Chrome()

SPORTSBET_HOCKEY_URL = "https://sportsbet.io/sports/ice-hockey/matches/today"
PINNACLE_HOCKEY_URL = "https://www.pinnacle.com/en/hockey/matchups/regulation"
BODOG_HOCKEY_URL = "https://www.bodog.eu/sports/hockey"

SPORTSBET_BASKETBALL_URL ="https://sportsbet.io/sports/basketball/matches/today"
PINNACLE_BASKETBALL_URL = "https://www.pinnacle.com/en/basketball/matchups"
BODOG_BASKETBALL_URL = "https://www.bodog.eu/sports/basketball"

PINNABLE_FOOTBALL_URL = "https://www.pinnacle.com/en/football/matchups"
BODOG_FOOTBALL_URL = "https://www.bodog.eu/sports/football"
# Hockey sportsbet
def sportsbetHockey():
    matches = []
    teamsBox, oddsBox = sportsbet(driver,SPORTSBET_HOCKEY_URL)
    oddsIndex = 0
    for i in range(0,len(teamsBox),2):
        teamAOdds1x2,drawOdds1x2,teamBOdds1x2 = sportsbetOdds1x2(oddsBox[oddsIndex])
        teamASpreadHandicap,teamAOddsHandicap,teamBSpreadHandicap,teamBOddsHandicap = sportsbetOddsHandicap(oddsBox[oddsIndex+1])
        teamA,teamB = teamsBox[i].text,teamsBox[i+1].text
        match, odds = standardizeMatchOdds(teamA,
                         teamB,
                         None,
                         None,
                         teamAOdds1x2, 
                         drawOdds1x2, 
                         teamBOdds1x2, 
                         teamASpreadHandicap,
                         teamAOddsHandicap,
                         teamBSpreadHandicap,
                         teamBOddsHandicap
                         )
        odds.overPoints, odds.overOdds, odds.underPoints,odds.underOdds = sportsbetOddsOverUnder(oddsBox[oddsIndex+2])
        matches.append((match,odds))
        oddsIndex += 3
    return matches

def pinnacleHockey():
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
        teamAOdds1x2, drawOdds1x2, teamBOdds1x2 = pinnacleOdds1x2(oddsBox[oddsIndex])
        teamASpreadHandicap,teamAOddsHandicap,teamBSpreadHandicap,teamBOddsHandicap = pinnacleOddsHandicap(oddsBox[oddsIndex+1])
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
                         teamBOddsHandicap
                         )
        odds.overPoints, odds.overOdds, odds.underPoints, odds.underOdds = pinnacleOddsOverUnder(oddsBox[oddsIndex+2])
        matches.append((match,odds))
        oddsIndex += 3
    return matches

def bodogHockey():
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
                                teamBOddsHandicap
                                )
        odds.overPoints = overPoints
        odds.overOdds = overOdds
        odds.underPoints = underPoints
        odds.underOdds = underOdds
        matches.append((match,odds))
        oddsIndex += 1  
    return matches

def hockey():
    pinnacleMatches = pinnacleHockey()
    print("Scraped pinnacle")
    bodogMatches = bodogHockey()
    print("Scraped bodog")

    for matchA in bodogMatches:
        for matchB in pinnacleMatches:
            if matchA[0].similar(matchB[0]):

                calculateScore(matchA[0],[matchA[1],matchB[1]])
    print("done :)")

# Basketball sportsbet
def sportsbetBasketball():
    matches = []
    teamsBox, oddsBox = sportsbet(driver,SPORTSBET_BASKETBALL_URL)
    oddsIndex = 0
    for i in range(0,len(teamsBox),2):
        teamAOdds, teamBOdds = sportsbetOddsMoneyline(oddsBox[oddsIndex])
        teamASpreadHandicap,teamAOddsHandicap,teamBSpreadHandicap,teamBOddsHandicap = sportsbetOddsHandicap(oddsBox[oddsIndex+1])
            
        teamA = teamsBox[i].text
        teamB = teamsBox[i+1].text
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
        odds.overPoints, odds.overOdds, odds.underPoints,odds.underOdds = sportsbetOddsOverUnder(oddsBox[oddsIndex+2])
        matches.append((match,odds))
        oddsIndex += 3
    return matches

def pinnacleBasketball():
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

def bodogBasketball():
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
                                teamBOddsHandicap
                                )
        odds.overPoints = overPoints
        odds.overOdds = overOdds
        odds.underPoints = underPoints
        odds.underOdds = underOdds
        matches.append((match,odds))
        oddsIndex += 1  
    return matches



def basketball():
    pinnacleMatches = pinnacleBasketball()
    print("Scraped pinnacle")
    bodogMatches = bodogBasketball()
    print("Scraped bodog")
    for matchA in pinnacleMatches:
        for matchB in bodogMatches:
            if matchA[0].similar(matchB[0]):
                calculateScore(matchA[0],[matchA[1],matchB[1]])

    print("done :)")
    
def pinnacleFootball():
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

def bodogFootball():
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
                                teamBOddsHandicap
                                )
        odds.overPoints = overPoints
        odds.overOdds = overOdds
        odds.underPoints = underPoints
        odds.underOdds = underOdds
        matches.append((match,odds))
        oddsIndex += 1  
    return matches

def football():
    pinnacleMatches = pinnacleFootball()
    print("Scraped pinnacle")
    bodogMatches = bodogFootball()
    print("Scraped bodog")
    for matchA in pinnacleMatches:
        for matchB in bodogMatches:
            if matchA[0].similar(matchB[0]):
                calculateScore(matchA[0],[matchA[1],matchB[1]])

    print("done :)")
hockey()
basketball()
football()

time.sleep(1000)