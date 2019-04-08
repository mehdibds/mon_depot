# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_simu
from octogone.tools import *
from octogone.strategies import *

# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Attaquant1", Attaque())
team1.add("Defenseur1", DefenseurVolley())   
team2.add("Attaquant2", Attaque()) 
team2.add("Defenseur2", DefenseurVolley())   

# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)