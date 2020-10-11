#TechDegree Project 2 - Basketball Stats tool

from constants import TEAMS
from constants import PLAYERS
import copy


#my copies of the original files
players_copy = copy.deepcopy(PLAYERS)
teams_copy = copy.deepcopy(TEAMS)

#new list of all players
players_list = []
guardian_list = []

#each team's list of players
panthers_players = []
bandits_players = []
warriors_players = []

print("\nWelcome to Basketball Stats!\n")

def clean_data():
    
    for player in players_copy:
        for key, value in player.items():
            if key == "name":
                players_list.append(value)

            if key == "guardians":
                guardian_list.append(value)
            
            if key == "height":
                num_inches = value.split(" ")
                num = int(num_inches[0])
                #print (num)

            #if players_copy['experience'] = "YES":
               # YES = True
                


    balance_teams()
    
    
    initial_entry = int(input("\nPlease enter '1' for stats, and '2' to exit: \n"))
    while initial_entry == 1:
        select_team = int(input("\nSelect option below (enter numer):\n (1) PANTHERS roster\n (2) BANDITS roster\n (3) WARRIORS roster \n (4) ALL Players\n (5) All Guardians\n"))
        if select_team == 1:
            print("\nPANTHERS:")
            for panther in players_copy:
                print(panther)
                if select_team == 2:
            print("\nBANDITS: ")
            for bandit in bandits_players:
                print(bandit)
        if select_team == 3:
            print("\nWARRIORS: ")
            for warrior in warriors_players:
                print(warrior)
        if select_team == 4:
            print("\nALL players: \n")
            for player in players_list:
                print(player)
        if select_team == 5:
            print("\nGUARDIANS: \n")
            for guardian in guardian_list:
                print(guardian)    

def balance_teams():
    
    panthers_players.append(players_list[0:6])
    bandits_players.append(players_list[6:12])
    warriors_players.append(players_list[12:])

   


if __name__ == "__main__":
    clean_data()
    balance_teams()

