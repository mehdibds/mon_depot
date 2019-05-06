from octogone.tools import *
from octogone.strategies import *


# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Papa", Attaquant())
team1.add("Moncef", Attaquant())
team1.add("Lyna", Defenseur())
team1.add("Hisoka", Defenseur())
team2.add("Maman", Attaquant())
team2.add("Nermine", Attaquant())
team2.add("Lola",Defenseur())
team2.add("Nami", Defenseur())


# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)

