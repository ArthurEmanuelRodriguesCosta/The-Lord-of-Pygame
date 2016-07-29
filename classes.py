# coding: utf-8
# Frodo Team
import pygame
from pygame.locals import *

class Aragorn:
        def __init__(self):
                self.i = 18
                self.j = 1
		self.x = (self.j * 32) + 7
		self.y = self.i * 32
                self.hp = 20
                self.defense = 3
                self.armor = "Heavy"
                self.speed = 4
                self.moves = self.speed
                self.attack = 8
                self.atk_range = 1
                self.atk_type = "Slash"
                self.icon = pygame.image.load("imagens/personagens/aragorn.gif")
		self.team = "F"
		self.enemy = "S"
                self.name = "Aragorn"
		self.hud_icon = pygame.image.load("imagens/HUD/aragorn.png")
                self.alive = True
		self.atacou = False

class Gimli:
        def __init__(self):
                self.i = 19
                self.j = 2
		self.x = (self.j * 32) + 7
		self.y = self.i * 32
                self.hp = 20
                self.defense = 3
                self.armor = "Heavy"
                self.speed = 4
                self.moves = self.speed
                self.attack = 7
                self.atk_range = 1
                self.atk_type = "Crush"
                self.icon = pygame.image.load("imagens/personagens/gimli.gif")
		self.team = "F"
		self.enemy = "S"
                self.name = "Gimli"
 		self.hud_icon = pygame.image.load("imagens/HUD/gimli.png")
                self.alive = True
		self.atacou = False

class Legolas:
        def __init__(self):
                self.i = 19
                self.j = 1
		self.x = (self.j * 32) + 7
		self.y = self.i * 32
                self.hp = 18
                self.defense = 2
                self.armor = "Medium"
                self.speed = 5
                self.moves = self.speed
                self.attack = 7
                self.atk_range = 3
                self.atk_type = "Pierce"
                self.icon = pygame.image.load("imagens/personagens/legolas.gif")
		self.team = "F"
		self.enemy = "S"
                self.name = "Legolas"
		self.hud_icon = pygame.image.load("imagens/HUD/legolas.jpg")
                self.alive = True
		self.atacou = False

class Frodo:
        def __init__(self):
                self.i = 19
                self.j = 0
		self.x = (self.j * 32) + 7
		self.y = self.i * 32
                self.hp = 12
                self.defense = 2
                self.armor = "Medium"
                self.speed = 7
                self.moves = self.speed
                self.attack = 4
                self.atk_range = 1
                self.atk_type = "Pierce"
                self.icon = pygame.image.load("imagens/personagens/frodo.gif")
		self.team = "F"
		self.enemy = "S"
                self.name = "Frodo"
		self.hud_icon = pygame.image.load("imagens/HUD/frodo.png")
                self.alive = True
		self.atacou = False
                
class Gandalf:
        def __init__(self):
                self.i = 18
                self.j = 0
		self.x = (self.j * 32) + 7
		self.y = self.i * 32
                self.hp = 15
                self.defense = 1
                self.armor = "Light"
                self.speed = 6
                self.moves = self.speed
                self.attack = 6
                self.atk_range = 2
                self.atk_type = "Magic"
                self.icon = pygame.image.load("imagens/personagens/gandalf.gif")
		self.team = "F"
		self.enemy = "S"
                self.name = "Gandalf"
		self.hud_icon = pygame.image.load("imagens/HUD/gandalf.png")
                self.alive = True
		self.atacou = False

# Sauron Team

class Orc:
        def __init__(self):
                self.i = 0
                self.j = 1
		self.x = (self.j * 32) + 7
		self.y = self.i * 32
                self.hp = 20
                self.defense = 3
                self.armor = "Heavy"
                self.speed = 4
                self.moves = self.speed
                self.attack = 7
                self.atk_range = 1
                self.atk_type = "Crush"
                self.icon = pygame.image.load("imagens/personagens/orc.gif")
		self.team = "S"
		self.enemy = "F"
                self.name = "Orc"
                self.alive = True 
		self.hud_icon = pygame.image.load("imagens/HUD/orc.jpg")
		self.atacou = False      

class Haradrim:
        def __init__(self):
                self.i = 1
                self.j = 0
		self.x = (self.j * 32) + 7
		self.y = self.i * 32
                self.hp = 20
                self.defense = 3
                self.armor = "Medium"
                self.speed = 4
                self.moves = self.speed
                self.attack = 6
                self.atk_range = 1
                self.atk_type = "Pierce"
                self.icon = pygame.image.load("imagens/personagens/haradrim.gif")
		self.team = "S"
		self.enemy = "F"
                self.name = "Haradrim"
		self.hud_icon = pygame.image.load("imagens/HUD/haradrim.jpg")
                self.alive = True 
		self.atacou = False   

class Urukhai:
        def __init__(self):
                self.i = 1
                self.j = 1
		self.x = (self.j * 32) + 7
		self.y = self.i * 32
                self.hp = 15
                self.defense = 2
                self.armor = "Heavy"
                self.speed = 5
                self.moves = self.speed
                self.attack = 7
                self.atk_range = 1
                self.atk_type = "Slash"
                self.icon = pygame.image.load("imagens/personagens/uruk-hai.gif")
		self.team = "S"
		self.enemy = "F"
                self.name = "Uruk-hai"
		self.hud_icon = pygame.image.load("imagens/HUD/uruk-hai.jpg")
                self.alive = True
		self.atacou = False                        

class Saruman:
        def __init__(self):
                self.i = 0
                self.j = 0
		self.x = (self.j * 32) + 7
		self.y = self.i * 32
                self.hp = 12
                self.defense = 1
                self.armor = "Light"
                self.speed = 6
                self.moves = self.speed
                self.attack = 7
                self.atk_range = 2
                self.atk_type = "Magic"
                self.icon = pygame.image.load("imagens/personagens/saruman.gif")
		self.team = "S"
		self.enemy = "F"
                self.name = "Saruman"
		self.hud_icon = pygame.image.load("imagens/HUD/saruman.png")
                self.alive = True
		self.atacou = False                       

class Wraith:
        def __init__(self):
                self.i = 0
                self.j = 2
		self.x = (self.j * 32) + 7
		self.y = self.i * 32
                self.hp = 12
                self.defense = 1
                self.armor = "Light"
                self.speed = 8
                self.moves = self.speed
                self.attack = 7
                self.atk_range = 1
                self.atk_type = "Pierce"
                self.icon = pygame.image.load("imagens/personagens/wraith.gif")
		self.team = "S"
		self.enemy = "F"
                self.name = "Wraith"
		self.hud_icon = pygame.image.load("imagens/HUD/wraith.png")
                self.alive = True 
		self.atacou = False   

# Cursor

class Cursor:
	def __init__(self):
		self.i = 19
		self.j = 0
		self.x = (self.j * 32) + 16
		self.y = (self.i * 32) + 16
		self.select = pygame.image.load("imagens/cursores/cursor.png")                  
		self.attack = pygame.image.load("imagens/cursores/cursor_2.png")
		self.img = self.select
		self.type = "select" 
