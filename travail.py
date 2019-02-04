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

class Attaquant(Strategy):
    def __init__(self):
        Strategy.__init__(self, "RandomAtt")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s = SuperState(state, id_team, id_player)
        return s.shoot 
         
class Defenseur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "RandomDef")

    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state,id_team,id_player)
        #joueur 3 de l'équipe 1
        if s.id_team == 1 and s.id_player == 1:
            #si la balle se trouve dans le côté supérieur gauche
            if (s.ball.x < GAME_WIDTH/2) :
                return s.shoot
            else :
                return s.etat(GAME_WIDTH/4, GAME_HEIGHT/2)
        #joueur 3 de l'équipe 2
        if s.id_team == 2 and s.id_player == 1 :
            #si la balle se trouve dans le côté supérieur droit
            if (s.ball.x > GAME_WIDTH/2) :
               return s.shoot
            else :
                return s.etat(3*GAME_WIDTH/4, GAME_HEIGHT/2)
        #joueur 4 de l'équipe 2

# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Mbappe", Attaquant())
team1.add("Kimpembe", Defenseur())


  # Random strategy
team2.add("Dembele", Attaquant())
team2.add("Mendy", Defenseur())
 #Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
