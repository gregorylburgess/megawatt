from megawatt.models import Card,Player
from django.contrib import admin

class MyCard(admin.TabularInline):
    model = Card

class MyPlayer(admin.TabularInline):
    model = Player
    
admin.site.register(MyCard, MyPlayer)
