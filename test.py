from octogone.tools import *
from octogone.strategies import *

# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Mbappe", Shoot())
team1.add("Kimpembe", Defenseur())


  # Random strategy
team2.add("Dembele", Shoot_Anticipe())
team2.add("Mendy", Defenseur())
 #Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
