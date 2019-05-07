# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import *
from .tools import *



"""class Fonceur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Shoot")
        
    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s = SuperState(state, id_team, id_player)
        if s.player.distance(s.ball)<PLAYER_RADIUS+BALL_RADIUS :
            return SoccerAction(shoot = s.goal-s.player)
        else :
            return SoccerAction(acceleration=s.ball-s.player)"""
        
class FonceurAnticipe(Strategy):
    def __init__(self):
        Strategy.__init__(self, "FonceurAnticipe")
        
    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s = SuperState(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        return move.to_ball_anticipe() + shoot.to_goal()

class Fonceur (Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")
        
    def compute_strategy(self, state, id_team, id_player):
        #id_team is 1 or 2
        #id_player starts at 0
        s = SuperState(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        #if s.ball.x != GAME_WIDTH/2 and s.ball.y != GAME_HEIGHT/2 :
        return move.to_ball()+shoot.to_goal()



"""class Fonceur_Intelligent(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
        
    def compute_strategy(self,state,id_team,id_player):
        s=SuperState(state, id_team, id_player)
        move = Move(s)
        if ((s.ball - s.player).norm < 50) :
            if ((s.ball - s.player).norm < PLAYER_RADIUS + BALL_RADIUS):
                if (id_team == 1):
                    if((state.player_state(2,id_player).position - s.player).norm < 50):
                        return SoccerAction(Vector2D(-75,10),Vector2D(-75,10))
                    if (s.ball.x > 112):
                        return SoccerAction(s.ball - s.player ,(Vector2D(150,45) - s.ball)/8)
                    return SoccerAction(0,(Vector2D(150,45) - s.ball)/75)
                if (id_team == 2):
                    if (s.ball.position.x < 37):
                        return SoccerAction(s.ball - s.player ,(Vector2D(0,45) - s.ball)/8)
                    return SoccerAction(0,(Vector2D(0,45) - s.ball)/75)
            else:
                return move.to_ball()
        else:
            return SoccerAction(0,0)"""
    
class Attaquant(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        if (s.zone_tir == True):
            return move.to_ball()+shoot.to_goal()
        else :
            if s.passe_possible == True :
                return move.to_ball()+shoot.passe()
            else :
                if (s.id_player == 0):
                    return move.to_ball()+shoot.dribble()
                if (s.id_player == 1):
                    if (s.player.distance(s.ball)<s.equipier_proche.distance(s.ball)):
                        return move.to_ball()+shoot.to_goal()
                    return move.to_goal()

"""class Defenseur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defenseur")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        if (s.zone_tir == True):
            return move.to_ball()+shoot.to_goal()
        else :
            if s.passe_possible == True :
                return move.to_ball()+shoot.passe()
            else :
                
                return move.to_player()+shoot.to_goal()"""

class Defenseur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defenseur")

    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state,id_team,id_player)
        move = Move(s)
        shoot = Shoot(s)
        pos_x = GAME_WIDTH/15
        pos_y = GAME_HEIGHT/4
            #la balle se trouve dans le côté gauche en haut
        if s.id_team == 1 and s.id_player == 2:
            if (s.ball.x < GAME_WIDTH/2 and s.ball.y < GAME_HEIGHT/2) :
                return move.to_ball()+shoot.to_goal()
            else :
                return move.to_position(pos_x, pos_y)
            #la balle se trouve dans le côté gauche en bas
        if s.id_team == 1 and s.id_player == 3 :
            if (s.ball.x < GAME_WIDTH/2 and s.ball.y > GAME_HEIGHT/2) :
                return move.to_ball()+shoot.to_goal()
            else :
                return move.to_position(pos_x, 3*pos_y)
            #la balle se trouve dans le côté droit en haut
        if s.id_team == 2 and s.id_player == 2:
            if (s.ball.x > GAME_WIDTH/2 and s.ball.y < GAME_HEIGHT/2) :
                return move.to_ball()+shoot.to_goal()
            else :
                return move.to_position(14*pos_x, pos_y)
            #la balle se trouve dans le côté droit en bas
        if s.id_team == 2 and s.id_player == 3 :
            if (s.ball.x > GAME_WIDTH/2 and s.ball.y > GAME_HEIGHT/2) :
                return move.to_ball()+shoot.to_goal()
            else :
                return move.to_position(14*pos_x, 3*pos_y) 
                            
                            
                            


          
        
"""def gobetter(state) :
    if state.player.distance(state.ball)<PLAYER_RADIUS+BALL_RADIUS :
            return SoccerAction(shoot = state.goal-state.player)
    else :
            return SoccerAction(acceleration=state.ball-state.player)"""

            
        

            

 