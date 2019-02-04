# coding: utf-8
from soccersimulator import Vector2D, MobileMixin , SoccerAction
from soccersimulator.settings import *
"""class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        return SoccerAction(Vector2D.create_random(-1,1),
                            Vector2D.create_random(-1,1))"""

class SuperState():
    def __init__(self,state,id_team,id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player
        
    @property
    def ball(self):
        return self.state.ball.position
    
    @property
    def player(self):
        return self.state.player_state(self.id_team,self.id_player).position
    
    @property
    def goal(self):
        if (self.id_team==1):
            return Vector2D(GAME_WIDTH,GAME_HEIGHT /2)
        else :
            return Vector2D(0, GAME_HEIGHT/2)
    
    @property
    def go(self):
            return SoccerAction(self.ball -self.player)
    
    @property    
    def shoot(self):
        if (self.player.distance(self.ball) < PLAYER_RADIUS + BALL_RADIUS):
            return SoccerAction(shoot=((self.goal-self.player)/20)*maxPlayerShoot)
        else:
            return SoccerAction((self.ball-self.player)*maxPlayerAcceleration)
    
    def etat(self, x, y):
        pos = Vector2D(x,y)
        return SoccerAction(pos-self.player)
        
    @property
    def advproche(self):
        mini=GAME_WIDTH
        
        for el in self.state.players :
            equipe = el[0]
            joueur = el[1]
            if equipe != self.id_team :
                if (self.player.distance(self.state.player_state(equipe,joueur).position)<mini):
                    mini = self.player.distance(self.state.player_state(equipe,joueur).position)
                    adverse = joueur
        return adverse
    
    @property
    def eqproche(self):
        mini=GAME_WIDTH
        
        for el in self.state.players :
            equipe = el[0]
            joueur = el[1]
            if equipe == self.id_team :
                if (self.player.distance(self.state.player_state(equipe,joueur).position)<mini):
                    mini = self.player.distance(self.state.player_state(equipe,joueur).position)
                    equipier = joueur
        return equipier
    
    @property
    def tirer(self):
        return SoccerAction(shoot=(self.goal - self.ball).normalize()*maxPlayerShoot)
    
    def foncer_but(self):
        return SoccerAction(shoot=(self.goal - self.ball).normalize())
    
    