from dulmo.strategies import Attaquant, Attaquant_Anticipe, Dribbler, Defenseur
from soccersimulator import SoccerTeam

def get_team(nb_players):
    team = SoccerTeam(name="Lyna et Mehdi")
    if nb_players == 1:
        team.add("Attaquant", Attaquant())
    if nb_players == 2 :
        team.add("Attaquant",Attaquant_Anticipe())
        team.add("Defenseur",Defenseur())
    return team
    
