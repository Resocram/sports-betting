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
PINNACLE_HOCKEY_URL = "https://www.pinnacle.com/en/hockey/matchups"
BODOG_HOCKEY_URL = "https://www.bodog.eu/sports/hockey"
BET99_HOCKEY_URL = "https://bet99.com/en/sport-betting#/alltopevents/events/70"

SPORTSBET_BASKETBALL_URL ="https://sportsbet.io/sports/basketball/matches/today"
PINNACLE_BASKETBALL_URL = "https://www.pinnacle.com/en/basketball/matchups"
BODOG_BASKETBALL_URL = "https://www.bodog.eu/sports/basketball"
BET99_BASKETBALL_URL = "https://bet99.com/en/sport-betting#/alltopevents/events/67"

PINNABLE_FOOTBALL_URL = "https://www.pinnacle.com/en/football/matchups"
BODOG_FOOTBALL_URL = "https://www.bodog.eu/sports/football"
BET99_FOOTBALL_URL = "https://bet99.com/en/sport-betting#/alltopevents/events/75    "

PINNACLE_SOCCER_URL = "https://www.pinnacle.com/en/soccer/matchups/highlights"
BODOG_SOCCER_URL = "https://www.bodog.eu/sports/soccer"
BET99_SOCCER_URL = "https://bet99.com/en/sport-betting#/alltopevents/events/66"

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

def bet99Hockey():
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
    bodogMatches = bet99Hockey()
    
    print("Scraped bet99")
    pinnacleMatches = pinnacleHockey()
    print("Scraped pinnacle")
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
    for match in matches:
        print(match[0].__dict__)
        print(match[1].__dict__)
        print("\n")

    return matches

def bet99Basketball():
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
    pinnacleMatches = bet99Basketball()
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

def bet99Football():
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
    pinnacleMatches = bet99Football()
    print("Scraped pinnacle")
    bodogMatches = bodogFootball()
    print("Scraped bodog")
    for matchA in pinnacleMatches:
        for matchB in bodogMatches:
            if matchA[0].similar(matchB[0]):
                calculateScore(matchA[0],[matchA[1],matchB[1]])

    print("done :)")
    
def pinnacleSoccer():
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

def bodogSoccer():
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
                                teamBOddsHandicap
                                )
        odds.overPoints = overPoints
        odds.overOdds = overOdds
        odds.underPoints = underPoints
        odds.underOdds = underOdds
        matches.append((match,odds))
        oddsIndex += 1  
    return matches

def bet99Soccer():
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
                            None
                            )
        odds.overPoints = overPoints
        odds.overOdds = overOdds
        odds.underPoints = underPoints
        odds.underOdds = underOdds
        matches.append((match,odds))
        oddsIndex += 1 
    return matches

def soccer():
    bet99Matches = bet99Soccer()
    print("Scraped bet99Matches")
    bodogMatches = bodogSoccer()
    print("Scraped bodog")
    for match in bet99Matches:
        print(match[0])
        print(match[1].__dict__)
    print("==========")
    for match in bodogMatches:
        print(match[0])
        print(match[1].__dict__)
    for matchA in bet99Matches:
        for matchB in bodogMatches:
            if matchA[0].similar(matchB[0]):
                print(matchA[0])
                print(matchA[1].__dict__)
                print(matchB[1].__dict__)
                calculateScore(matchA[0],[matchA[1],matchB[1]])

    print("done :)")
#hockey()
#basketball()
football()
#soccer()

time.sleep(1000)