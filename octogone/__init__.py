from octogone.strategies import Shoot, Shoot_Anticipe, Dribbler, Defenseur
from soccersimulator import SoccerTeam

def get_team(nb_players):
    team = SoccerTeam(name="Lyna et Mehdi")
    if nb_players == 1:
        team.add("Attaquant", Shoot())
    if nb_players == 2 :
        team.add("Attaquant",Shoot_Anticipe())
        team.add("Defenseur",Defenseur())
    return team
    
