# coding: utf-8
from soccersimulator import Vector2D, MobileMixin , SoccerAction
from soccersimulator.settings import *

class SuperState():
    def __init__(self,state,id_team,id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player
   
	#positon de la balle     
    @property
    def ball(self):
        return self.state.ball.position
    
     #vitesse de la balle  
    @property
    def vitesse_ball(self):
        return self.state.ball.position
    
	#position du joueur
    @property
    def player(self):
        return self.state.player_state(self.id_team,self.id_player).position
    
	#position du goal
    @property
    def goal(self):
        if (self.id_team==1):
            return Vector2D(GAME_WIDTH,GAME_HEIGHT /2)
        else :
            return Vector2D(0, GAME_HEIGHT/2)
	#aller vers la balle
    @property
    def go(self):
            return SoccerAction(self.ball -self.player)
    
	#shooter dans la balle ou aller vers la balle
    @property    
    def shoot(self):
        if (self.player.distance(self.ball) < PLAYER_RADIUS + BALL_RADIUS):
            return SoccerAction(shoot=((self.goal-self.player)/20)*maxPlayerShoot)
        else:
            return SoccerAction((self.ball-self.player)*maxPlayerAcceleration)
    	
	#aller à un point donné
    def go_to_position(self, x, y):
        pos = Vector2D(x,y)
        return SoccerAction(pos-self.player)

	#trouver l'adversaire le plus proche        
    @property
    def adv_proche(self):
        mini=GAME_WIDTH
        for el in self.state.players :
            equipe = el[0]
            joueur = el[1]
            if equipe != self.id_team :
                if (self.player.distance(self.state.player_state(equipe,joueur).position)<mini):
                    mini = self.player.distance(self.state.player_state(equipe,joueur).position)
                    adverse = joueur
        return adverse
   
	#trouver l'équipier le plus proche
    @property
    def eq_proche(self):
        mini=GAME_WIDTH
        for el in self.state.players :
            equipe = el[0]
            joueur = el[1]
            if equipe == self.id_team :
                if (self.player.distance(self.state.player_state(equipe,joueur).position)<mini):
                    mini = self.player.distance(self.state.player_state(equipe,joueur).position)
                    equipier = self.state.player_state(equipe,joueur).position
        return equipier

	#faire la passe à l'équipier le plus proche
    @property
    def passe(self):
        return SoccerAction(shoot=((self.eq_proche-self.player)/20)*maxPlayerShoot)

    """@property
    def tirer(self):
        return SoccerAction(shoot=(self.goal - self.ball).normalize()*maxPlayerShoot)
    
    @property
    def foncer_but(self):
        return SoccerAction(shoot=(self.goal - self.ball).normalize())"""
    
    
	
