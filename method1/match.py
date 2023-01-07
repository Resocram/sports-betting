import http.client, urllib

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
                  teamAOdds = None,
                  teamBOdds = None,
                  teamAOdds1x2 = None,
                  drawOdds1x2 = None,
                  teamBOdds1x2 = None,
                  teamASpreadHandicap = None,
                  teamAOddsHandicap = None,
                  teamBSpreadHandicap = None,
                  teamBOddsHandicap = None,
                  underPoints = None,
                  underOdds = None,
                  overPoints = None,
                  overOdds  = None
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
        if web1 == web2 and web2 == web3:
            return score, None, None, None
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
            if web1 == web2:
                return score, None, None
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
            if web1 == web2:
                return score, None, None
            return score, web1, web2 
    return score, None, None
    
def calculateScoreMoneyLine(oddsDf):
    maxTeamAOdds = oddsDf["teamAOdds"].max()
    maxTeamBOdds = oddsDf["teamBOdds"].max()   
    score = 1/maxTeamAOdds + 1/maxTeamBOdds
    if score < 1:
        web1 = oddsDf["teamAOdds"].idxmax()
        web2 = oddsDf["teamBOdds"].idxmax()
        if web1 == web2:
            return score, None, None
        return score, web1,web2
    else:
        return score, None, None


def calculateScore(match, oddsDf):
    
    scoreMoneyLine = calculateScoreMoneyLine(oddsDf)
    score1x2 = calculateScore1x2(oddsDf)
    scoreHandicap = calculateScoreHandicap(oddsDf)
    scoreOverUnder = calculateScoreOverUnder(oddsDf)
    
    if scoreMoneyLine[0] < 1 and scoreMoneyLine[1] != None and scoreMoneyLine[2] != None:
        msg = "==========" + "\n" + \
              "Score for Moneyline: " + str(scoreMoneyLine[0]) + "\n" + \
              str(match) + "\n" + \
              str(scoreMoneyLine[1]) + "\n" + \
              oddsDf.loc[scoreMoneyLine[1],["teamAOdds","teamBOdds"]].to_string() + "\n" + \
              str(scoreMoneyLine[2]) + "\n" + \
              oddsDf.loc[scoreMoneyLine[2],["teamAOdds","teamBOdds"]].to_string()+ "\n" + \
              "=========="
        print(msg)
        send(msg)
    if score1x2[0] < 1 and score1x2[1] != None and score1x2[2] != None and score1x2[3] != None:
        msg = "==========" + "\n" + \
              "Score for 1x2: " + str(score1x2[0]) + "\n" +  \
              str(match) + "\n" + \
              str(score1x2[1]) + "\n" + \
              oddsDf.loc[score1x2[1],["teamAOdds1x2","drawOdds1x2","teamBOdds1x2"]].to_string() + "\n" + \
              str*score1x2[2]() + "\n" + \
              oddsDf.loc[score1x2[2],["teamAOdds1x2","drawOdds1x2","teamBOdds1x2"]].to_string() + "\n" + \
              str(score1x2[3]) + "\n" + \
              oddsDf.loc[score1x2[3],["teamAOdds1x2","drawOdds1x2","teamBOdds1x2"]].to_string() + "\n" + \
              "=========="
        print(msg)
        send(msg)
    if scoreHandicap[0] < 1 and scoreHandicap[1] != None and scoreHandicap[2] != None:
        msg = "==========" + "\n" + \
              "Score for Handicap: " + str(scoreHandicap[0]) + "\n" + \
              str(match) + "\n" + \
              str(scoreHandicap[1]) + "\n" + \
              oddsDf.loc[scoreHandicap[1],["teamASpreadHandicap","teamAOddsHandicap","teamBSpreadHandicap","teamBOddsHandicap"]].to_string() + "\n" + \
              str(scoreHandicap[2]) + "\n" + \
              oddsDf.loc[scoreHandicap[2],["teamASpreadHandicap","teamAOddsHandicap","teamBSpreadHandicap","teamBOddsHandicap"]].to_string() + "\n" + \
              "=========="
        print(msg)
        send(msg)
    if scoreOverUnder[0] < 1 and scoreOverUnder[1] != None and scoreOverUnder[2] != None:
        msg = "==========" + "\n" + \
              "Score for Over Under: " + str(scoreOverUnder[0]) + "\n" + \
              str(match) + "\n" + \
              str(scoreOverUnder[1]) + "\n" + \
              oddsDf.loc[scoreOverUnder[1],["underPoints","underOdds","overPoints","overOdds"]].to_string() + "\n" + \
              str(scoreOverUnder[2]) + "\n" + \
              oddsDf.loc[scoreOverUnder[2],["underPoints","underOdds","overPoints","overOdds"]].to_string() + "\n" + \
              "=========="
        print(msg)
        send(msg)
              
def americanToDecimal(american):
    if american >= 0:
        return round(1+american/100,3)
    return round(1 - 100/american,3)

def send(msg):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": "a3uxep39ni2r8cwoyks8zhfdqzf8ui",
        "user": "ufsr1fk5oe2zcbukgszoqgrvqepeob",
        "message": msg,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()



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
