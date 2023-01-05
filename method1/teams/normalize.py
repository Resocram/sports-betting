from fuzzywuzzy import fuzz
from teams import *
            
def findTeams(teamA,teamB,teams):
    newTeamA = ""
    newTeamAScore = 0
    newTeamB = ""
    newTeamBScore = 0
    for team in teams:
        if fuzz.WRatio(teamA,team) >= newTeamAScore:
            newTeamAScore = fuzz.WRatio(teamA,team)
            newTeamA = team
        if fuzz.WRatio(teamB,team) >= newTeamBScore:
            newTeamBScore = fuzz.WRatio(teamB,team)
            newTeamB = team
    if newTeamAScore < 70 or newTeamBScore < 70:
        print("Low matching score for teams")
        print(teamA)
        print(teamB)
        print("matched")
        print(newTeamA)
        print(newTeamB)
    return newTeamA, newTeamB
        