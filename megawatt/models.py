from django.db import models

class PointSet(models.Model):
    nrg = models.IntegerField()
    user = models.IntegerField()
    env = models.IntegerField()
    dollar = models.IntegerField()
    

class Player(models.Model):
    points = models.ForeignKey(PointSet)
    owned_cards = []

    
class Card(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=200)
    type = ("E_Gen", "Tactical", "Service")
    flavor_text = models.CharField(max_length=100)
    success_val = models.IntegerField()
    image = models.CharField(max_length=200)
    owner = models.ForeignKey(Player)
    def __unicode__(self):
        return self.type + ": " + self.name + self.id 


class GameState(models.Model):
    player_cards = {}
    player_scores = {}
    neutral_cards= {}
    active_player = ("p1","p2")
    phase = ("U","B","R","G","E")
    