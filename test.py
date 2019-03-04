from octogone.tools import *
from octogone.strategies import *

# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Mbappe", Shoot_Anticipe())
team1.add("Dembele", Shoot_Anticipe())
team1.add("Varane", Defenseur())
team1.add("Umtiti", Defenseur())

  # Random strategy
team2.add("Kane", Shoot_Anticipe())
team2.add("Sterling", Shoot_Anticipe())
team2.add("Stones", Defenseur())
team2.add("Rose", Defenseur())
 #Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
