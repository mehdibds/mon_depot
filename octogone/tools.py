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

    #distance au goal
    @property
    def distance_goal(self):
        return self.goal.distance(self.player)
    
    	#aller à un point donné
    def go_to_position(self, x, y):
        pos = Vector2D(x,y)
        return SoccerAction(pos-self.player)
    
    #retourne vrai si le joueur peut shoot, faux sinon
    @property
    def can_shoot(self):
        return self.ball.distance(self.player) < PLAYER_RADIUS+BALL_RADIUS
    
    #aller vers la balle
    @property
    def go (self):
        return SoccerAction((self.ball-self.player)*maxPlayerAcceleration)   

    #shooter dans la baller
    @property
    def shoot(self):
        return SoccerAction(shoot=((self.goal-self.player)/20)*maxPlayerShoot)
    
	#shooter dans la balle ou aller vers la balle
    @property    
    def shoot_or_go(self):
        if (self.can_shoot):
            return self.shoot
        else:
            return self.go 
        
      
      #anticiper la position de la balle
    @property
    def ball_anticipe(self):
        return self.state.ball.position+self.player.distance(self.ball)*self.state.ball.vitesse
    
    #aller vers la position anticipée de la balle
    @property
    def go_anticipe (self):
        return SoccerAction((self.ball_anticipe-self.player)*maxPlayerAcceleration) 
    
    #shooter dans la balle ou aller vers la position anticipée de la balle
    @property    
    def shoot_or_go_anticipe(self):
        if (self.can_shoot):
            return self.shoot
        else:
            return self.go_anticipe
    
    
    
    
    
    
    
    
    
    
    #position du joueur adverse (???)
    @property
    def player_adverse(self):
        if (self.id_team == 1):
            return self.state.player_state(2,self.id_player).position
        if (self.id_team == 2):
            return self.state.player_state(1,self.id_player).position
 

    
     #liste des adversaires
    @property
    def liste_adv(self):
        return [self.state.player_state(id_team, id_team).position for (id_team, id_player) in self.state.players if id_team != self.id_team]
    
    #position de l'adversaire le plus proche    
    @property
    def adv_proche(self):
        adversaire = self.liste_adv
        mini = min ([(self.player.distance(player), player) for player in adversaire])
        return mini[1]
    
	#liste des equipiers
    @property
    def liste_eq(self):
        return [self.state.player_state(id_team, id_team).position for (id_team, id_player) in self.state.players if id_team == self.id_team]
    
    #position de l'equipier le plus proche
    @property
    def eq_proche(self):
        equipier = self.liste_eq
        mini = min([(self.player.distance(player),player) for player in equipier])
        return mini[1]
    
    
    #distance de l'équipier le plus proche à la balle
    @property
    def distance_eq_ball(self):
        equipier = self.liste_eq
        return min ([(player.distance(self.ball), player) for player in equipier])
    
     #distance de l'adversaire le plus proche à la balle
    @property
    def distance_adv_ball(self):
        adversaire = self.liste_adv
        return min ([(player.distance(self.ball), player) for player in adversaire])
    
	#faire la passe à l'équipier le plus proche
    @property
    def passe(self):
        if (self.can_shoot):
            return SoccerAction(shoot=((self.eq_proche-self.player)/20)*maxPlayerShoot)
        else:
            return SoccerAction((self.ball-self.player)*maxPlayerAcceleration)
       

    


    
	
