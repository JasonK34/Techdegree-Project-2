#TechDegree Project 2 - Basketball Stats tool

from constants import TEAMS
from constants import PLAYERS
import copy
import random

#my copies of the original files
players_copy = copy.deepcopy(PLAYERS)
teams_copy = copy.deepcopy(TEAMS)

#new copy of the entire player list
players_list = []

#files of the list of players on each team
panthers = teams_copy[0]
panthers_players = []

bandits = teams_copy[1] 
bandits_players = []

warriors = teams_copy[2]
warriors_players = []

print("\nWelcome to Basketball Stats!")


def clean_data():
    
    for player in players_copy:
        for key, value in player.items():
            if key == "name":
                players_list.append(value)
            if key == "height":
                num_inches = value.split(" ")
                num = int(num_inches[0])
                #print (num)

def balance_teams():

    panthers_players.append(random.sample(players_list, k=6))
    bandits_players.append(random.sample(players_list, k=6))
    warriors_players.append(random.sample(players_list, k=6))
    
    #print(len(players_copy))
    #panthers_players.append(players_copy[0:6])
    #bandits_players.append(players_copy[6:13])
    #warriors_players.append(players_copy[13:])

   
def stat_tool():
    
    clean_data()
    balance_teams()
    initial_entry = int(input("\nPlease enter '1' for stats, and '2' to exit: \n"))
    while initial_entry == 1:
        select_team = int(input("\nSelect team (enter numer): (1) Panthers, (2) Bandits, (3) Warriors: \n"))
        if select_team == 1:
            print("\nPanthers:", panthers_players) 
        if select_team == 2:
            print("\nBandits: ", bandits_players)
        if select_team == 3:
            print("\nWarriors: ", warriors_players)
    

if __name__ == "__main__":
    stat_tool()


