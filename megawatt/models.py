from django.db import models

class Player(models.Model):
    owned_cards = []
    
class PointSet(models.Model):
    player= models.ForeignKey(Player)
    nrg = models.IntegerField()
    env = models.IntegerField()
    dollar = models.IntegerField()
    user = models.IntegerField()

class Card(models.Model):
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
    