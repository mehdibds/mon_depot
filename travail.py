# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import *
from tools import *

"""class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        return SoccerAction(Vector2D.create_random(-1,1),
                            Vector2D.create_random(-1,1))"""

class Fonceur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "RandomAtt")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s=SuperState(state, id_team, id_player)
        balle = state.ball.position
        joueur = state.player_state (id_team ,id_player).position
        but = s.goal
        
        if (joueur.distance(balle) < PLAYER_RADIUS + BALL_RADIUS):
            return SoccerAction(shoot=((but-joueur)/20)*maxPlayerShoot)
        else:
            return SoccerAction((balle-joueur)*maxPlayerAcceleration)
         
class Defenseur(Strategy):
    """def __init__(self):
        Strategy.__init__(self, "RandomDef")"""

    """def defenseur_strategy(self, state, id_team, id_player):"""
    
        
        
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Joueur1", Strategy())  # Random strategy
team2.add("Joueur2", Fonceur()) #Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
