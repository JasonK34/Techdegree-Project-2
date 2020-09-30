#TechDegree Project 2 - Basketball Stats tool

from constants import TEAMS
from constants import PLAYERS
import copy

the_players = copy.deepcopy(PLAYERS)
the_teams = copy.deepcopy(TEAMS)


panthers = the_teams[0]
panthers_players = []

bandits = the_teams[1] 
bandits_players = []

warriors = the_teams[2]
warriors_players = []

print("\nWelcome to Basketball Stats!")


def clean_data():
    print(len(the_players))


def balance_teams():

    panthers_players.append(the_players[0:6])
    bandits_players.append(the_players[6:13])
    warriors_players.append(the_players[13:])

   
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


