from fuzzywuzzy import fuzz

NOSCORE = 100

class Match:
    def __init__(self, teamA, teamB):
        self.teamA = teamA
        self.teamB = teamB
        
    def __eq__(self,other):
        if isinstance(other, Match):
            return self.teamA == other.teamA and self.teamB == other.teamB or self.teamA == other.teamB and self.teamB == other.teamA
        
    def __hash__(self):
        return hash(self.teamA) + hash(self.teamB)    
    
    def __str__(self):
        return "Team A:" + self.teamA + " Team B:" + self.teamB
    
    def similar(self,other):
        s,t = self.teamA.lower()+self.teamB.lower(),other.teamA.lower()+other.teamB.lower()
        #score = fuzz.ratio(s,t)
        #score1 = fuzz.partial_ratio(s,t)
        #score2 = fuzz.token_sort_ratio(s,t)
        score3 = fuzz.token_set_ratio(s,t)
        #score4 = fuzz.WRatio(s,t)
        #print("Score for " + self.teamA.lower() + " " + self.teamB.lower() + " vs " + other.teamA.lower() + " " + other.teamB.lower() + ": " + str(score) + " " + str(score1) + " " + str(score2) + " " +str(score3) + " "+ str(score4))
        return score3 > 70

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
           
    
def standardizeMatchOdds(teamA,
                         teamB,
                         teamAOdds,
                         teamBOdds,
                         teamAOdds1x2, 
                         drawOdds1x2, 
                         teamBOdds1x2, 
                         teamASpreadHandicap,
                         teamAOddsHandicap,
                         teamBSpreadHandicap,
                         teamBOddsHandicap,
                         underPoints = None,
                         underOdds = None,
                         overPoints = None,
                         overOdds = None
                         ):
    if teamA < teamB:
        return (Match(teamA,teamB),Odds(
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
            overOdds))
    else:
        return (Match(teamB,teamA),Odds(
            teamBOdds,
            teamAOdds,
            teamBOdds1x2,
            drawOdds1x2,
            teamAOdds1x2,
            teamBSpreadHandicap,
            teamBOddsHandicap,
            teamASpreadHandicap,
            teamAOddsHandicap,
            underPoints,
            underOdds,
            overPoints,
            overOdds))


def calculateScore1x2(odd1,odd2):
    try:
        maxTeamAOdds1x2 = max(odd1.teamAOdds1x2,odd2.teamAOdds1x2)
        maxDrawOdds1x2 = max(odd1.drawOdds1x2, odd2.drawOdds1x2)
        maxTeamBOdds1x2 = max(odd1.teamBOdds1x2, odd2.teamBOdds1x2)
        return 1/maxTeamAOdds1x2 + 1/maxDrawOdds1x2 + 1/maxTeamBOdds1x2
    except:
        return NOSCORE

def calculateScoreHandicap(odd1, odd2):
    try:
        if odd1.teamASpreadHandicap == odd2.teamASpreadHandicap and odd1.teamBSpreadHandicap == odd2.teamBSpreadHandicap:
            maxTeamAOddsHandicap = max(odd1.teamAOddsHandicap,odd2.teamAOddsHandicap)
            maxTeamBOddsHandicap = max(odd1.teamBOddsHandicap,odd2.teamBOddsHandicap)
            return 1/maxTeamAOddsHandicap + 1/maxTeamBOddsHandicap
        else:
            return NOSCORE
    except:
        return NOSCORE

def calculateScoreMiddleHandicap(odd1,odd2):
    try:
        # Probably a better way to calculate this
        if odd1.teamASpreadHandicap != odd2.teamASpreadHandicap or odd1.teamBSpreadHandicap != odd2.teamBSpreadHandicap:
            if abs(odd1.teamASpreadHandicap) > abs(odd2.teamASpreadHandicap):
                maxWebsiteOddsHandicap = odd1.teamAOddsHandicap if odd1.teamASpreadHandicap > 0 else odd1.teamBOddsHandicap
                maxWebsite2OddsHandicap = odd2.teamAOddsHandicap if odd2.teamASpreadHandicap < 0 else odd2.teamBOddsHandicap
                return 1/maxWebsiteOddsHandicap + 1/maxWebsite2OddsHandicap
            elif abs(odd1.teamASpreadHandicap) < abs(odd2.teamASpreadHandicap):
                maxWebsiteOddsHandicap = odd1.teamAOddsHandicap if odd1.teamASpreadHandicap < 0 else odd1.teamBOddsHandicap
                maxWebsite2OddsHandicap = odd2.teamAOddsHandicap if odd2.teamASpreadHandicap > 0 else odd2.teamBOddsHandicap
                return 1/maxWebsiteOddsHandicap + 1/maxWebsite2OddsHandicap
            else:
                # Not sure how to deal with 0
                return NOSCORE
        return NOSCORE
    except:
        return NOSCORE
def calculateScoreMiddleOverUnder(odd1,odd2):
    try:
        # Probably a better way to calculate this
        if odd1.underPoints != odd2.underPoints or odd1.overPoints != odd2.overPoints:
            if abs(odd1.underPoints) > abs(odd2.underPoints):
                maxWebsiteOddsOverUnder = odd1.underOdds
                maxWebsite2OddsOverUnder = odd2.overOdds
                return 1/maxWebsiteOddsOverUnder + 1/maxWebsite2OddsOverUnder
            elif abs(odd1.underPoints) < abs(odd2.underPoints):
                maxWebsiteOddsOverUnder = odd1.overOdds
                maxWebsite2OddsOverUnder = odd2.underOdds
                return 1/maxWebsiteOddsOverUnder + 1/maxWebsite2OddsOverUnder
            else:
                # Not sure how to deal with 0
                return NOSCORE
        return NOSCORE
    except:
        return NOSCORE


def calculateScoreOverUnder(odd1, odd2):
    try:
        if odd1.underPoints == odd2.underPoints and odd1.overPoints == odd2.overPoints:
            maxUnderOdds = max(odd1.underOdds,odd2.underOdds)
            maxOverOdds = max(odd1.overOdds,odd2.overOdds)
            return 1/maxUnderOdds + 1/maxOverOdds
        return NOSCORE
    except:
        return NOSCORE
    
def calculateScoreMoneyLine(odd1,odd2):
    try:
        maxTeamAOdds1x2 = max(odd1.teamAOdds,odd2.teamAOdds)
        maxTeamBOdds1x2 = max(odd1.teamBOdds, odd2.teamBOdds)

        return 1/maxTeamAOdds1x2 + 1/maxTeamBOdds1x2
    except:
        return NOSCORE

def calculateScore(match,odds):
    score1x2 = calculateScore1x2(odds[0],odds[1])
    scoreHandicap = calculateScoreHandicap(odds[0],odds[1])
    scoreOverUnder = calculateScoreOverUnder(odds[0],odds[1])
    scoreMiddleHandicap = calculateScoreMiddleHandicap(odds[0],odds[1])
    scoreMiddleOverUnder = calculateScoreMiddleOverUnder(odds[0],odds[1])
    scoreMoneyLine = calculateScoreMoneyLine(odds[0],odds[1])
    if scoreMoneyLine < 1:
        print("Score for Moneyline: " + str(scoreMoneyLine) + "\n")
        print(match.__dict__)
        print(str(odds[0].__dict__) + str(odds[1].__dict__))
    if score1x2 < 1:
        print("Score for 1x2: " + str(score1x2) + "\n")
        print(match.__dict__)
        print(str(odds[0].__dict__) + str(odds[1].__dict__))
        return True
    if scoreHandicap < 1:
        print("Score for Handicap: " + str(scoreHandicap) + "\n")
        print(match.__dict__)
        print(str(odds[0].__dict__) + str(odds[1].__dict__))
        return True
    if scoreOverUnder < 1:
        print("Score for Over Under: " + str(scoreOverUnder) + "\n")
        print(match.__dict__)
        print(str(odds[0].__dict__) + str(odds[1].__dict__))
    if scoreMiddleHandicap < 1:
        print("Score for Middle Handicap: " + str(scoreMiddleHandicap) + "\n")
        print(match.__dict__)
        print(str(odds[0].__dict__) + str(odds[1].__dict__))
        return True
    if scoreMiddleOverUnder < 1:
        print("Score for Middle Over Under: " + str(scoreMiddleOverUnder) + "\n")
        print(match.__dict__)
        print(str(odds[0].__dict__) + str(odds[1].__dict__))
        return True
    return False
    
def americanToDecimal(american):
    if american >= 0:
        return round(1+american/100,3)
    return round(1 - 100/american,3)
