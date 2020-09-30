#TechDegree Project 2 - Basketball Stats tool

from constants import TEAMS
from constants import PLAYERS
import copy

players_copy = copy.deepcopy(PLAYERS)
teams_copy = copy.deepcopy(TEAMS)


panthers = teams_copy[0]
panthers_players = []

bandits = teams_copy[1] 
bandits_players = []

warriors = teams_copy[2]
warriors_players = []

print("\nWelcome to Basketball Stats!")


def clean_data():
    print(len(players_copy))


def balance_teams():

    panthers_players.append(players_copy[0:6])
    bandits_players.append(players_copy[6:13])
    warriors_players.append(players_copy[13:])

   
def stat_tool():
    balance_teams()
    initial_entry = int(input("\nPlease enter '1' for stats, and '2' to exit: \n"))
    if initial_entry == 1:
        select_team = int(input("Select team (enter numer): (1) Panthers, (2) Bandits, (3) Warriors: \n"))
        if select_team == 1:
            #balance_teams()
            print(panthers, ": ", panthers_players) 
        if select_team == 2:
            #balance_teams()
            print(bandits, ": ", bandits_players)
        if select_team == 3:
            #balance_teams()
            print(warriors, ": ", warriors_players)
    

if __name__ == "__main__":
    stat_tool()


