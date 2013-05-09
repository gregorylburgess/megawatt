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
    flavor_text = models.CharField(max_length=300)
    success_val = models.IntegerField()
    success_text = models.CharField(max_length=100)
    fail_text = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    owner = models.ForeignKey(Player)
    def __unicode__(self):
        return self.type + ": " + self.name + self.id 


class GameState(models.Model):
    p1 = models.ForeignKey(Player)
    p2 = models.ForeignKey(Player)
    p1_hand={}
    p2_hand={}
    p1_field={}
    p2_field={}
    player_cards = {}
    neutral_cards= {}
    tactical_deck=[]
    e_gen_deck=[]
    p1_score = models.ForeignKey(PointSet)
    p2_score = models.ForeignKey(PointSet)
    active_player = ("p1","p2")
    phase = ("U","B","R","I","G","R")
    