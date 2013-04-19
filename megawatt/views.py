from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from megawatt.settings import STATIC_URL
from megawatt.models import Card, Player
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
def index(request):
   
    cards ={}
    for i in range(0,15):
        name=i
        card = Card()
        card.id = i
        card.name= str(i)
        card.field = "p2_field"
        card.image = "http://a.dryicons.com/images/icon_sets/colorful_stickers_part_2_icons_set/png/256x256/light_bulb.png";
        cards[card.id]=card
    
    p2 = Player()
    p2.owned_cards = cards
    players = {}
    players[1]=(p2)
    return render_to_response(
              'index.html',
              {
               'STATIC_URL': STATIC_URL,
               'cards':cards,
               'p2':p2,
               })
@csrf_exempt
def update(request, field, id):
    print str("moved "+str(id) + " to " + str(field))
    return HttpResponse(status=200)
    