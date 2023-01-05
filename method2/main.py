import undetected_chromedriver.v2 as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from match import *
from urls import *
op = webdriver.ChromeOptions()
op.add_argument('--headless')
driver = uc.Chrome(options=op)

def getBoxes(url,soccer=False):
    driver.get(url)
    TEAMS = ".list-unstyled.sport-team-matrix"
    ODDS = ".totals"
    if soccer:
        ODDS = ".select-odds"

    teamsBox = driver.find_elements(By.CSS_SELECTOR, TEAMS)
    oddsBox = driver.find_elements(By.CSS_SELECTOR, ODDS)
    return teamsBox,oddsBox

def football(url):
    teamsBox, oddsBox = getBoxes(url)

    matches = []
    for team in teamsBox:   
        txt = team.text
        if len(txt) != 0:
            teamA,teamB = txt.split("\n")
            matches.append(Match(teamA,teamB))
    odds = []
    for i in range(0,len(oddsBox),3):
        txt = oddsBox[i].text
        txt1 = oddsBox[i+1].text
        txt2 = oddsBox[i+2].text
        if len(txt) != 0 and len(txt1) != 0 and len(txt2) != 0:
            teamASpreadHandicap,teamAOddsHandicap,teamBSpreadHandicap,teamBOddsHandicap = spread(txt)
            teamAOdds, teamBOdds = moneyline(txt1)
            underPoints, underOdds, overPoints, overOdds = totals(txt2)
            odds.append(Odds(teamAOdds,
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
                            ))
    return matches,odds

def hockey(url):
    teamsBox, oddsBox = getBoxes(url)

    matches = []
    for team in teamsBox:   
        txt = team.text
        if len(txt) != 0:
            teamA,teamB = txt.split("\n")
            matches.append(Match(teamA,teamB))
    odds = []
    for i in range(0,len(oddsBox),3):
        txt = oddsBox[i].text
        txt1 = oddsBox[i+1].text
        txt2 = oddsBox[i+2].text
        if len(txt) != 0 and len(txt1) != 0 and len(txt2) != 0:
            teamAOdds, teamBOdds = moneyline(txt)
            underPoints, underOdds, overPoints, overOdds = totals(txt1)
            teamASpreadHandicap,teamAOddsHandicap,teamBSpreadHandicap,teamBOddsHandicap = spread(txt2)
            odds.append(Odds(teamAOdds,
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
                            ))
    return matches,odds

def basketball(url):
    teamsBox, oddsBox = getBoxes(url)

    matches = []
    for team in teamsBox:   
        txt = team.text
        if len(txt) != 0:
            teamA,teamB = txt.split("\n")
            matches.append(Match(teamA,teamB))
    odds = []
    for i in range(0,len(oddsBox),3):
        txt = oddsBox[i].text
        txt1 = oddsBox[i+1].text
        txt2 = oddsBox[i+2].text
        if len(txt) != 0 and len(txt1) != 0 and len(txt2) != 0:
            teamAOdds, teamBOdds = moneyline(txt)
            underPoints, underOdds, overPoints, overOdds = totals(txt1)
            teamASpreadHandicap,teamAOddsHandicap,teamBSpreadHandicap,teamBOddsHandicap = spread(txt2)
            odds.append(Odds(teamAOdds,
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
                            ))
    return matches,odds
        
def soccer(url):
    teamsBox, oddsBox = getBoxes(url,True)

    matches = []
    for team in teamsBox:   
        txt = team.text
        if len(txt) != 0:
            teamA,teamB = txt.split("vs ")
            matches.append(Match(teamA,teamB))
    odds = []
    for i in range(0,len(oddsBox),3):
        txt = oddsBox[i].text
        txt1 = oddsBox[i+1].text
        txt2 = oddsBox[i+2].text
        if len(txt) != 0 and len(txt1) != 0 and len(txt2) != 0:
            one = oneXtwo(txt)
            draw = oneXtwo(txt1)
            two = oneXtwo(txt2)
            odds.append(Odds(None,
                            None,
                            one,
                            draw,
                            two,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None
                            ))
    return matches,odds

def calculate(matches,odds):
    for i in range(min(len(matches),len(odds))):
        calculateScore(matches[i],odds[i])
            
def main():
    footballUrls = getFootballUrls()
    hockeyUrls = getHockeyUrls()
    basketballUrls = getBasketballUrls()
    soccerUrls = getSoccerUrls()
    
    for footballUrl in footballUrls:
        matches,odds = football(footballUrl)
        calculate(matches,odds)
        
    for hockeyUrl in hockeyUrls:
        matches,odds = hockey(hockeyUrl)
        calculate(matches,odds)
    
    for basketballUrl in basketballUrls:
        matches, odds = basketball(basketballUrl)
        calculate(matches,odds)
        
    for soccerUrl in soccerUrls:
        matches,odds = soccer(soccerUrl)
        calculate(matches,odds)
        
    

main()

