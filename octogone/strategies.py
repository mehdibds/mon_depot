# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import *
from .tools import *


class Shoot(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant")
        
    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s = SuperState(state, id_team, id_player)
        return s.shoot_or_go
   
class Attaquanttlp(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant")
        
    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s = SuperState(state, id_team, id_player)
        if (s.player.distance(s.goal) < s.player.distance(s.eq_proche)):
            return s.shoot_and_go
        else :
            return s.passe
    
    
class  Shoot_Anticipe(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant")
               
    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s = SuperState(state, id_team, id_player)
        return s.shoot_or_go_anticipe
  


      
class Dribbler (Strategy):
    def __init__(self):
        Strategy.__init__(self, "Dribbler")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        if (s.player_adverse.distance(s.player) < 20):    
            if (s.can_shoot):
                return SoccerAction(Vector2D(-GAME_WIDTH/2,GAME_GOAL_HEIGHT),Vector2D(-GAME_WIDTH/2,GAME_GOAL_HEIGHT))
            if (s.ball.x < 3*GAME_WIDTH/4):
                return SoccerAction(Vector2D(GAME_WIDTH,GAME_HEIGHT/2)-s.ball/GAME_WIDTH)
            return SoccerAction(Vector2D(GAME_WIDTH,GAME_HEIGHT/2))
        return s.shoot_or_go
       
        
  
    
class Defenseur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defenseur")

    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state,id_team,id_player)
        if s.id_team == 1 and s.id_player == 1:
            #si la balle se trouve dans le côté gauche
            if (s.ball.x < GAME_WIDTH/2) :
                return s.shoot_or_go
            else :
                return s.go_to_position(GAME_WIDTH/8, GAME_HEIGHT/2)
        if s.id_team == 2 and s.id_player == 1 :
            #si la balle se trouve dans le côté droit
            if (s.ball.x > GAME_WIDTH/2) :
               return s.shoot_or_go
            else :
                return s.go_to_position(7*GAME_WIDTH/8, GAME_HEIGHT/2)
        

