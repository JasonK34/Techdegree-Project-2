#TechDegree Project 2 - Basketball Stats tool

from constants import TEAMS
from constants import PLAYERS
import copy

the_players = copy.deepcopy(PLAYERS)
the_teams = copy.deepcopy(TEAMS)

print("\nWelcome to Basketball Stats!")

def clean_data():
    #print(the_players)
    print(len(the_players))

def balance_teams():
    panthers = the_teams[0]
    panthers_players = []
    panthers_players.append(the_players[0:6])

    bandits = the_teams[1] 
    bandits_players = []
    bandits_players.append(the_players[6:13])

    warriors = the_teams[2]
    warriors_players = []
    warriors_players.append(the_players[13:])

    print(the_teams)
    print(panthers, bandits, warriors)
    print(f"Your Panthers are: {panthers_players}, \n\nYour Bandits are: {bandits_players}, \n\nYour Warriors are: {warriors_players}")

def stat_tool():
    initial_entry = int(input("\nPlease enter '1' for stats, and '2' to exit: \n"))
    if initial_entry == 1:
        clean_data()
        balance_teams()
        
    

if __name__ == "__main__":
    stat_tool()


