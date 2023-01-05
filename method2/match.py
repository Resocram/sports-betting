NOSCORE = 100

class Match:
    def __init__(self, teamA, teamB):
        self.teamA = teamA
        self.teamB = teamB
    
    def __str__(self):
        return "Team A:" + self.teamA + " Team B:" + self.teamB

class Odds:
    def __init__(self,
                  teamAOdds,
                  teamBOdds,
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
                  ):
         self.teamAOdds = teamAOdds
         self.teamBOdds = teamBOdds
         
         self.teamAOdds1x2 = teamAOdds1x2
         self.drawOdds1x2 = drawOdds1x2
         self.teamBOdds1x2 = teamBOdds1x2
         
         self.teamASpreadHandicap = teamASpreadHandicap
         self.teamAOddsHandicap = teamAOddsHandicap
         self.teamBSpreadHandicap = teamBSpreadHandicap
         self.teamBOddsHandicap = teamBOddsHandicap
         
         self.underPoints = underPoints
         self.underOdds = underOdds
         self.overPoints = overPoints
         self.overOdds = overOdds
    def __str__(self):
        return str(self.__dict__)

def spread(spreadBox):
    spreadBox = spreadBox.split("\n")
    if len(spreadBox) == 4:
        teamASpreadHandicap = None if spreadBox[0] == "OFF" else float(spreadBox[0])
        teamAOddsHandicap = None if spreadBox[1] == "OFF" else float(spreadBox[1])
        teamBSpreadHandicap = None if spreadBox[2] == "OFF" else float(spreadBox[2])
        teamBOddsHandicap = None if spreadBox[3] == "OFF" else float(spreadBox[3])
        if teamASpreadHandicap + teamBSpreadHandicap == 0:
            return teamASpreadHandicap, teamAOddsHandicap, teamBSpreadHandicap, teamBOddsHandicap
        else:
            return None, None, None, None
    return None, None, None, None

def moneyline(moneyBox):
    moneyBox = moneyBox.split("\n")
    if len(moneyBox) == 2:
        teamAOdds = None if moneyBox[0] == "OFF" else float(moneyBox[0])
        teamBOdds = None if moneyBox[1] == "OFF" else float(moneyBox[1])
        return teamAOdds, teamBOdds
    return None, None

def totals(totalBox):
    totalBox = totalBox.split("\n")
    if len(totalBox) == 4:
        overPoints = None if totalBox[0] == "OFF" else float(totalBox[0].split(" ")[1])
        overOdds =  None if totalBox[1] == "OFF" else float(totalBox[1])
        underPoints =  None if totalBox[2] == "OFF" else float(totalBox[2].split(" ")[1])
        underOdds =  None if totalBox[3] == "OFF" else float(totalBox[3])
        if overPoints <= underPoints:
            return underPoints, underOdds, overPoints, overOdds
        else:
            return None, None, None, None
    return None, None, None, None

def oneXtwo(oneXtwoBox):
    return 1 if oneXtwoBox == "OFF" else float(oneXtwoBox)


def calculateScoreHandicap(odds):
    if odds.teamAOddsHandicap is not None and odds.teamBOddsHandicap is not None:
        return 1/odds.teamAOddsHandicap + 1/odds.teamBOddsHandicap
    return NOSCORE


def calculateScoreOverUnder(odds):
    if odds.underOdds is not None and odds.overOdds is not None:
        return 1/odds.underOdds + 1/odds.overOdds
    return NOSCORE

def calculateScoreMoneyLine(odds):
    if odds.teamAOdds is not None and odds.teamBOdds is not None:
        return 1/odds.teamAOdds + 1/odds.teamBOdds
    return NOSCORE


def calculateScore(match,odds):
    scoreHandicap = calculateScoreHandicap(odds)
    scoreOverUnder = calculateScoreOverUnder(odds)
    scoreMoneyLine = calculateScoreMoneyLine(odds)
    if scoreMoneyLine < 1:
        print("Score for Moneyline: " + str(scoreMoneyLine))
        print(match)
        print(odds)
        print("\n")
        return True
    if scoreHandicap < 1:
        print("Score for Handicap: " + str(scoreHandicap))
        print(match)
        print(odds)
        print("\n")
        return True
    if scoreOverUnder < 1:
        print("Score for Over Under: " + str(scoreOverUnder))
        print(match)
        print(odds)
        print("\n")
        return True
    return False

