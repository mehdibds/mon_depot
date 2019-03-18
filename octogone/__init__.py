from octogone.strategies import Shoot, Shoot_Anticipe, Dribbler, Defenseur
from Soccer.soccersimulator import SoccerTeam

def get_team(nb_players):
	team = SoccerTeam(name="Lyna et Mehdi")
	if nb_players == 1:
		team.add("Mbappe", Shoot_Anticipe())
	if nb_players == 2 :
		team.add("Mbappe",Shoot_Anticipe())
		team.add("Umtiti",Defenseur())
	if nb_players == 4 :
		team.add("Mbappe",Shoot_Anticipe())
		team.add("Umtiti",Defenseur())
		team.add("Dembele",Shoot_Anticipe())
		team.add("Varane",Defenseur())
	return team
	    
