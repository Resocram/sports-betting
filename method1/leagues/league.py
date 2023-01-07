from leagues.teams import *
from leagues.url import *

class League:
    def __init__(self,name,teams,urls):
        self.name = name
        self.teams = teams
        self.urls = urls
        
NHL = League("NHL",NHL_TEAMS,NHL_URLS)
NBA = League("NBA",NBA_TEAMS,NBA_URLS)
NCAAB = League("NCAAB", NCAAB_TEAMS, NCAAB_URLS)
NFL = League("NFL", NFL_TEAMS, NFL_URLS)
EPL = League("EPL", EPL_TEAMS, EPL_URLS)
CBA = League("CBA", CBA_TEAMS, CBA_URLS)
EUROLEAGUE = League("EUROLEAGUE", EUROLEAGUE_TEAMS, EUROLEAGUE_URLS)
LALIGA = League("LALIGA", LALIGA_TEAMS, LALIGA_URLS)
KHL = League("KHL", KHL_TEAMS, KHL_URLS)
SHL = League("SHL", SHL_TEAMS,SHL_URLS)
ELH = League("ELH", ELH_TEAMS, ELH_URLS)
LIIGA = League("LIIGA", LIIGA_TEAMS, LIIGA_URLS)