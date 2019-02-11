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
        Strategy.__init__(self, "Attaquant")
        
        
    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s = SuperState(state, id_team, id_player)
        return s.shoot
        
class Dribbler (Strategy):
    def __init__(self):
        Strategy.__init__(self, "Dribbler")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        if (s.player_adverse.distance(s.player) < 50):    
            if (s.ball.distance(s.player) < PLAYER_RADIUS+BALL_RADIUS):
                return SoccerAction(Vector2D(-GAME_WIDTH/2,GAME_GOAL_HEIGHT),Vector2D(-GAME_WIDTH/2,GAME_GOAL_HEIGHT))
            if (s.ball.x < 3*GAME_WIDTH/4):
                return SoccerAction(Vector2D(GAME_WIDTH,GAME_HEIGHT/2)-s.ball/GAME_WIDTH)
            return SoccerAction(Vector2D(GAME_WIDTH,GAME_HEIGHT/2))
        return s.shoot
       
        
    """-s.ball/(GAME_WIDTH/2)"""
class Defenseur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defenseur")

    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state,id_team,id_player)
        if s.id_team == 1 and s.id_player == 1:
            #si la balle se trouve dans le côté gauche
            if (s.ball.x < GAME_WIDTH/2) :
                return s.shoot
            else :
                return s.go_to_position(GAME_WIDTH/8, GAME_HEIGHT/2)
        if s.id_team == 2 and s.id_player == 1 :
            #si la balle se trouve dans le côté droit
            if (s.ball.x > GAME_WIDTH/2) :
               return s.shoot
            else :
                return s.go_to_position(7*GAME_WIDTH/8, GAME_HEIGHT/2)
        

