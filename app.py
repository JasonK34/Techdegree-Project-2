#TechDegree Project 2 - Basketball Stats tool

from constants import TEAMS
from constants import PLAYERS
import copy


def clean_data():

    new_teams_copy = copy.deepcopy(TEAMS)
    print(new_teams_copy)    
    
    new_teams_copy.append("Bears")
    print(new_teams_copy)




if __name__ == "__main__":
    clean_data()


