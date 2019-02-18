from dulmo.tools import *
from dulmo.strategies import *

# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Mbappe", Attaquant_Anticipe())
team1.add("Kimpembe", Defenseur())


  # Random strategy
team2.add("Dembele", Attaquant())
team2.add("Mendy", Defenseur())
 #Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
