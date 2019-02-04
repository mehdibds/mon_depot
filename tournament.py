#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tools import *
from travail import *

def get_team(nb_players):
    team = SoccerTeam(name="Lyna et Mehdi")
    if nb_player == 1:
        team.add("Attaquant", Fonceur())
    if nb_players == 2 :
        team.add("Attaquant",Fonceur())
        team.add("Defenseur",Defenseur())
        
        return team
    
if __name__ == '__main__':
    from soccersimulator import Simulation, show_simu
    
    #Check team with 1 player and 2 players
    team1=get_team(1)
    team2=get_team(2)
    
    #Create a match
    simu=Simulation(team1,team2)
    
    #simulate and display the match
    
