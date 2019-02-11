# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Mbappe", Attaquant())
team1.add("Kimpembe", Defenseur())
team1.add("Angel Di Maria",Attaquant())

  # Random strategy
team2.add("Dembele", Attaquant())
team2.add("Mendy", Defenseur())
 #Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
