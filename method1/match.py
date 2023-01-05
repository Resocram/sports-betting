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
        return self.teamA + " vs " + self.teamB

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


def calculateScore1x2(oddsDf):
    maxTeamAOdds1x2 = oddsDf["teamAOdds1x2"].max()
    maxDrawOdds1x2 = oddsDf["drawOdds1x2"].max()
    maxTeamBOdds1x2 = oddsDf["teamBOdds1x2"].max()   
    score = 1/maxTeamAOdds1x2 + 1/maxDrawOdds1x2 + 1/maxTeamBOdds1x2
    if score < 1:
        web1 = oddsDf["teamAOdds1x2"].idxmax()
        web2 = oddsDf["drawOdds1x2"].idxmax()
        web3 = oddsDf["teamBOdds1x2"].idxmax()
        return score, web1,web2,web3
    else:
        return score, None, None, None

def calculateScoreHandicap(oddsDf):
    uniqueHandicaps = oddsDf["teamASpreadHandicap"].unique()
    for handicap in uniqueHandicaps:
        newDf = oddsDf[oddsDf['teamASpreadHandicap'] == handicap]
        maxTeamAOddsHandicap = newDf["teamAOddsHandicap"].max()
        maxTeamBOddsHandicap = newDf["teamBOddsHandicap"].max()
        score = 1/maxTeamAOddsHandicap + 1/maxTeamBOddsHandicap
        if score < 1:
            web1 = newDf["teamAOddsHandicap"].idxmax()
            web2 = newDf["teamBOddsHandicap"].idxmax()
            return score, web1, web2 
    return score, None, None

def calculateScoreOverUnder(oddsDf):
    uniquePoints = oddsDf["underPoints"]
    for points in uniquePoints:
        newDf = oddsDf[oddsDf["underPoints"] == points]
        maxUnderOdds = newDf["underOdds"].max()
        maxOverOdds = newDf["overOdds"].max()
        score = 1/maxUnderOdds + 1/maxOverOdds
        if score < 1:
            web1 = newDf["underOdds"].idxmax()
            web2 = newDf["overOdds"].idxmax()
            return score, web1, web2 
    return score, None, None
    
def calculateScoreMoneyLine(oddsDf):
    maxTeamAOdds = oddsDf["teamAOdds"].max()
    maxTeamBOdds = oddsDf["teamBOdds"].max()   
    score = 1/maxTeamAOdds + 1/maxTeamBOdds
    if score < 1:
        web1 = oddsDf["teamAOdds"].idxmax()
        web2 = oddsDf["teamBOdds"].idxmax()
        return score, web1,web2
    else:
        return score, None, None


def calculateScore(match, oddsDf):
    
    scoreMoneyLine = calculateScoreMoneyLine(oddsDf)
    score1x2 = calculateScore1x2(oddsDf)
    scoreHandicap = calculateScoreHandicap(oddsDf)
    scoreOverUnder = calculateScoreOverUnder(oddsDf)
    
    if scoreMoneyLine[0] < 1:
        print("==========")
        print("Score for Moneyline: " + str(scoreMoneyLine[0]))
        print(match)
        print(scoreMoneyLine[1])
        print(oddsDf.loc[scoreMoneyLine[1],["teamAOdds","teamBOdds"]].to_string())
        print(scoreMoneyLine[2])
        print(oddsDf.loc[scoreMoneyLine[2],["teamAOdds","teamBOdds"]].to_string())
        print("==========")
    if score1x2[0] < 1:
        print("==========")
        print("Score for 1x2: " + str(score1x2[0]))
        print(match)
        print(score1x2[1])
        print(oddsDf.loc[scoreMoneyLine[1],["teamAOdds1x2","drawOdds1x2","teamBOdds1x2"]].to_string())
        print(score1x2[2])
        print(oddsDf.loc[scoreMoneyLine[2],["teamAOdds1x2","drawOdds1x2","teamBOdds1x2"]].to_string())
        print(score1x2[3])
        print(oddsDf.loc[scoreMoneyLine[3],["teamAOdds1x2","drawOdds1x2","teamBOdds1x2"]].to_string())
        print("==========")
    if scoreHandicap[0] < 1:
        print("==========")
        print("Score for Handicap: " + str(scoreHandicap[0]))
        print(match)
        print(scoreHandicap[1])
        print(oddsDf.loc[scoreMoneyLine[1],["teamASpreadHandicap","teamAOddsHandicap","teamBSpreadHandicap","teamBOddsHandicap"]].to_string())
        print(scoreHandicap[2])
        print(oddsDf.loc[scoreMoneyLine[2],["teamASpreadHandicap","teamAOddsHandicap","teamBSpreadHandicap","teamBOddsHandicap"]].to_string())
        print("==========")
    if scoreOverUnder[0] < 1:
        print("==========")
        print("Score for Over Under: " + str(scoreOverUnder[0]))
        print(match)
        print(scoreMoneyLine[1])
        print(oddsDf.loc[scoreMoneyLine[1],["underPoints","underOdds","overPoints","overOdds"]].to_string())
        print(scoreMoneyLine[2])
        print(oddsDf.loc[scoreMoneyLine[2],["underPoints","underOdds","overPoints","overOdds"]].to_string())
        print("==========")
    
def americanToDecimal(american):
    if american >= 0:
        return round(1+american/100,3)
    return round(1 - 100/american,3)




# TODO: Add support for middle betting
# def calculateScoreMiddleHandicap(odd1,odd2):
#     try:
#         # Probably a better way to calculate this
#         if odd1.teamASpreadHandicap != odd2.teamASpreadHandicap or odd1.teamBSpreadHandicap != odd2.teamBSpreadHandicap:
#             if abs(odd1.teamASpreadHandicap) > abs(odd2.teamASpreadHandicap):
#                 maxWebsiteOddsHandicap = odd1.teamAOddsHandicap if odd1.teamASpreadHandicap > 0 else odd1.teamBOddsHandicap
#                 maxWebsite2OddsHandicap = odd2.teamAOddsHandicap if odd2.teamASpreadHandicap < 0 else odd2.teamBOddsHandicap
#                 return 1/maxWebsiteOddsHandicap + 1/maxWebsite2OddsHandicap
#             elif abs(odd1.teamASpreadHandicap) < abs(odd2.teamASpreadHandicap):
#                 maxWebsiteOddsHandicap = odd1.teamAOddsHandicap if odd1.teamASpreadHandicap < 0 else odd1.teamBOddsHandicap
#                 maxWebsite2OddsHandicap = odd2.teamAOddsHandicap if odd2.teamASpreadHandicap > 0 else odd2.teamBOddsHandicap
#                 return 1/maxWebsiteOddsHandicap + 1/maxWebsite2OddsHandicap
#             else:
#                 # Not sure how to deal with 0
#                 return NOSCORE
#         return NOSCORE
#     except:
#         return NOSCORE

# TODO: Add support for middle betting
# def calculateScoreMiddleOverUnder(odd1,odd2):
#     try:
#         # Probably a better way to calculate this
#         if odd1.underPoints != odd2.underPoints or odd1.overPoints != odd2.overPoints:
#             if abs(odd1.underPoints) > abs(odd2.underPoints):
#                 maxWebsiteOddsOverUnder = odd1.underOdds
#                 maxWebsite2OddsOverUnder = odd2.overOdds
#                 return 1/maxWebsiteOddsOverUnder + 1/maxWebsite2OddsOverUnder
#             elif abs(odd1.underPoints) < abs(odd2.underPoints):
#                 maxWebsiteOddsOverUnder = odd1.overOdds
#                 maxWebsite2OddsOverUnder = odd2.underOdds
#                 return 1/maxWebsiteOddsOverUnder + 1/maxWebsite2OddsOverUnder
#             else:
#                 # Not sure how to deal with 0
#                 return NOSCORE
#         return NOSCORE
#     except:
#         return NOSCORE
