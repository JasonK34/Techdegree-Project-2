#TechDegree Project 2 - Basketball Stats tool

from constants import TEAMS
from constants import PLAYERS
import copy

the_players = copy.deepcopy(PLAYERS)

print("\nWelcome to Basketball Stats!")

def clean_data():
    #the_players = copy.deepcopy(PLAYERS)
    print(the_players)

def balance_teams():
    the_teams = copy.deepcopy(TEAMS)
    print(the_teams)

def stat_tool():
    initial_entry = int(input("\nPlease enter '1' for stats, and '2' to exit: \n"))
    if initial_entry == 1:
        clean_data()
        balance_teams()
        
    

    




if __name__ == "__main__":
    stat_tool()


