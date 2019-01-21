# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import *

"""class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        return SoccerAction(Vector2D.create_random(-1,1),
                            Vector2D.create_random(-1,1))"""

class Test(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        balle = state.ball.position
        joueur = state.player_state (id_team ,id_player).position
        but = Vector2D(GAME_WIDTH,GAME_HEIGHT /2)
        
        if (joueur.distance(balle) < PLAYER_RADIUS + BALL_RADIUS):
            return SoccerAction(shoot=(but-joueur)/20)
        else:
            return SoccerAction(balle-joueur)

# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Random", Test())  # Random strategy
team2.add("Static", Strategy())   # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
