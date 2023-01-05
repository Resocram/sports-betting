# Code to get all URLS
# import undetected_chromedriver.v2 as uc
# from selenium.webdriver.common.by import By
# from match import *
# driver = uc.Chrome()

# driver.get("https://www.oddsjet.com/en-ca/england/league-1/odds")
# IDENTIFIER = ".list-unstyled.nav-sub-links > li > a"
# matches = driver.find_elements(By.CSS_SELECTOR, IDENTIFIER)

# for match in matches:
#     if len(match.text) != 0:
#         var = match.text.replace(" ","").replace("-","_") + "_URL"
#         value = match.get_attribute("href")
#         print(var + "=\"" + value+"\"")

# Football
NFL_URL="https://www.oddsjet.com/en-ca/nfl/odds"
#NFL_SuperBowlWinner_URL="https://www.oddsjet.com/en-ca/super-bowl/outright-winner/odds"
CFL_URL="https://www.oddsjet.com/en-ca/cfl/odds"
#CFL_GreyCupWinner_URL="https://www.oddsjet.com/en-ca/cfl/grey-cup/outright-winner/odds"
NCAAFootball_URL="https://www.oddsjet.com/en-ca/ncaa-football/odds"
NCAAFootball_NationalChampion_URL="https://www.oddsjet.com/en-ca/ncaa-football/nation-champion/outright/odds"

def getFootballUrls():
    return [NFL_URL,
            CFL_URL,
            NCAAFootball_URL,
            NCAAFootball_NationalChampion_URL]

# Hockey
NHL_URL="https://www.oddsjet.com/en-ca/nhl/odds"
#NHL_StanleyCupWinner_URL="https://www.oddsjet.com/en-ca/stanley-cup-winner/odds"
KHL_URL="https://www.oddsjet.com/en-ca/khl/odds"
AHL_URL="https://www.oddsjet.com/en-ca/ahl/odds"
Austria_EHL_URL="https://www.oddsjet.com/en-ca/austria/ehl/odds"
Czech_Extraliga_URL="https://www.oddsjet.com/en-ca/czech/extraliga/odds"
Denmark_MetalLigaen_URL="https://www.oddsjet.com/en-ca/denmark/metal-ligaen/odds"
Finland_SMLiiga_URL="https://www.oddsjet.com/en-ca/finland/sm-liiga/odds"
Germany_DEL_URL="https://www.oddsjet.com/en-ca/germany/del/odds"
Germany_DEL2_URL="https://www.oddsjet.com/en-ca/germany/del2/odds"
IIHFInternational_URL="https://www.oddsjet.com/en-ca/iihf/odds"
Norway_GET_ligaen_URL="https://www.oddsjet.com/en-ca/norway/eliteserien/odds"
Slovakia_Extraliga_URL="https://www.oddsjet.com/en-ca/slovakia/extraliga/odds"
Switzerland_NLA_URL="https://www.oddsjet.com/en-ca/switzerland/nla-hockey/odds"
Switzerland_NLB_URL="https://www.oddsjet.com/en-ca/switzerland/nlb-hockey/odds"
Sweden_SHL_URL="https://www.oddsjet.com/en-ca/sweden/shl/odds"
Sweden_HockeyAllsvenskan_URL="https://www.oddsjet.com/en-ca/hockeyallsvenskan/odds"

def getHockeyUrls():
    return [NHL_URL,
            KHL_URL,
            AHL_URL,
            Austria_EHL_URL,
            Czech_Extraliga_URL,
            Denmark_MetalLigaen_URL,
            Finland_SMLiiga_URL,
            Germany_DEL_URL,
            Germany_DEL2_URL,
            IIHFInternational_URL,
            Norway_GET_ligaen_URL,
            Slovakia_Extraliga_URL,
            Switzerland_NLA_URL,
            Switzerland_NLB_URL,
            Sweden_SHL_URL,
            Sweden_HockeyAllsvenskan_URL]

# Baseball (i dont even support baseball yet lol)
MLB_URL="https://www.oddsjet.com/en-ca/mlb/odds"
#MLB_WorldSeriesWinner_URL="https://www.oddsjet.com/en-ca/world-series/outright-winner/odds"
Japan_NPB_URL="https://www.oddsjet.com/en-ca/japan/baseball/odds"
Korea_KBO_URL="https://www.oddsjet.com/en-ca/korea/baseball/odds"
Mexico_LMB_URL="https://www.oddsjet.com/en-ca/mexico/baseball/odds"

def getBaseballUrls():
    return [MLB_URL,
            Japan_NPB_URL,
            Korea_KBO_URL,
            Mexico_LMB_URL]


# Basketball
NBA_URL="https://www.oddsjet.com/en-ca/nba/odds"
#NBAFinals_OutrightWinner_URL="https://www.oddsjet.com/en-ca/nba-finals/outright-winner/odds"
NCAA_USCollegeHoops_URL="https://www.oddsjet.com/en-ca/ncaa-basketball/odds"
#NCAAChampionship_OutrightWinner_URL="https://www.oddsjet.com/en-ca/ncaa-basketball/championship-winner/odds"
AdriaticLeague_ABALiga_URL="https://www.oddsjet.com/en-ca/aba-league/odds"
Argentina_LigaNacional_URL="https://www.oddsjet.com/en-ca/argentina/liga-nacional/odds"
Australia_NBL_URL="https://www.oddsjet.com/en-ca/australia/nbl/odds"
#Australia_NBL_OutrightWinner_URL="https://www.oddsjet.com/en-ca/australia/nbl/outright-winner/odds"
Brazil_NBB_URL="https://www.oddsjet.com/en-ca/brazil/nbb/odds"
China_CBA_URL="https://www.oddsjet.com/en-ca/chinese-basketball-association/odds"
Euroleague_URL="https://www.oddsjet.com/en-ca/euroleague/odds"
#Euroleague_OutrightWinner_URL="https://www.oddsjet.com/en-ca/euroleague/outright-winner/odds"
Eurocup_URL="https://www.oddsjet.com/en-ca/basketball/eurocup/odds"
FIBA_InternationalMatches_URL="https://www.oddsjet.com/en-ca/fiba/international/basketball/odds"
France_ProA_URL="https://www.oddsjet.com/en-ca/france/lnb-pro-a/odds"
France_ProB_URL="https://www.oddsjet.com/en-ca/france/lnb-pro-b/odds"
Germany_BasketballBundesliga_URL="https://www.oddsjet.com/en-ca/germany/bbl/odds"
#Germany_BBL_OutrightWinner_URL="https://www.oddsjet.com/en-ca/germany/bbl/outright-winner/odds"
Italy_LegaBasket_URL="https://www.oddsjet.com/en-ca/italy/lega-basket-serie-a/odds"
#Italy_LegaBasket_OutrightWinner_URL="https://www.oddsjet.com/en-ca/italy/lega-basket-serie-a/outright-winner/odds"
Lithuania_LKL_URL="https://www.oddsjet.com/en-ca/lithuania/lkl/odds"
#Lithuania_LKL_OutrightWinner_URL="https://www.oddsjet.com/en-ca/lithuania/lkl/outright-winner/odds"
Mexico_LNBP_URL="https://www.oddsjet.com/en-ca/mexico/lnbp/odds"
Poland_PLK_URL="https://www.oddsjet.com/en-ca/poland/plk/odds"
Russia_VTBUnitedLeague_URL="https://www.oddsjet.com/en-ca/russia/united-league/odds"
Spain_ACBLeague_URL="https://www.oddsjet.com/en-ca/spain/liga-acb/odds"
#Spain_LigaACB_OutrightWinner_URL="https://www.oddsjet.com/en-ca/spain/liga-acb/outright-winner/odds"
Turkey_BSL_URL="https://www.oddsjet.com/en-ca/turkey/bsl/odds"
#Turkey_BSL_OutrightWinner_URL="https://www.oddsjet.com/en-ca/turkey/bsl/outright-winner/odds"

def getBasketballUrls():
    return [NBA_URL,
            NCAA_USCollegeHoops_URL,
            AdriaticLeague_ABALiga_URL,
            Argentina_LigaNacional_URL,
            Australia_NBL_URL,
            Brazil_NBB_URL,
            China_CBA_URL,
            Euroleague_URL,
            Eurocup_URL,
            FIBA_InternationalMatches_URL,
            France_ProA_URL,
            France_ProB_URL,
            Germany_BasketballBundesliga_URL,
            Italy_LegaBasket_URL,
            Lithuania_LKL_URL,
            Mexico_LNBP_URL,
            Poland_PLK_URL,
            Russia_VTBUnitedLeague_URL,
            Spain_ACBLeague_URL,
            Turkey_BSL_URL]


# Soccer
InternationalMatches_URL="https://www.oddsjet.com/en-ca/international/soccer/odds"
MLS_URL="https://www.oddsjet.com/en-ca/mls/odds"
#MLSCup_OutrightWinner_URL="https://www.oddsjet.com/en-ca/mls-cup/outright-winner/odds"
CanadaPremierLeague_URL="https://www.oddsjet.com/en-ca/canadian-premier-league/odds"
ChampionsLeague_URL="https://www.oddsjet.com/en-ca/champions-league/odds"
#ChampionsLeague_OutrightWinner_URL="https://www.oddsjet.com/en-ca/champions-league/outright-winner/odds"
EuropaLeague_URL="https://www.oddsjet.com/en-ca/europa-league/odds"
#EuropaLeague_OutrightWinner_URL="https://www.oddsjet.com/en-ca/europa-league/outright-winner/odds"
EuropaConferenceLeague_URL="https://www.oddsjet.com/en-ca/europa-conference-league/odds"
UEFAEuro2024_OutrightWinner_URL="https://www.oddsjet.com/en-ca/uefa-euro/outright-winner/odds"
#2022WorldCup_OutrightWinner_URL="https://www.oddsjet.com/en-ca/fifa/world-cup/outright-winner/odds"
Argentina_PrimeraDivisión_URL="https://www.oddsjet.com/en-ca/argentina/primera-division/odds"
Argentina_Cup_URL="https://www.oddsjet.com/en-ca/argentina/cup/odds"
Australia_A_League_URL="https://www.oddsjet.com/en-ca/australia/a-league/odds"
#Australia_A_League_OutrightWinner_URL="https://www.oddsjet.com/en-ca/australia/a-league/outright-winner/odds"
Australia_FFACup_URL="https://www.oddsjet.com/en-ca/australia/ffa-cup/odds"
Austria_Bundesliga_URL="https://www.oddsjet.com/en-ca/austria/bundesliga/odds"
#Austria_Bundesliga_OutrightWinner_URL="https://www.oddsjet.com/en-ca/austria/bundesliga/outright-winner/odds"
Austria_ÖFBCup_URL="https://www.oddsjet.com/en-ca/austria/ofb-cup/odds"
Azerbaijan_PremierLeague_URL="https://www.oddsjet.com/en-ca/azerbaijan/premier-league/odds"
Belgium_ProLeague_URL="https://www.oddsjet.com/en-ca/belgium/pro-league/odds"
Belgium_Division2_URL="https://www.oddsjet.com/en-ca/belgium/division-2/odds"
Belgium_Cup_URL="https://www.oddsjet.com/en-ca/belgium/cup/odds"
Bolivia_ProfessionalLeague_URL="https://www.oddsjet.com/en-ca/bolivia-league/odds"
Bosnia_Herzegovina_PremierLiga_URL="https://www.oddsjet.com/en-ca/bosnia-herzegovina/premier-liga/odds"
Brazil_SerieA_URL="https://www.oddsjet.com/en-ca/brazil/serie-a/odds"
#Brazil_SerieA_OutrightWinner_URL="https://www.oddsjet.com/en-ca/brazil/serie-a/outright-winner/odds"
Brazil_SerieB_URL="https://www.oddsjet.com/en-ca/brazil/serie-b/odds"
Brazil_CopadoBrasil_URL="https://www.oddsjet.com/en-ca/copa-do-brasil/odds"
Chile_Primera_URL="https://www.oddsjet.com/en-ca/chile/primera/odds"
China_SuperLeague_URL="https://www.oddsjet.com/en-ca/china/super-league/odds"
Colombia_PrimeraA_URL="https://www.oddsjet.com/en-ca/colombia/primera-a/odds"
CopaLibertadores_URL="https://www.oddsjet.com/en-ca/copa-libertadores/odds"
#CopaLibertadores_Outright_URL="https://www.oddsjet.com/en-ca/copa-libertadores/outright-winner/odds"
Croatia_1_HNL_URL="https://www.oddsjet.com/en-ca/croatia/first-league/odds"
Czech_FirstLeague_URL="https://www.oddsjet.com/en-ca/czech/first-league/odds"
Denmark_Superliga_URL="https://www.oddsjet.com/en-ca/denmark/superliga/odds"
#Denmark_Superliga_OutrightWinner_URL="https://www.oddsjet.com/en-ca/denmark/superliga/outright-winner/odds"
Denmark_Division1_URL="https://www.oddsjet.com/en-ca/denmark/1st-division/odds"
Denmark_DBUCup_URL="https://www.oddsjet.com/en-ca/denmark/cup/odds"
Ecuador_SerieA_URL="https://www.oddsjet.com/en-ca/ecuador/serie-a/odds"
England_PremierLeague_URL="https://www.oddsjet.com/en-ca/england/premier-league/odds"
#England_PremierLeague_OutrightWinner_URL="https://www.oddsjet.com/en-ca/england/premier-league/outright-winner/odds"
England_Championship_URL="https://www.oddsjet.com/en-ca/england/championship/odds"
#England_Championship_OutrightWinner_URL="https://www.oddsjet.com/en-ca/england/championship/outright-winner/odds"
England_League1_URL="https://www.oddsjet.com/en-ca/england/league-1/odds"
England_League2_URL="https://www.oddsjet.com/en-ca/england/league-2/odds"
England_FACup_URL="https://www.oddsjet.com/en-ca/england/fa-cup/odds"
#England_FACup_OutrightWinner_URL="https://www.oddsjet.com/en-ca/england/fa-cup/outright-winner/odds"
England_EFLCup_URL="https://www.oddsjet.com/en-ca/england/league-cup/odds"
England_NationalLeague_URL="https://www.oddsjet.com/en-ca/england/national-league/odds"
England_NationalLeagueNorth_URL="https://www.oddsjet.com/en-ca/england/national-league-north/odds"
England_NationalLeagueSouth_URL="https://www.oddsjet.com/en-ca/england/national-league-south/odds"
Estonia_Meistriliiga_URL="https://www.oddsjet.com/en-ca/estonia/meistriliiga/odds"
Finland_Veikkausliiga_URL="https://www.oddsjet.com/en-ca/finland/veikkausliiga/odds"
#Finland_Veikkausliiga_OutrightWinner_URL="https://www.oddsjet.com/en-ca/finland/veikkausliiga/outright-winner/odds"
Finland_SuomenCup_URL="https://www.oddsjet.com/en-ca/finland/cup/odds"
France_Ligue1_URL="https://www.oddsjet.com/en-ca/france/ligue-1/odds"
#France_Ligue1_OutrightWinner_URL="https://www.oddsjet.com/en-ca/france/ligue-1/outright-winner/odds"
France_Ligue2_URL="https://www.oddsjet.com/en-ca/france/ligue-2/odds"
France_CoupedeFrance_URL="https://www.oddsjet.com/en-ca/coupe-de-france/odds"
France_LeagueCup_URL="https://www.oddsjet.com/en-ca/france/league-cup/odds"
Germany_Bundesliga_URL="https://www.oddsjet.com/en-ca/germany/bundesliga/odds"
#Germany_Bundesliga_OutrightWinner_URL="https://www.oddsjet.com/en-ca/germany/bundesliga/outright-winner/odds"
Germany_2_Bundesliga_URL="https://www.oddsjet.com/en-ca/germany/bundesliga-2/odds"
Germany_3_Liga_URL="https://www.oddsjet.com/en-ca/germany/3-liga/odds"
Germany_DFBPokal_URL="https://www.oddsjet.com/en-ca/germany/dfb-pokal/odds"
Greece_SuperLeague_URL="https://www.oddsjet.com/en-ca/greece/super-league/odds"
#Greece_SuperLeague_OutrightWinner_URL="https://www.oddsjet.com/en-ca/greece/super-league/outright-winner/odds"
Honduras_LigaNacional_URL="https://www.oddsjet.com/en-ca/honduras/liga-nacional/odds"
Hungary_NBI_URL="https://www.oddsjet.com/en-ca/hungary/nb-1/odds"
Iceland_PremierLeague_URL="https://www.oddsjet.com/en-ca/iceland/premier-league/odds"
India_SuperLeague_URL="https://www.oddsjet.com/en-ca/india/super-league/odds"
Ireland_PremierDivision_URL="https://www.oddsjet.com/en-ca/ireland/premier-division/odds"
Ireland_FirstDivision_URL="https://www.oddsjet.com/en-ca/ireland/first-division/odds"
Ireland_FAICup_URL="https://www.oddsjet.com/en-ca/ireland/fai-cup/odds"
Israel_PremierLeague_URL="https://www.oddsjet.com/en-ca/israel/premier-league/odds"
Italy_SerieA_URL="https://www.oddsjet.com/en-ca/italy/serie-a/odds"
#Italy_SerieA_OutrightWinner_URL="https://www.oddsjet.com/en-ca/italy/serie-a/outright-winner/odds"
Italy_SerieB_URL="https://www.oddsjet.com/en-ca/italy/serie-b/odds"
Italy_CoppaItalia_URL="https://www.oddsjet.com/en-ca/coppa-italia/odds"
Japan_J_League_URL="https://www.oddsjet.com/en-ca/japan/j-league/odds"
Kazakhstan_PremierLeague_URL="https://www.oddsjet.com/en-ca/kazakhstan/premier-league/odds"
Lithuania_ALyga_URL="https://www.oddsjet.com/en-ca/lithuania/a-lyga/odds"
Luxembourg_DivisionNationale_URL="https://www.oddsjet.com/en-ca/luxembourg/division-nationale/odds"
Malaysia_SuperLeague_URL="https://www.oddsjet.com/en-ca/malaysia/super-league/odds"
Mexico_Primera_LigaMX_URL="https://www.oddsjet.com/en-ca/mexico/liga-mx/odds"
#Mexico_LigaMX_OutrightWinner_URL="https://www.oddsjet.com/en-ca/mexico/liga-mx/outright-winner/odds"
Mexico_LigadeAscenso_URL="https://www.oddsjet.com/en-ca/mexico/ascenso/odds"
Mexico_Cup_CopaMX_URL="https://www.oddsjet.com/en-ca/mexico/cup/odds"
Netherlands_Eredivisie_URL="https://www.oddsjet.com/en-ca/netherlands/eredivisie/odds"
#Netherlands_Eredivisie_OutrightWinner_URL="https://www.oddsjet.com/en-ca/netherlands/eredivisie/outright-winner/odds"
Netherlands_KNVBCup_URL="https://www.oddsjet.com/en-ca/netherlands/knvb-cup/odds"
NewZealand_Premiership_URL="https://www.oddsjet.com/en-ca/new-zealand/premiership/odds"
NorthernIreland_Premier_URL="https://www.oddsjet.com/en-ca/northern-ireland/nifl-premiership/odds"
NorthernIreland_Cup_URL="https://www.oddsjet.com/en-ca/northern-ireland/cup/odds"
Norway_Eliteserien_URL="https://www.oddsjet.com/en-ca/norway/tippeligaen/odds"
#Norway_Eliteserien_OutrightWinner_URL="https://www.oddsjet.com/en-ca/norway/tippeligaen/outright-winner/odds"
Norway_Division1_URL="https://www.oddsjet.com/en-ca/norway/1st-division/odds"
Norway_Cup_URL="https://www.oddsjet.com/en-ca/norway/cup/odds"
Panama_LPF_URL="https://www.oddsjet.com/en-ca/panama/lpf/odds"
Paraguay_DivisiónProfesional_URL="https://www.oddsjet.com/en-ca/paraguay/primera-division/odds"
Peru_PrimeraDivisión_URL="https://www.oddsjet.com/en-ca/peru/primera-division/odds"
Poland_Ekstraklasa_URL="https://www.oddsjet.com/en-ca/poland/ekstraklasa/odds"
#Poland_Ekstraklasa_OutrightWinner_URL="https://www.oddsjet.com/en-ca/poland/ekstraklasa/outright-winner/odds"
Poland_ILiga_URL="https://www.oddsjet.com/en-ca/poland/i-liga/odds"
Poland_Cup_URL="https://www.oddsjet.com/en-ca/poland/cup/odds"
Portugal_PrimeiraLiga_URL="https://www.oddsjet.com/en-ca/portugal/primeira-liga/odds"
#Portugal_PrimeiraLiga_OutrightWinner_URL="https://www.oddsjet.com/en-ca/portugal/primeira-liga/outright-winner/odds"
Russia_PremierLeague_URL="https://www.oddsjet.com/en-ca/russia/premier-league/odds"
#Russia_PremierLeague_OutrightWinner_URL="https://www.oddsjet.com/en-ca/russia/premier-league/outright-winner/odds"
Russia_Cup_URL="https://www.oddsjet.com/en-ca/russia/cup/odds"
Scotland_Premiership_URL="https://www.oddsjet.com/en-ca/scotland/premiership/odds"
#Scotland_Premiership_OutrightWinner_URL="https://www.oddsjet.com/en-ca/scotland/premiership/outright/odds"
Scotland_Championship_URL="https://www.oddsjet.com/en-ca/scotland/championship/odds"
Scotland_League1_URL="https://www.oddsjet.com/en-ca/scotland/league-1/odds"
Scotland_League2_URL="https://www.oddsjet.com/en-ca/scotland/league-2/odds"
Scotland_FACup_URL="https://www.oddsjet.com/en-ca/scotland/fa-cup/odds"
Scotland_LeagueCup_URL="https://www.oddsjet.com/en-ca/scotland/league-cup/odds"
Serbia_SuperLiga_URL="https://www.oddsjet.com/en-ca/serbia/super-liga/odds"
Singapore_SLeague_URL="https://www.oddsjet.com/en-ca/singapore/s-league/odds"
Slovakia_SuperLiga_URL="https://www.oddsjet.com/en-ca/slovakia/super-liga/odds"
Slovenia_PrvaLiga_URL="https://www.oddsjet.com/en-ca/slovenia/prva-liga/odds"
SouthAfrica_PremierSoccerLeague_URL="https://www.oddsjet.com/en-ca/south-africa/premiership/odds"
SouthKorea_K_LeagueClassic_URL="https://www.oddsjet.com/en-ca/south-korea/k-league/odds"
Spain_LaLiga_URL="https://www.oddsjet.com/en-ca/spain/laliga/odds"
#Spain_LaLiga_OutrightWinner_URL="https://www.oddsjet.com/en-ca/spain/laliga/outright-winner/odds"
Spain_Segunda_URL="https://www.oddsjet.com/en-ca/spain/segunda-division/odds"
Spain_CopadelRey_URL="https://www.oddsjet.com/en-ca/spain/copa-del-rey/odds"
Sweden_Allsvenskan_URL="https://www.oddsjet.com/en-ca/sweden/allsvenskan/odds"
#Sweden_Allsvenskan_OutrightWinner_URL="https://www.oddsjet.com/en-ca/sweden/allsvenskan/outright-winner/odds"
Sweden_Superettan_URL="https://www.oddsjet.com/en-ca/sweden/superettan/odds"
Sweden_Cup_URL="https://www.oddsjet.com/en-ca/sweden/svenska-cupen/odds"
Switzerland_SuperLeague_URL="https://www.oddsjet.com/en-ca/switzerland/super-league/odds"
#Switzerland_SuperLeague_OutrightWinner_URL="https://www.oddsjet.com/en-ca/switzerland/super-league/outright/odds"
Switzerland_SwissCup_URL="https://www.oddsjet.com/en-ca/switzerland/cup/odds"
Turkey_SuperLig_URL="https://www.oddsjet.com/en-ca/turkey/super-lig/odds"
#Turkey_SuperLig_OutrightWinner_URL="https://www.oddsjet.com/en-ca/turkey/super-lig/outright-winner/odds"
Turkey_Cup_URL="https://www.oddsjet.com/en-ca/turkey/cup/odds"
Ukraine_PremierLeague_URL="https://www.oddsjet.com/en-ca/ukraine/premier-league/odds"
Uruguay_PrimeraDivisión_URL="https://www.oddsjet.com/en-ca/uruguay/primera-division/odds"
Venezuela_PrimeraDivisión_URL="https://www.oddsjet.com/en-ca/venezuela/primera-division/odds"
Wales_PremierLeague_URL="https://www.oddsjet.com/en-ca/wales/premier-league/odds"

def getSoccerUrls():
    return [
        InternationalMatches_URL,
        MLS_URL,
        CanadaPremierLeague_URL,
        ChampionsLeague_URL,
        EuropaLeague_URL,
        EuropaConferenceLeague_URL,
        Argentina_PrimeraDivisión_URL,
        Argentina_Cup_URL,
        Australia_A_League_URL,
        Australia_FFACup_URL,
        Austria_Bundesliga_URL,
        Austria_ÖFBCup_URL,
        Azerbaijan_PremierLeague_URL,
        Belgium_ProLeague_URL,
        Belgium_Division2_URL,
        Belgium_Cup_URL,
        Bolivia_ProfessionalLeague_URL,
        Brazil_SerieA_URL,
        Brazil_SerieB_URL,
        Brazil_CopadoBrasil_URL,
        Chile_Primera_URL,
        China_SuperLeague_URL,
        Colombia_PrimeraA_URL,
        CopaLibertadores_URL,
        Croatia_1_HNL_URL,
        Czech_FirstLeague_URL,
        Denmark_Superliga_URL,
        Denmark_Division1_URL,
        Denmark_DBUCup_URL,
        Ecuador_SerieA_URL,
        England_PremierLeague_URL,
        England_Championship_URL,
        England_League1_URL,
        England_League2_URL,
        England_FACup_URL,
        England_EFLCup_URL,
        England_NationalLeague_URL,
        England_NationalLeagueNorth_URL,
        England_NationalLeagueSouth_URL,
        Estonia_Meistriliiga_URL,
        Finland_Veikkausliiga_URL,
        Finland_SuomenCup_URL,
        France_Ligue1_URL,
        France_Ligue2_URL,
        France_CoupedeFrance_URL,
        France_LeagueCup_URL,
        Germany_Bundesliga_URL,
        Germany_2_Bundesliga_URL,
        Germany_3_Liga_URL,
        Germany_DFBPokal_URL,
        Greece_SuperLeague_URL,
        Honduras_LigaNacional_URL,
        Hungary_NBI_URL,
        Iceland_PremierLeague_URL,
        India_SuperLeague_URL,
        Ireland_PremierDivision_URL,
        Ireland_FirstDivision_URL,
        Ireland_FAICup_URL,
        Israel_PremierLeague_URL,
        Italy_SerieA_URL,
        Italy_SerieB_URL,
        Italy_CoppaItalia_URL,
        Japan_J_League_URL,
        Kazakhstan_PremierLeague_URL,
        Lithuania_ALyga_URL,
        Luxembourg_DivisionNationale_URL,
        Malaysia_SuperLeague_URL,
        Mexico_Primera_LigaMX_URL,
        Mexico_LigadeAscenso_URL,
        Netherlands_Eredivisie_URL,
        Netherlands_KNVBCup_URL,
        NewZealand_Premiership_URL,
        NorthernIreland_Premier_URL,
        NorthernIreland_Cup_URL,
        Norway_Eliteserien_URL,
        Norway_Division1_URL,
        Norway_Cup_URL,
        Panama_LPF_URL,
        Paraguay_DivisiónProfesional_URL,
        Peru_PrimeraDivisión_URL,
        Poland_Ekstraklasa_URL,
        Poland_ILiga_URL,
        Poland_Cup_URL,
        Portugal_PrimeiraLiga_URL,
        Russia_PremierLeague_URL,
        Russia_Cup_URL,
        Scotland_Premiership_URL,
        Scotland_Championship_URL,
        Scotland_League1_URL,
        Scotland_League2_URL,
        Scotland_FACup_URL,
        Scotland_LeagueCup_URL,
        Serbia_SuperLiga_URL,
        Singapore_SLeague_URL,
        Slovakia_SuperLiga_URL,
        Slovenia_PrvaLiga_URL,
        SouthAfrica_PremierSoccerLeague_URL,
        SouthKorea_K_LeagueClassic_URL,
        Spain_LaLiga_URL,
        Spain_Segunda_URL,
        Spain_CopadelRey_URL,
        Sweden_Allsvenskan_URL,
        Sweden_Superettan_URL,
        Sweden_Cup_URL,
        Switzerland_SuperLeague_URL,
        Switzerland_SwissCup_URL,
        Turkey_SuperLig_URL,
        Turkey_Cup_URL,
        Ukraine_PremierLeague_URL,
        Uruguay_PrimeraDivisión_URL,
        Venezuela_PrimeraDivisión_URL,
        Wales_PremierLeague_URL]