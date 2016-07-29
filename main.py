	# coding: utf-8
# Parte da Movimentação do jogo e alguns testes

from classes import *
import sys, tty, termios, os, pygame, time
from random import *
from pygame.locals import *
from xml import sax

# =========================================================================================
# Cria e atualiza o mapa / matriz principal

def matriz_espacos(lin, col):
        M = []
        for i in range(lin):
                M.append([])
                for j in range(col):
                        M[i].append(" ")

        return M

def bota_blocos_em_matriz(M, B):
	for cords in B:
		M[cords[1]][cords[0]] = "M"

def atualiza_HUD(unidade, Team):
	pygame.font.init()	

	# carrega fotos
	personagem_icon = unidade.hud_icon
	window.blit(personagem_icon, (0, 640))

        font = pygame.font.Font("elv.ttf", 25)                        
	name = font.render("%s" % unidade.name, True, (0, 0, 0))
	if unidade.hp < 5:
		hp = font.render("%d" % unidade.hp, True, (255, 0, 0))	
	else:        
		hp = font.render("%d" % unidade.hp, True, (0, 180, 0))
	armor = font.render("%s" % unidade.armor, True, (0, 0, 0))
	atk_type = font.render("%s" % unidade.atk_type, True, (0, 0, 0))

	# carrega palavras      
	window.blit(name, (180, 650))
	window.blit(hp, (165, 670))
	window.blit(armor, (220, 690))	
	window.blit(atk_type, (265, 710))

def atualiza_mapa():
	window.fill(0)
	window.blit(mapa_img , (0, 0))
	window.blit(vulcao, (735, 0))
        for unidade in Team1:
                mapa[unidade.i][unidade.j] = "F"
		window.blit(unidade.icon, (unidade.x, unidade.y))	

	for unidade in Team2:
		mapa[unidade.i][unidade.j] = "S"
		window.blit(unidade.icon, (unidade.x, unidade.y))

	# coloca mordor no mapa

	window.blit(wall, (738, 128))
	window.blit(wall1, (705, 133))
	window.blit(statue1, (640, 127))
	window.blit(wall, (573, 128))
	window.blit(wall1, (540, 133))
	window.blit(wall3, (511, 0))
	window.blit(wall3, (511, 96))	
	window.blit(corner, (513, 129))

	# coloca arvores no mapa

	window.blit(arvore1, (96, 32))
	window.blit(arvore2, (257, 131))
	window.blit(arvore3, (384,192))
	window.blit(arvore4, (32, 384))
	window.blit(arvore5, (705, 417))
	window.blit(arvore6, (417, 385))
	window.blit(arvore7, (570, 470))
	window.blit(arvore8, (256,288))
	window.blit(arvore9, (481, 194))

	# cursor
	if cursor_ativado:
		window.blit(cursor.img, (cursor.x, cursor.y))

	# HUD
	window.blit(HUD, (0, 640))
	window.blit(separador, (384, 640))
	
	pygame.font.init()
	font = pygame.font.Font("elv.ttf", 25)                        
	name = font.render("Nome: " , True, (0, 0, 0))
	hp = font.render("Vida: " , True, (0, 0, 0))
	armor = font.render("Armadura: ", True, (0, 0, 0))
	atk_type = font.render("Tipo de ataque: " , True, (0, 0, 0))

	window.blit(name, (110, 650))
	window.blit(hp, (110, 670))
	window.blit(armor, (110, 690))	
	window.blit(atk_type, (110, 710))
	
	# condição de vitoria

	if frodo.i == 0 and frodo.j == 24:
		pygame.mixer.quit()
		screen = pygame.display.set_mode((800, 736))
		movie11 = pygame.movie.Movie("videos/tentou1.mpeg")
		movie21 = pygame.movie.Movie("videos/tentou11.mpeg")
		movie11.play()
		movie21.play()
		movie11.stop()
		movie21.stop()		
		window.blit(img_win1, (0, 0))
		vic = pygame.mixer.music.load("sons/win.mp3")
		pygame.mixer.music.play(1, 0.0)
		pygame.font.init()
                font = pygame.font.Font("elv.ttf", 50)                        
		text = font.render("Frodo destruiu o anel!!!", True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.centerx = window.get_rect().centerx
                textRect.centery = window.get_rect().centery+24
                window.blit(text, textRect)
		pygame.display.update()
		time.sleep(10)
		reinicia_jogo()
		main_menu()
	if frodo.hp <= 0:
		pygame.mixer.quit()
		screen = pygame.display.set_mode((800, 736))
		movie11 = pygame.movie.Movie("videos/tentou2.mpeg")
		movie21 = pygame.movie.Movie("videos/tentou22.mpeg")
		movie11.play()
		movie21.play()
		movie11.stop()
		movie21.stop()
		explode_vulcao()
		window.blit(img_win2, (0, 0))
		vic = pygame.mixer.music.load("sons/win.mp3")
		pygame.mixer.music.play(1, 0.0)
		pygame.font.init()
    		font = pygame.font.Font("elv.ttf", 50)
    		text = font.render("Os orcs mataram Frodo!!!", True, (255, 0, 0))
    		textRect = text.get_rect()
    		textRect.centerx = window.get_rect().centerx
    		textRect.centery = window.get_rect().centery+24
		window.blit(text, textRect)
		pygame.display.update()
		time.sleep(10)
		reinicia_jogo()
		main_menu()	

	pygame.display.update()	

# =========================================================================================
# Parte da batalha

def explode_vulcao():
	sound = pygame.mixer.Sound("sons/Fireball.wav")
	magic = pygame.image.load("imagens/animacao/fire.png")
	sound.play()
	for y in range(9):
		for x in range(9):
			window.blit(enemy.hud_icon, (352, 320))
			window.blit(magic, (704, 0), (x * 100, y * 100, 100, 100))
			pygame.display.update()
			time.sleep(0.05)
	sound.stop()

def demage_feedback(player, enemy, sound):
	
	sprite = pygame.image.load("imagens/animacao/slash.gif")
	magic = pygame.image.load("imagens/animacao/fire.png")
	mod = modificador_atk_armor(player.atk_type, enemy.armor)


	# Coloca a foto do inimigo na tela
	pygame.display.update()
	time.sleep(1)

	# Animação de ataque
	
	if player.atk_type == "Magic":
		sound.set_volume(volume_s)
		sound.play()
		for y in range(9):
			for x in range(9):

				window.blit(enemy.hud_icon, (352, 320))
				window.blit(magic, (352,320), (x * 100, y * 100, 100, 100))
				pygame.display.update()
				time.sleep(0.05)

		sound.stop()
				
		
	
	if player.atk_type == "Slash":
		for i in range(int(2 * mod)):
			sound.play()

			window.blit(enemy.hud_icon, (352, 320))
			window.blit(sprite, (372,340), (0, 78, 32, 76))
			pygame.display.update()
			time.sleep(0.03)

			window.blit(enemy.hud_icon, (352, 320))
			window.blit(sprite, (372,340), (32, 78, 50, 76))
			pygame.display.update()
			time.sleep(0.03)

			window.blit(enemy.hud_icon, (352, 320))
			window.blit(sprite, (372,340), (93, 78, 50, 76))
			pygame.display.update()
			time.sleep(0.03)

			window.blit(enemy.hud_icon, (352, 320))
			window.blit(sprite, (372,340), (160, 78, 60, 76))
			pygame.display.update()
			time.sleep(0.03)

			window.blit(enemy.hud_icon, (352, 320))
			window.blit(sprite, (372,340), (220, 78, 70, 76))
			pygame.display.update()
			time.sleep(0.03)

			atualiza_mapa()
			window.blit(enemy.hud_icon, (352, 320))
			window.blit(sprite, (372,340), (295, 78, 40, 76))
			pygame.display.update()
			time.sleep(0.03)

			window.blit(enemy.hud_icon, (352, 320))
			window.blit(sprite, (372,340), (335, 78, 55, 76))
			pygame.display.update()
			time.sleep(0.03)
			sound.stop

			window.blit(enemy.hud_icon, (352, 320))
			pygame.display.update()

			time.sleep(0.5)			

	
	if player.atk_type == "Crush":
		for i in range(int(2 * mod)):
			sound.play()

			window.blit(enemy.hud_icon, (352, 320))
			window.blit(sprite, (372,340), (112, 0, 40, 60))
			pygame.display.update()
			time.sleep(0.03)

			window.blit(enemy.hud_icon, (352, 320))
			window.blit(sprite, (372,340), (152, 0, 60, 60))
			pygame.display.update()
			time.sleep(0.03)

			window.blit(enemy.hud_icon, (352, 320))
			window.blit(sprite, (372,340), (212, 0, 36, 60))
			pygame.display.update()
			time.sleep(0.03)

			window.blit(enemy.hud_icon, (352, 320))
			window.blit(sprite, (372,340), (250, 0, 50, 60))
			pygame.display.update()
			time.sleep(0.03)

			window.blit(enemy.hud_icon, (352, 320))
			window.blit(sprite, (372,340), (300, 0, 70, 60))
			pygame.display.update()
			time.sleep(0.03)
			
			window.blit(enemy.hud_icon, (352, 320))
			window.blit(sprite, (372,340), (370, 0, 60, 60))
			pygame.display.update()
			time.sleep(0.03)
			sound.stop()

			window.blit(enemy.hud_icon, (352, 320))
			pygame.display.update()

			time.sleep(0.5)			

	if player.atk_type == "Pierce":
		for i in range(int(2 * mod)):
			sound.play()

			window.blit(enemy.hud_icon, (352, 320))
			window.blit(sprite, (372,340), (370, 0, 60, 60))
			pygame.display.update()
			time.sleep(0.03)

			window.blit(enemy.hud_icon, (352, 320))
			window.blit(sprite, (372,340), (300, 0, 70, 60))
			pygame.display.update()
			time.sleep(0.03)

			window.blit(enemy.hud_icon, (352, 320))
			window.blit(sprite, (372,340), (250, 0, 50, 60))
			pygame.display.update()
			time.sleep(0.03)

			window.blit(enemy.hud_icon, (352, 320))
			window.blit(sprite, (372,340), (152, 0, 60, 60))
			pygame.display.update()
			time.sleep(0.03)

			window.blit(enemy.hud_icon, (352, 320))
			window.blit(sprite, (372,340), (112, 0, 40, 60))
			pygame.display.update()
			time.sleep(0.03)
			sound.stop()

			window.blit(enemy.hud_icon, (352, 320))
			pygame.display.update()			

			time.sleep(0.5)

	atualiza_mapa()

	

def animacao_ataque(player, enemy):
	if player == legolas:
		atk_sound = pygame.mixer.Sound("sons/Arrow.wav")
	elif player == gandalf or player == saruman:
		atk_sound = pygame.mixer.Sound("sons/Fireball.wav")
	elif player == frodo or player == aragorn or player == gimli or player == wraith or player == orc or player == uruk or player == haradrim:
		atk_sound = pygame.mixer.Sound("sons/Sword.wav")

	demage_feedback(player, enemy, atk_sound)
	

	

def ataque(player, enemy):
	player.atacou = True
	animacao_ataque(player, enemy)
	if player != saruman and player != gandalf:
        	dano = (player.attack - enemy.defense)
        	dano = int(dano * modificador_atk_armor(player.atk_type, enemy.armor))

	else:
		dano = player.attack

        enemy.hp -= dano
	if enemy.hp < 0:
		enemy.hp = 0

	font = pygame.font.Font("elv.ttf", 25)
	ataq1 = font.render("%d" % (dano), True, (255, 0, 0))
	window.blit(enemy.hud_icon, (352, 320))
	window.blit(ataq1, (400, 320))
	pygame.display.update()
	time.sleep(2)
	atualiza_mapa()
	ataq = font.render("%s atacou %s com dano de %d" % (player.name, enemy.name, dano), True, (0, 0, 0))
	hp_enemy_atual = font.render("%s agora tem %d de vida" % (enemy.name, enemy.hp), True, (0, 0, 0))	
	window.blit(ataq, (400,640))
	window.blit(hp_enemy_atual, (400, 660))
	pygame.display.update()

	print "%s HP = %d" % (enemy.name, enemy.hp)
	time.sleep(1)

def modificador_atk_armor(atk, armor):
        if (atk == "Crush" and armor == "Heavy") or (atk == "Slash" and armor == "Light") or (atk == "Pierce" and armor == "Medium"):
                return 1.5
        if (atk == "Crush" and armor == "Light") or (atk == "Slash" and armor == "Medium") or (atk == "Pierce" and armor == "Heavy"):
                return 1.0
        if (atk == "Crush" and armor == "Medium") or (atk == "Slash" and armor == "Heavy") or (atk == "Pierce" and armor == "Light"):
		return 0.5

def checar_atk_range(player):
	possibilidades = []
	rng = player.atk_range
	i = player.i
	j = player.j
	for lin in range(-i, i + 1, 1):
		for col in range(-j, j + 1, 1):
			if abs(lin) + abs(col) <= rng and abs(lin) + abs(col) != 0:
				tupla = (lin + i, col + j)
				possibilidades.append(tupla)

	return possibilidades
		
def direcao_ataque(player, Team):
	lin = player.i
	col = player.j
	cursor.type = "attack"
	cursor.img = cursor.attack 

	while True:
		if (Team == Team1 and escolha1 == "joystick") or (Team == Team2 and escolha2 == "joystick"):
			r = movimento_joy(cursor, Team)
		else:
			r = movimento(cursor, Team)
		if r == "HUD":
			atualiza_HUD(player, Team)
			pygame.display.update()
		if r == "attack":
			possibilidades = checar_atk_range(player)
			if mapa[cursor.i][cursor.j] == player.enemy and (cursor.i, cursor.j) in possibilidades:
				enemy = pega_unidade(cursor.i, cursor.j)
				x = cursor.x
				y = cursor.y
				cursor.x = 799
				cursor.y = 735
				atualiza_mapa()
				ataque(player, enemy)
				# chega se o inimigo morreu
				if enemy.hp <= 0:
					if Team == Team1:
						mapa[enemy.i][enemy.j] = " "
						Team2.remove(enemy)
						enemy.alive = False
					elif Team == Team2:
						mapa[enemy.i][enemy.j] = " "
						Team1.remove(enemy)
						enemy.alive = False
				
				

				cursor.x = x
				cursor.y = y
				player.moves = 0
				player.atacou = True
				cursor.type = "select"
				cursor.img = cursor.select
				if enemy.hp <= 0:
					return enemy
				else:
					return "vivo"
		if r == "back":
			cursor.type = "select"
			cursor.img = cursor.select
			return "vivo"
					
	

def pega_unidade(lin, col):
	for e in (Team1 + Team2):
		if lin == e.i and col == e.j:
			return e

def ataque_selecionado(player, Team):
	enemy = direcao_ataque(player, Team)

		
		
	



# =========================================================================================
# Parte da interação com o jogador, focando no turno e no que se pode fazer nele, junto com
# a parte da movimentação


def selecionar_acao_joy(unidade, Team):
	acoes = ["Mover", "Atacar"]

	if Team == Team1:
		up, down, right, left, confirm, back = pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_z, pygame.K_x
	if Team == Team2:
		up, down, right, left, confirm, back = pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a, pygame.K_k, pygame.K_l
	if Team == Team1 and escolha1 == "joystick":
		up = (0.0, -1.0)
		down = (0.0 , 0.999969482422)
		right = (0.999969482422 , 0.0)
		left = (-1.0 , 0.0)
		confirm = JOYSTICK1.get_button(3)
		back = JOYSTICK1.get_button(2)
	if Team == Team2 and escolha2 == "joystick":
		up = (0.0, -1.0)
		down = (0.0 , 0.999969482422)
		right = (0.999969482422 , 0.0)
		left = (-1.0 , 0.0)
		confirm = JOYSTICK2.get_button(3)
		back = JOYSTICK2.get_button(2)
	keys = [up, down, right, left]
	if escolha1 == "joystick":
		while True:
			for acao in acoes:
				a = ""
				os.system('clear')
				# pergunta
				atualiza_mapa()
				atualiza_HUD(unidade, Team)
				font = pygame.font.Font("elv.ttf", 25)                        			
				opcao_acao = font.render("O que deseja fazer?", True, (0, 0, 0))			
				window.blit(opcao_acao, (448, 650))
				
				# resposta                    			
				opcao_acao = font.render("%s" % acao, True, (0, 0, 0))			
				window.blit(opcao_acao, (480, 690))
				pygame.display.update()
	
				while True:	
					for event in pygame.event.get():
						if event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYBUTTONDOWN:
							if JOYSTICK1.get_axis(0) == 0 and JOYSTICK1.get_axis(1) <= -0.9:
								a = "break"
							if JOYSTICK1.get_button(2):
								atualiza_mapa()
								atualiza_HUD(unidade, Team)
								pygame.display.update()
								return acao
							if JOYSTICK1.get_button(1):
								atualiza_mapa()
								atualiza_HUD(unidade, Team)
								pygame.display.update()
								return "back"
						if event.type == pygame.KEYDOWN:
							if event.key == K_ESCAPE:
								pygame.quit()
								exit()
						if event.type == QUIT:
							pygame.quit()
							exit()
					if a == "break":
						break
					
 	if escolha2 == "joystick":
		while True:
			for acao in acoes:
				a = ""
				os.system('clear')
				# pergunta
				atualiza_mapa()
				atualiza_HUD(unidade, Team)
				font = pygame.font.Font("elv.ttf", 25)                        			
				opcao_acao = font.render("O que deseja fazer?", True, (0, 0, 0))			
				window.blit(opcao_acao, (448, 650))
				
				# resposta                    			
				opcao_acao = font.render("%s" % acao, True, (0, 0, 0))			
				window.blit(opcao_acao, (480, 690))
				pygame.display.update()
	
				while True:	
					for event in pygame.event.get():
						if event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYBUTTONDOWN:
							if JOYSTICK2.get_axis(0) == 0 and JOYSTICK2.get_axis(1) <= -0.9:
								a = "break"
							if JOYSTICK2.get_button(2):
								atualiza_mapa()
								atualiza_HUD(unidade, Team)
								pygame.display.update()
								return acao
							if JOYSTICK2.get_button(1):
								atualiza_mapa()
								atualiza_HUD(unidade, Team)
								pygame.display.update()
								return "back"
						if event.type == pygame.KEYDOWN:
							if event.key == K_ESCAPE:
								pygame.quit()
								exit()
						if event.type == QUIT:
							pygame.quit()
							exit()
					if a == "break":
						break
def selecionar_acao(unidade, Team):
	acoes = ["Mover", "Atacar"]

	if Team == Team1:
		up, down, right, left, confirm, back = pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_z, pygame.K_x
	if Team == Team2:
		up, down, right, left, confirm, back = pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a, pygame.K_k, pygame.K_l
	if Team == Team1 and escolha1 == "joystick":
		up = (0.0, -1.0)
		down = (0.0 , 0.999969482422)
		right = (0.999969482422 , 0.0)
		left = (-1.0 , 0.0)
		confirm = JOYSTICK1.get_button(3)
		back = JOYSTICK1.get_button(2)
	if Team == Team2 and escolha2 == "joystick":
		up = (0.0, -1.0)
		down = (0.0 , 0.999969482422)
		right = (0.999969482422 , 0.0)
		left = (-1.0 , 0.0)
		confirm = JOYSTICK2.get_button(3)
		back = JOYSTICK2.get_button(2)
	keys = [up, down, right, left]
	
	while True:
		for acao in acoes:
			a = ""
			os.system('clear')
			# pergunta
			atualiza_mapa()
			atualiza_HUD(unidade, Team)
			font = pygame.font.Font("elv.ttf", 25)                        			
			opcao_acao = font.render("O que deseja fazer?", True, (0, 0, 0))			
			window.blit(opcao_acao, (448, 650))
				
			# resposta                    			
			opcao_acao = font.render("%s" % acao, True, (0, 0, 0))			
			window.blit(opcao_acao, (480, 690))
			pygame.display.update()

			while True:	
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key in keys:
							a = "break"
						if (event.key == confirm or confirm == 1):
							atualiza_mapa()
							atualiza_HUD(unidade, Team)
							pygame.display.update()
							return acao
						if (event.key == back or back == 1):
							atualiza_mapa()
							atualiza_HUD(unidade, Team)
							pygame.display.update()
							return "back"
						if event.key == K_ESCAPE:
							pygame.quit()
							exit()			
					if event.type == QUIT:
						pygame.quit()
						exit()
				if a == "break":
					break
				


def movimento(unidade, Team):
	moveu = False
	if Team == Team1 and escolha1 == "keyboard":
		up, down, right, left, confirm, back = pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_z, pygame.K_x
	if Team == Team2 and escolha2 == "keyboard":
		up, down, right, left, confirm, back = pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a, pygame.K_k, pygame.K_l
	while True:
		lin = unidade.i
		col = unidade.j
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()

			# MDAR MUDAR MDAR MDAR MUDAR MUDAR =-==========--==============================
			if event.type == pygame.KEYDOWN:
				# Ações das unidades

				if unidade != cursor:
					if event.key == K_ESCAPE:
						pygame.quit()
						exit()
        				if (event.key == up) and lin > 0 and mapa[lin-1][col] == " ":
						unidade.y -= 32	
						mapa[lin][col] = " "
						mapa[lin-1][col] = unidade.team
						unidade.i -= 1
						moveu = True
        				elif (event.key == down) and lin < len(mapa) -1 and mapa[lin+1][col] == " ":
						unidade.y += 32
						mapa[lin][col] = " "
						mapa[lin+1][col] = unidade.team
						unidade.i += 1
						moveu = True
					elif (event.key == left) and col > 0 and mapa[lin][col-1] == " ":
						unidade.x -= 32
						mapa[lin][col] = " "
						mapa[lin][col-1] = unidade.team
						unidade.j -= 1
						moveu = True
					elif (event.key == right) and col < len(mapa[0]) -1 and mapa[lin][col+1] == " ":
						unidade.x += 32
						mapa[lin][col] = " "
						mapa[lin][col+1] = unidade.team
						unidade.j += 1
						moveu = True
					elif (event.key == confirm or confirm == 1):
						atualiza_mapa()
						atualiza_HUD(unidade, Team)
						pygame.display.update()
						unidade.moves = 1
						return None
					elif (event.key == back or back == 1):
						os.system('clear')
						return "back"
						

				# Ações do cursor
				if unidade == cursor:
					if event.key == K_ESCAPE:
						pygame.quit()
						exit()
        				if (event.key == up) and lin > 0:
						unidade.y -= 32	
						unidade.i -= 1
						moveu = True
        				elif (event.key == down) and lin < len(mapa) -1:
						unidade.y += 32
						unidade.i += 1
						moveu = True
					elif (event.key == left) and col > 0:
						unidade.x -= 32
						unidade.j -= 1
						moveu = True
					elif (event.key == right) and col < len(mapa[0]) -1:
						unidade.x += 32
						unidade.j += 1
						moveu = True

					elif (event.key == confirm or confirm == 1) and cursor.type == "attack":
						return "attack"
					elif (event.key == back or back == 1) and cursor.type == "attack":
						return "back"

					elif (event.key == confirm or confirm == 1) and cursor.type == "select":
						u = pega_unidade(lin, col)
						if u in Team1 + Team2:
							atualiza_HUD(u, Team)
							pygame.display.update()
	
						if u not in Team1 + Team2:
							os.system('clear')

							# pergunta
							atualiza_mapa()
							font = pygame.font.Font("elv.ttf", 30)
							parar = font.render("Parar turno?", True, (0, 0, 0))	
							window.blit(parar, (460, 650))
							pygame.display.update()
							
							while True:
								for event in pygame.event.get():
									if event.type == pygame.KEYDOWN or event.type == pygame.locals.JOYBUTTONDOWN:
										if (event.key == confirm or confirm == 1):
											return "skip"
										if (event.key == back or back == 1):
											os.system('clear')
											atualiza_mapa()
											pygame.display.update()
											return ""
									
						if u in Team:
							atualiza_HUD(u, Team)
							pygame.display.update()
							acabou = False
							while not acabou:
								acao = selecionar_acao(u, Team)
								if acao == "back":
									os.system('clear')
									return None
								if acao == "Atacar" and not u.atacou:
									atualiza_mapa()
									atualiza_HUD(u, Team)
									unidade.moves = 0
									ataque_selecionado(u, Team)
									v = atualiza_mapa()
									atualiza_HUD(u, Team)
									pygame.display.update()
									if v == "v2":
										return "v2"
									return None
								if acao == "Mover":
									acabou = False
									cursor.x = 799
									cursor.y = 735
									atualiza_mapa()
									while True:
										os.system('clear')
										font = pygame.font.Font("elv.ttf", 25)                    
										mov = font.render("Movimentos restantes: %s" % u.moves, True, (0, 0, 0))
										window.blit(mov, (400,650))
										pygame.display.update()
										
										if u.moves == 0:
											cursor.i, cursor.j = u.i, u.j
											cursor.x, cursor.y = (cursor.j * 32) + 16, (cursor.i * 32) + 16
											atualiza_mapa()
											atualiza_HUD(u, Team)
											# caso exista inimigos que possa atacar, selecione ataque
											redondezas = checar_atk_range(u)
											if u in Team1:
												for e in Team2:
													if (e.i, e.j) in redondezas:
														direcao_ataque(u, Team1)
														break
											elif u in Team2:
												for e in Team1:
													if (e.i, e.j) in redondezas:
														direcao_ataque(u, Team2)
														break

											acabou = True
											break
										r = movimento(u, Team)
										u.moves -= 1
										if r == "v1":
											cursor.i, cursor.j = u.i, u.j
											cursor.x, cursor.y = (cursor.j * 32) + 16, (cursor.i * 32) + 16
											return "v1"
										if r == "change char":
											cursor.i, cursor.j = u.i, u.j
											cursor.x, cursor.y = (cursor.j * 32) + 16, (cursor.i * 32) + 16
											break
										if r == "back":
											cursor.i, cursor.j = u.i, u.j
											cursor.x, cursor.y = (cursor.j * 32) + 16, (cursor.i * 32) + 16
											break
									
								


			if moveu:
				break

		if moveu:
			break

		
	vitoria = atualiza_mapa()
	if unidade != cursor:
        	atualiza_HUD(unidade, Team)
	pygame.display.update()
	if vitoria == "v1":
		return "v1"
	if vitoria == "v2":
		return "v2"
	if unidade == cursor:
    		if cursor.type == "attack":
        		return "HUD"

def movimento_joy(unidade, Team):
	moveu = False
	if Team == Team1 and escolha1 == "joystick":
		up = (0.0, -1.0)
		down = (0.0 , 1.0)
		right = (1.0, 0.0)
		left = (-1.0 , 0.0)
		confirm = JOYSTICK1.get_button(2)
		back = JOYSTICK1.get_button(1)
	if Team == Team2 and escolha2 == "joystick":
		up = (0.0, -1.0)
		down = (0.0 , 0.999969482422)
		right = (0.999969482422 , 0.0)
		left = (-1.0 , 0.0)
		confirm = JOYSTICK2.get_button(2)
		back = JOYSTICK2.get_button(1)
	if escolha1 == "joystick":
		while True:
			lin = unidade.i
			col = unidade.j
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == K_ESCAPE:
						pygame.quit()
						exit()
				if event.type == QUIT:
					pygame.quit()
					exit()
	
				# MDAR MUDAR MDAR MDAR MUDAR MUDAR =-==========--==============================
				if event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYBUTTONDOWN:
					# Ações das unidades
	
					if unidade != cursor:
	        				if JOYSTICK1.get_axis(0) == 0 and JOYSTICK1.get_axis(1) <= -0.9 and lin > 0 and mapa[lin-1][col] == " ":
							unidade.y -= 32	
							mapa[lin][col] = " "
							mapa[lin-1][col] = unidade.team
							unidade.i -= 1
							moveu = True
	        				elif JOYSTICK1.get_axis(0) == 0 and JOYSTICK1.get_axis(1) >= 0.9 and lin < len(mapa) -1 and mapa[lin+1][col] == " ":
							unidade.y += 32
							mapa[lin][col] = " "
							mapa[lin+1][col] = unidade.team
							unidade.i += 1
							moveu = True
						elif JOYSTICK1.get_axis(0) <= -0.9 and JOYSTICK1.get_axis(1) == 0.0 and col > 0 and mapa[lin][col-1] == " ":
							unidade.x -= 32
							mapa[lin][col] = " "
							mapa[lin][col-1] = unidade.team
							unidade.j -= 1
							moveu = True
						elif JOYSTICK1.get_axis(0) >= 0.9 and JOYSTICK1.get_axis(1) == 0.0 and col < len(mapa[0]) -1 and mapa[lin][col+1] == " ":
							unidade.x += 32
							mapa[lin][col] = " "
							mapa[lin][col+1] = unidade.team
							unidade.j += 1
							moveu = True
						elif JOYSTICK1.get_button(2):
							atualiza_mapa()
							atualiza_HUD(unidade, Team)
							pygame.display.update()
							unidade.moves = 1
							return None
						elif JOYSTICK1.get_button(1):
							os.system('clear')
							return "back"
							
	
					# Ações do cursor
					if unidade == cursor:
	
	        				if JOYSTICK1.get_axis(0) == 0 and JOYSTICK1.get_axis(1) <= -0.9 and lin > 0:
							unidade.y -= 32	
							unidade.i -= 1
							moveu = True
	        				elif JOYSTICK1.get_axis(0) == 0 and JOYSTICK1.get_axis(1) >= 0.9 and lin < len(mapa) -1:
							unidade.y += 32
							unidade.i += 1
							moveu = True
						elif JOYSTICK1.get_axis(0) <= -0.9 and JOYSTICK1.get_axis(1) == 0.0 and col > 0:
							unidade.x -= 32
							unidade.j -= 1
							moveu = True
						elif JOYSTICK1.get_axis(0) >= 0.9 and JOYSTICK1.get_axis(1) == 0.0 and col < len(mapa[0]) -1:
							unidade.x += 32
							unidade.j += 1
							moveu = True

						elif JOYSTICK1.get_button(2) and cursor.type == "attack":
							return "attack"
						elif JOYSTICK1.get_button(1) and cursor.type == "attack":
							return "back"

						elif JOYSTICK1.get_button(2) and cursor.type == "select":
							u = pega_unidade(lin, col)
							if u in Team1 + Team2:
								atualiza_HUD(u, Team)
								pygame.display.update()
							if u not in Team1 + Team2:
								os.system('clear')
	
								# pergunta
								atualiza_mapa()
								font = pygame.font.Font("elv.ttf", 30)
								parar = font.render("Parar turno?", True, (0, 0, 0))	
								window.blit(parar, (460, 650))
								pygame.display.update()
								
								while True:
									for event in pygame.event.get():
										if event.type == pygame.locals.JOYBUTTONDOWN:
											if  JOYSTICK1.get_button(2):
												return "skip"
											if  JOYSTICK1.get_button(1):
												os.system('clear')
												atualiza_mapa()
												pygame.display.update()
												return ""
										
							if u in Team:
								atualiza_HUD(u, Team)
								pygame.display.update()
								acabou = False
								while not acabou:
									acao = selecionar_acao_joy(u, Team)
									if acao == "back":
										os.system('clear')
										return None
									if acao == "Atacar" and not u.atacou:
										atualiza_mapa()
										atualiza_HUD(u, Team)
										unidade.moves = 0
										ataque_selecionado(u, Team)
										v = atualiza_mapa()
										atualiza_HUD(u, Team)
										pygame.display.update()
										if v == "v2":
											return "v2"
										return None
									if acao == "Mover":
										acabou = False
										cursor.x = 799
										cursor.y = 735
										atualiza_mapa()
										while True:
											os.system('clear')
											font = pygame.font.Font("elv.ttf", 25)                    
											mov = font.render("Movimentos restantes: %s" % u.moves, True, (0, 0, 0))
											window.blit(mov, (400,650))
											pygame.display.update()
											
											if u.moves == 0:
												cursor.i, cursor.j = u.i, u.j
												cursor.x, cursor.y = (cursor.j * 32) + 16, (cursor.i * 32) + 16
												atualiza_mapa()
												atualiza_HUD(u, Team)
												# caso exista inimigos que possa atacar, selecione ataque
												redondezas = checar_atk_range(u)
												if u in Team1:
													for e in Team2:
														if (e.i, e.j) in redondezas:
															direcao_ataque(u, Team1)
															break
												elif u in Team2:
													for e in Team1:
														if (e.i, e.j) in redondezas:
															direcao_ataque(u, Team2)
															break

												acabou = True
												break
											r = movimento_joy(u, Team)
											u.moves -= 1
											if r == "v1":
												cursor.i, cursor.j = u.i, u.j
												cursor.x, cursor.y = (cursor.j * 32) + 16, (cursor.i * 32) + 16
												return "v1"
											if r == "change char":
												cursor.i, cursor.j = u.i, u.j
												cursor.x, cursor.y = (cursor.j * 32) + 16, (cursor.i * 32) + 16
												break
											if r == "back":
												cursor.i, cursor.j = u.i, u.j
												cursor.x, cursor.y = (cursor.j * 32) + 16, (cursor.i * 32) + 16
												break
									
								


				if moveu:
					break

			if moveu:
				break

		
		vitoria = atualiza_mapa()
		if unidade != cursor:
	        	atualiza_HUD(unidade, Team)
		pygame.display.update()
		if vitoria == "v1":
			return "v1"
		if vitoria == "v2":
			return "v2"
		if unidade == cursor:
	    		if cursor.type == "attack":
	        		return "HUD"
	if escolha2 == "joystick":
		while True:
			lin = unidade.i
			col = unidade.j
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == K_ESCAPE:
						pygame.quit()
						exit()
				if event.type == QUIT:
					pygame.quit()
					exit()
	
				# MDAR MUDAR MDAR MDAR MUDAR MUDAR =-==========--==============================
				if event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYBUTTONDOWN:
					# Ações das unidades
	
					if unidade != cursor:
	        				if JOYSTICK2.get_axis(0) == 0 and JOYSTICK2.get_axis(1) <= -0.9 and lin > 0 and mapa[lin-1][col] == " ":
							unidade.y -= 32	
							mapa[lin][col] = " "
							mapa[lin-1][col] = unidade.team
							unidade.i -= 1
							moveu = True
	        				elif JOYSTICK2.get_axis(0) == 0 and JOYSTICK2.get_axis(1) >= 0.9 and lin < len(mapa) -1 and mapa[lin+1][col] == " ":
							unidade.y += 32
							mapa[lin][col] = " "
							mapa[lin+1][col] = unidade.team
							unidade.i += 1
							moveu = True
						elif JOYSTICK2.get_axis(0) <= -0.9 and JOYSTICK2.get_axis(1) == 0.0 and col > 0 and mapa[lin][col-1] == " ":
							unidade.x -= 32
							mapa[lin][col] = " "
							mapa[lin][col-1] = unidade.team
							unidade.j -= 1
							moveu = True
						elif JOYSTICK2.get_axis(0) >= 0.9 and JOYSTICK2.get_axis(1) == 0.0 and col < len(mapa[0]) -1 and mapa[lin][col+1] == " ":
							unidade.x += 32
							mapa[lin][col] = " "
							mapa[lin][col+1] = unidade.team
							unidade.j += 1
							moveu = True
						elif JOYSTICK2.get_button(2):
							atualiza_mapa()
							atualiza_HUD(unidade, Team)
							pygame.display.update()
							unidade.moves = 1
							return None
						elif JOYSTICK2.get_button(1):
							os.system('clear')
							return "back"
							
	
					# Ações do cursor
					if unidade == cursor:
	
	        				if JOYSTICK2.get_axis(0) == 0 and JOYSTICK2.get_axis(1) <= -0.9 and lin > 0:
							unidade.y -= 32	
							unidade.i -= 1
							moveu = True
	        				elif JOYSTICK2.get_axis(0) == 0 and JOYSTICK2.get_axis(1) >= 0.9 and lin < len(mapa) -1:
							unidade.y += 32
							unidade.i += 1
							moveu = True
						elif JOYSTICK2.get_axis(0) <= -0.9 and JOYSTICK2.get_axis(1) == 0.0 and col > 0:
							unidade.x -= 32
							unidade.j -= 1
							moveu = True
						elif JOYSTICK2.get_axis(0) >= 0.9 and JOYSTICK2.get_axis(1) == 0.0 and col < len(mapa[0]) -1:
							unidade.x += 32
							unidade.j += 1
							moveu = True

						elif JOYSTICK2.get_button(2) and cursor.type == "attack":
							return "attack"
						elif JOYSTICK2.get_button(1) and cursor.type == "attack":
							return "back"

						elif JOYSTICK2.get_button(2) and cursor.type == "select":
							u = pega_unidade(lin, col)
							if u not in Team:
								os.system('clear')
	
								# pergunta
								atualiza_mapa()
								font = pygame.font.Font("elv.ttf", 30)
								parar = font.render("Parar turno?", True, (0, 0, 0))	
								window.blit(parar, (460, 650))
								pygame.display.update()
								
								while True:
									for event in pygame.event.get():
										if event.type == pygame.locals.JOYBUTTONDOWN:
											if  JOYSTICK2.get_button(2):
												return "skip"
											if  JOYSTICK2.get_button(1):
												os.system('clear')
												atualiza_mapa()
												pygame.display.update()
												return ""
										
							if u in Team:
								atualiza_HUD(u, Team)
								pygame.display.update()
								acabou = False
								while not acabou:
									acao = selecionar_acao_joy(u, Team)
									if acao == "back":
										os.system('clear')
										return None
									if acao == "Atacar" and not u.atacou:
										atualiza_mapa()
										atualiza_HUD(u, Team)
										unidade.moves = 0
										ataque_selecionado(u, Team)
										v = atualiza_mapa()
										atualiza_HUD(u, Team)
										pygame.display.update()
										if v == "v2":
											return "v2"
										return None
									if acao == "Mover":
										acabou = False
										cursor.x = 799
										cursor.y = 735
										atualiza_mapa()
										while True:
											os.system('clear')
											font = pygame.font.Font("elv.ttf", 25)                    
											mov = font.render("Movimentos restantes: %s" % u.moves, True, (0, 0, 0))
											window.blit(mov, (400,650))
											pygame.display.update()
											
											if u.moves == 0:
												cursor.i, cursor.j = u.i, u.j
												cursor.x, cursor.y = (cursor.j * 32) + 16, (cursor.i * 32) + 16
												atualiza_mapa()
												atualiza_HUD(u, Team)
												# caso exista inimigos que possa atacar, selecione ataque
												redondezas = checar_atk_range(u)
												if u in Team1:
													for e in Team2:
														if (e.i, e.j) in redondezas:
															direcao_ataque(u, Team1)
															break
												elif u in Team2:
													for e in Team1:
														if (e.i, e.j) in redondezas:
															direcao_ataque(u, Team2)
															break

												acabou = True
												break
											r = movimento_joy(u, Team)
											u.moves -= 1
											if r == "v1":
												cursor.i, cursor.j = u.i, u.j
												cursor.x, cursor.y = (cursor.j * 32) + 16, (cursor.i * 32) + 16
												return "v1"
											if r == "change char":
												cursor.i, cursor.j = u.i, u.j
												cursor.x, cursor.y = (cursor.j * 32) + 16, (cursor.i * 32) + 16
												break
											if r == "back":
												cursor.i, cursor.j = u.i, u.j
												cursor.x, cursor.y = (cursor.j * 32) + 16, (cursor.i * 32) + 16
												break
									
								


				if moveu:
					break

			if moveu:
				break

		
		vitoria = atualiza_mapa()
		if unidade != cursor:
	        	atualiza_HUD(unidade, Team)
		pygame.display.update()
		if vitoria == "v1":
			return "v1"
		if vitoria == "v2":
			return "v2"
		if unidade == cursor:
	    		if cursor.type == "attack":
	        		return "HUD"

def turnos():


	atualiza_mapa()
	os.system("clear")
	# aviso 1
	atualiza_mapa()
	font = pygame.font.Font("elv.ttf", 40)                        			
	aviso1 = font.render("Vez do time de Frodo, Jogador 1!!!", True, (0, 0, 0))			
	window.blit(aviso1, (150, 250))
	pygame.display.update()
	
	time.sleep(2)
	atualiza_mapa()
	pygame.display.update()
	os.system("clear")
	cursor.i = frodo.i
	cursor.j = frodo.j
	cursor.x = (cursor.j * 32) + 16
	cursor.y = (cursor.i * 32) + 16
	atualiza_mapa()
	while total_moves(Team1) > 0:
                if escolha1 == "keyboard":
                        r = movimento(cursor, Team1)
                        if r == "skip":
                                break

                if escolha1 == "joystick":
                        r = movimento_joy(cursor, Team1)
                        if r == "skip":
                                break

	atualiza_mapa()
	os.system("clear")
		
	# aviso 2
	atualiza_mapa()
	font = pygame.font.Font("elv.ttf", 40)                        			
	aviso1 = font.render("Vez do time de Sauron, Jogador 2!!!", True, (0, 0, 0))			
	window.blit(aviso1, (150, 250))
	pygame.display.update()
	
	time.sleep(2)
	atualiza_mapa()
	pygame.display.update()
	os.system("clear")
	cursor.i = Team2[0].i
	cursor.j = Team2[0].j
	cursor.x = (cursor.j * 32) + 16
	cursor.y = (cursor.i * 32) + 16
	atualiza_mapa()
	while total_moves(Team2) > 0:
                if escolha2 == "keyboard":
                        r = movimento(cursor, Team2)
                        if r == "skip":
                                break

                if escolha2 == "joystick":
                        r = movimento_joy(cursor, Team2)
                        if r == "skip":
                                break

def restaura_movimento():
	for e in Team1 + Team2:
		e.moves = e.speed
		e.atacou = False

def total_moves(Team):
	total = 0
	for e in Team:
		total += e.moves

	return total

def posicao_randomica():
	posicoes = []
	for unidade in Team2:
		while True:
			i = randint(0, 2)
			j = randint(0, 2)
			posicao = (i, j)
			if posicao not in posicoes:
				unidade.i = i
				unidade.j = j
				unidade.x = (j * 32) + 7
				unidade.y = i * 32
				posicoes.append(posicao)
				break

	for unidade in Team1:
		while True:
			i = randint(17, 19)
			j = randint(0, 2)
			posicao = (i, j)
			if posicao not in posicoes:
				unidade.i = i
				unidade.j = j
				unidade.x = (j * 32) + 7
				unidade.y = i * 32
				posicoes.append(posicao)
				break


# =========================================================================================
# Menus
def creditos():
	while True:
		window.blit(tela_creditos, (0, 0))
		pygame.font.init()
		font = pygame.font.Font("elv.ttf", 50)
		text = font.render("", True, (100, 100, 100))
		textRect = text.get_rect()
		textRect.centerx = window.get_rect().centerx
		textRect.centery = window.get_rect().centery
		window.blit(text, textRect)
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					exit()
				if event.key == back:
					return None		
	
def como_jogar():
	while True:
		window.blit(tela_instrucoes, (0, 0))
		pygame.font.init()
		font = pygame.font.Font("elv.ttf", 50)
		text = font.render("", True, (100, 100, 100))
		textRect = text.get_rect()
		textRect.centerx = window.get_rect().centerx
		textRect.centery = window.get_rect().centery
		window.blit(text, textRect)
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					exit()
				if event.key == back:
					return None
				
def main_menu():
	pygame.mixer.init()
	menu_music = pygame.mixer.music.load("sons/menu.mp3")
	gollum_cords =  (250, 243)
	acao = "start"
	pygame.mixer.music.play(-1, 0.0)
	while True:
		window.blit(tela_menu, (0, 0))
		pygame.font.init()
                font = pygame.font.Font("elv.ttf", 45) 
		title_font = pygame.font.Font("elv.ttf", 100)           
            
		text1 = font.render("Iniciar", True, (255, 255, 255))
		text2 = font.render("Creditos", True, (255, 255, 255))
		text3 = font.render("Como Jogar", True, (255, 255, 255))
		text4 = font.render("Mudar", True, (255, 255, 255))
		text5 = font.render("Pressione esc a qualquer momento para sair", True, (255, 5, 50))
		title = font.render("THE LORD OF PYGAME", True, (255, 255, 255))

                textRect1 = text1.get_rect()
                textRect2 = text2.get_rect()
                textRect3 = text3.get_rect()
		textRect4 = text4.get_rect()
		titleRect = title.get_rect()

                textRect1.centerx = window.get_rect().centerx
                textRect1.centery = window.get_rect().centery - 106
		textRect4.centerx = window.get_rect().centerx 
                textRect4.centery = window.get_rect().centery - 50
		textRect2.centerx = window.get_rect().centerx
		textRect2.centery = window.get_rect().centery + 75		
		textRect3.centerx = window.get_rect().centerx
                textRect3.centery = window.get_rect().centery + 15
                titleRect.centerx = window.get_rect().centerx
                titleRect.centery = window.get_rect().centery - 350


                window.blit(text1, textRect1)	
                window.blit(text2, textRect2)
                window.blit(text3, textRect3)
		window.blit(text4, textRect4)
		window.blit(text5, (0, 650))
		window.blit(title, titleRect)
		window.blit(gollum, gollum_cords)
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					exit()
				if event.key == confirm and acao == "start":
					pygame.mixer.music.fadeout(1000)
					pygame.mixer.music.load("sons/gameplay.mp3")
					pygame.mixer.music.play(-1, 0.0)
					posicao_randomica()
					atualiza_mapa()
					pygame.display.flip()
					game_loop()
					return None
					height = 736
				elif event.key == confirm and acao == "como jogar":
					como_jogar()
				elif event.key == confirm and acao == "creditos":
					creditos()
				elif event.key == confirm and acao == "mudar":
					mudar()
				elif event.key == pygame.K_DOWN and acao == "start":
					gollum_cords = (250, 243 + 60)
					acao = "mudar"
				elif event.key == pygame.K_DOWN and acao == "mudar":
					gollum_cords = (250, 243 + 120)
					acao = "como jogar"
				elif event.key == pygame.K_DOWN and acao == "como jogar":
					gollum_cords = (250, 243 + 180)
					acao = "creditos"
				elif event.key == pygame.K_UP and acao == "creditos":
					gollum_cords = (250, 243 + 120)
					acao = "como jogar"
				elif event.key == pygame.K_UP and acao == "como jogar":
					gollum_cords = (250, 243 + 60)
					acao = "mudar"
				elif event.key == pygame.K_UP and acao == "mudar":
					gollum_cords = (250, 243)
					acao = "start"

def mudar():
	global tela_cheia
	global volume_m
	global escolha1
	global escolha2
	global JOYSTICK1
	global JOYSTICK2
	gollum_cords = (4, 50)
	muda = "musica"
	while True:
		window.blit(tela_mudar, (0, 0))

		font = pygame.font.Font("elv.ttf", 50)
		text_som = font.render("Volume", True, (0, 0, 0))
		text_musica = font.render("Musica:", True, (100, 100, 100))
		text_efeitos = font.render("Efeitos:", True, (100, 100, 100))		
		text_tela = font.render("Tela", True, (0, 0, 0))
		text_cheia = font.render("Tela Cheia", True, (100, 100, 100))
		text_controles = font.render("Controles:", True, (0, 0, 0))
		text_vol = font.render("%.1f" % volume_m, True, (0, 0, 0))
		text_vol_s = font.render("%.1f" % volume_s, True, (0, 0, 0))
		text_jogador1 = font.render("Jogador 1", True, (0, 0, 0))
		text_jogador2 = font.render("Jogador 2", True, (0, 0, 0))

		window.blit(text_vol, (220, 50))
		window.blit(text_vol_s, (220, 100))
		window.blit(text_som, (0, 0))
		window.blit(text_musica, (30, 50))
		window.blit(text_efeitos, (30, 100))
		window.blit(text_tela, (0, 150))
		window.blit(text_cheia, (30, 200))
		window.blit(text_controles, (0, 250))
		window.blit(text_jogador1, (30, 300))
		window.blit(text_jogador2, (30, 350))
		if tela_cheia:
			window.blit(conf, (250, 200))
		else:
			window.blit(cancel, (250, 200))
		if escolha1 == "keyboard":
			window.blit(keyboard_img, (210, 280))
		else:
			try:
				JOYSTICK1 = pygame.joystick.Joystick(0) # create a joystick instance
				JOYSTICK1.init() # init instance
				font1 = pygame.font.Font("elv.ttf", 25)
				text_joystick1 = font1.render('ON: ' + JOYSTICK1.get_name(), True, (0, 0, 0))
				window.blit(text_joystick1, (300, 300))
			except pygame.error:
				font1 = pygame.font.Font("elv.ttf", 25)
				text_joystick1 = font1.render('Conecte um joystick e reinicie o jogo', True, (255, 0, 100))
				window.blit(text_joystick1, (300, 300))
			window.blit(joystick_img, (210, 280))
		if escolha2 == "keyboard":
			window.blit(keyboard_img, (210, 330))
		else:
			try:
				JOYSTICK2 = pygame.joystick.Joystick(1) # create a joystick instance
				JOYSTICK2.init() # init instance
				font1 = pygame.font.Font("elv.ttf", 25)
				text_joystick2 = font1.render('ON: ' + JOYSTICK2.get_name(), True, (0, 0, 0))
				window.blit(text_joystick2, (300, 350))
			except pygame.error:
				font1 = pygame.font.Font("elv.ttf", 25)
				text_joystick2 = font1.render('Conecte um joystick e reinicie o jogo', True, (255, 0, 100))
				window.blit(text_joystick2, (300, 350))
			window.blit(joystick_img, (210, 330))
		window.blit(gollum, gollum_cords)
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					exit()
				if event.key == back:
					return None
				elif event.key == confirm and muda == "tela cheia" and tela_cheia:
					pygame.display.set_mode((width, hight))
					tela_cheia = False
					pygame.mouse.set_visible(True)
				elif event.key == confirm and muda == "tela cheia":
					tela_cheia = True
					pygame.mouse.set_visible(False)
					pygame.display.set_mode((width, hight), pygame.FULLSCREEN)
				elif event.key == confirm and muda == "musica":
					sair = False
					while True:
						pygame.mixer.music.set_volume(volume_m)
						for event in pygame.event.get():
							if event.type == QUIT:
								pygame.quit()
								exit()
							if event.type == pygame.KEYDOWN:
								if event.key == K_ESCAPE:
									pygame.quit()
									exit()
								if event.key == back:
									sair = True
									break
								elif event.key == K_DOWN and volume_m > 0.1:
									volume_m -= 0.1
									window.blit(tela_mudar, (0, 0))
									window.blit(text_som, (0, 0))
									window.blit(text_musica, (30, 50))
									window.blit(text_vol_s, (220, 100))
									window.blit(text_efeitos, (30, 100))
									window.blit(text_tela, (0, 150))
									window.blit(text_cheia, (30, 200))
									window.blit(text_controles, (0, 250))
									window.blit(text_jogador1, (30, 300))
									window.blit(text_jogador2, (30, 350))
									if tela_cheia:
										window.blit(conf, (250, 200))
									else:
										window.blit(cancel, (250, 200))
									if escolha1 == "keyboard":
										window.blit(keyboard_img, (210, 280))
									else:
										window.blit(joystick_img, (210, 280))
									if escolha2 == "keyboard":
										window.blit(keyboard_img, (210, 330))
									else:
										window.blit(joystick_img, (210, 330))
									window.blit(gollum, gollum_cords)
									text_vol = font.render("%.1f" % volume_m, True, (0, 0, 0))
									window.blit(text_vol, (220, 50))
									pygame.display.update()
								elif event.key == K_UP and volume_m <= 1.0:
									volume_m += 0.1
									window.blit(tela_mudar, (0, 0))
									window.blit(text_som, (0, 0))
									window.blit(text_musica, (30, 50))
									window.blit(text_vol_s, (220, 100))
									window.blit(text_efeitos, (30, 100))
									window.blit(text_tela, (0, 150))
									window.blit(text_cheia, (30, 200))
									window.blit(text_controles, (0, 250))
									window.blit(text_jogador1, (30, 300))
									window.blit(text_jogador2, (30, 350))
									if tela_cheia:
										window.blit(conf, (250, 200))
									else:
										window.blit(cancel, (250, 200))
									if escolha1 == "keyboard":
										window.blit(keyboard_img, (210, 280))
									else:
										window.blit(joystick_img, (210, 280))
									if escolha2 == "keyboard":
										window.blit(keyboard_img, (210, 330))
									else:
										window.blit(joystick_img, (210, 330))
									window.blit(gollum, gollum_cords)
									window.blit(gollum, gollum_cords)
									text_vol = font.render("%.1f" % volume_m, True, (0, 0, 0))
									window.blit(text_vol, (220, 50))
									pygame.display.update()
						if sair: break
				elif event.key == confirm and muda == "jogador 1":
					sair = False
					while True:
						for event in pygame.event.get():
							if event.type == QUIT:
								pygame.quit()
								exit()
							if event.type == pygame.KEYDOWN:
								if event.key == K_ESCAPE:
									pygame.quit()
									exit()
								if event.key == back:
									sair = True
									break
								elif event.key == K_RIGHT:
									window.blit(tela_mudar, (0, 0))
									window.blit(text_vol, (220, 50))
									window.blit(text_vol_s, (220, 100))
									window.blit(text_som, (0, 0))
									window.blit(text_musica, (30, 50))
									window.blit(text_efeitos, (30, 100))
									window.blit(text_tela, (0, 150))
									window.blit(text_cheia, (30, 200))
									window.blit(text_controles, (0, 250))
									window.blit(text_jogador1, (30, 300))
									window.blit(text_jogador2, (30, 350))
									window.blit(joystick_img, (210, 280))
									if tela_cheia:
										window.blit(conf, (250, 200))
									else:
										window.blit(cancel, (250, 200))
									if escolha2 == "keyboard":
										window.blit(keyboard_img, (210, 330))
									else:
										window.blit(joystick_img, (210, 330))
									window.blit(gollum, gollum_cords)
									pygame.display.update
									escolha1 = "joystick"
								elif event.key == K_LEFT:
									window.blit(tela_mudar, (0, 0))
									window.blit(text_vol, (220, 50))
									window.blit(text_vol_s, (220, 100))
									window.blit(text_som, (0, 0))
									window.blit(text_musica, (30, 50))
									window.blit(text_efeitos, (30, 100))
									window.blit(text_tela, (0, 150))
									window.blit(text_cheia, (30, 200))
									window.blit(text_controles, (0, 250))
									window.blit(text_jogador1, (30, 300))
									window.blit(text_jogador2, (30, 350))
									window.blit(keyboard_img, (210, 280))
									if tela_cheia:
										window.blit(conf, (250, 200))
									else:
										window.blit(cancel, (250, 200))
									if escolha2 == "keyboard":
										window.blit(keyboard_img, (210, 330))
									else:
										window.blit(joystick_img, (210, 330))
									window.blit(gollum, gollum_cords)
									pygame.display.update
									escolha1 = "keyboard"
						if sair: break
						pygame.display.update()
				elif event.key == confirm and muda == "jogador 2":
					sair = False
					while True:
						for event in pygame.event.get():
							if event.type == QUIT:
								pygame.quit()
								exit()
							if event.type == pygame.KEYDOWN:
								if event.key == K_ESCAPE:
									pygame.quit()
									exit()
								if event.key == back:
									sair = True
									break
								elif event.key == K_RIGHT:
									window.blit(tela_mudar, (0, 0))
									window.blit(text_vol, (220, 50))
									window.blit(text_vol_s, (220, 100))
									window.blit(text_som, (0, 0))
									window.blit(text_musica, (30, 50))
									window.blit(text_efeitos, (30, 100))
									window.blit(text_tela, (0, 150))
									window.blit(text_cheia, (30, 200))
									window.blit(text_controles, (0, 250))
									window.blit(text_jogador1, (30, 300))
									window.blit(text_jogador2, (30, 350))
									window.blit(joystick_img, (210, 330))
									if tela_cheia:
										window.blit(conf, (250, 200))
									else:
										window.blit(cancel, (250, 200))
									if escolha1 == "keyboard":
										window.blit(keyboard_img, (210, 280))
									else:
										window.blit(joystick_img, (210, 280))
									window.blit(gollum, gollum_cords)
									pygame.display.update
									escolha2 = "joystick"
								elif event.key == K_LEFT:
									window.blit(tela_mudar, (0, 0))
									window.blit(text_vol, (220, 50))
									window.blit(text_vol_s, (220, 100))
									window.blit(text_som, (0, 0))
									window.blit(text_musica, (30, 50))
									window.blit(text_efeitos, (30, 100))
									window.blit(text_tela, (0, 150))
									window.blit(text_cheia, (30, 200))
									window.blit(text_controles, (0, 250))
									window.blit(text_jogador1, (30, 300))
									window.blit(text_jogador2, (30, 350))
									window.blit(keyboard_img, (210, 330))
									if tela_cheia:
										window.blit(conf, (250, 200))
									else:
										window.blit(cancel, (250, 200))
									if escolha1 == "keyboard":
										window.blit(keyboard_img, (210, 280))
									else:
										window.blit(joystick_img, (210, 280))
									window.blit(gollum, gollum_cords)
									pygame.display.update
									escolha2 = "keyboard"
						if sair: break
						pygame.display.update()
				elif event.key == pygame.K_DOWN and muda == "musica":
					gollum_cords = (4,100)
					muda = "efeitos"
				elif event.key == pygame.K_DOWN and muda == "efeitos":
					gollum_cords = (4, 200)
					muda = "tela cheia"
				elif event.key == pygame.K_DOWN and muda == "tela cheia":
					gollum_cords = (4, 300)
					muda = "jogador 1"
				elif event.key == pygame.K_DOWN and muda == "jogador 1":
					gollum_cords = (4, 350)
					muda = "jogador 2"
				elif event.key == pygame.K_UP and muda == "jogador 2":
					gollum_cords = (4, 300)
					muda = "jogador 1"
				elif event.key == pygame.K_UP and muda == "jogador 1":
					gollum_cords = (4, 200)
					muda = "tela cheia"
				elif event.key == pygame.K_UP and muda == "tela cheia":
					gollum_cords = (4, 100)
					muda = "efeitos"
				elif event.key == pygame.K_UP and muda == "efeitos":
					gollum_cords = (4, 50)
					muda = "musica"
# =========================================================================================
# Loop principal

def reinicia_jogo():

	global frodo 
	global aragorn 
	global legolas 
	global gandalf
	global gimli 
	global orc
	global haradrim 
	global uruk 
	global saruman 
	global wraith 
	global Team1
	global Team2

	for i in range (len(Team1)):
		Team1.pop()
	for i in range (len(Team2)):
		Team2.pop()

	pygame.mixer.music.fadeout(1000)
	pygame.mixer.music.load("sons/menu.mp3")
	pygame.mixer.music.play(-1, 0.0)

	frodo = Frodo()
	aragorn = Aragorn()
	legolas = Legolas()
	gandalf = Gandalf()
	gimli = Gimli()
	orc = Orc()
	haradrim = Haradrim()
	uruk = Urukhai()
	saruman = Saruman()
	wraith = Wraith()

	cursor = Cursor()
	cursor_ativado = True

	up = pygame.K_UP
	down = pygame.K_DOWN
	right = pygame.K_RIGHT
	left = pygame.K_LEFT
	confirm = pygame.K_z
	back = pygame.K_x

	Team1.append(gandalf)
	Team1.append(aragorn)
	Team1.append(legolas)
	Team1.append(gimli)
	Team1.append(frodo)
	Team2.append(haradrim)
	Team2.append(uruk)
	Team2.append(orc)
	Team2.append(saruman)
	Team2.append(wraith)

	main_menu()



def game_loop():
	while True:
		v = turnos()
		restaura_movimento()
		if v == "v1":
			print "Frodo jogou o anel no vulcão!"
		if v == "v2":
			print "Os orcs mataram Frodo!"
	
# Main
os.system('clear')
width, hight = 800, 736
white  = (0,0,0)
other = (0, 100, 0)
volume_m = 1.0
volume_s = 1.0
tela_cheia = False
escolha1 = "keyboard"
escolha2 = "keyboard"
pygame.init()
pygame.joystick.init()
pygame.mixer.init()

gollum = pygame.image.load("imagens/personagens/gollum.gif")

vulcao = pygame.image.load("imagens/mapa/volcano.png")
wall = pygame.image.load("imagens/mapa/wall.png")
wall1 = pygame.image.load("imagens/mapa/wall1.png")
statue1 = pygame.image.load("imagens/mapa/statue1.png")
corner = pygame.image.load("imagens/mapa/corner.png")
wall3 = pygame.image.load("imagens/mapa/wall3.png")
walll = pygame.image.load("imagens/mapa/wall3.png")

arvore1 = pygame.image.load("imagens/mapa/arvore.png")
arvore2 = pygame.image.load("imagens/mapa/arvore2.png")
arvore3 = pygame.image.load("imagens/mapa/arvore3.png")
arvore4 = pygame.image.load("imagens/mapa/arvore2.png")
arvore5 = pygame.image.load("imagens/mapa/arvore3.png")
arvore6 = pygame.image.load("imagens/mapa/arvore.png")
arvore7 = pygame.image.load("imagens/mapa/arvore2.png")
arvore8 = pygame.image.load("imagens/mapa/arvore2.png")
arvore9 = pygame.image.load("imagens/mapa/arvoremordor2.png")

img_win1 = pygame.image.load("imagens/telas/win1.jpg")
img_win2 = pygame.image.load("imagens/telas/win2.jpg")
tela_menu = pygame.image.load("imagens/menu/menu.jpg")
tela_instrucoes = pygame.image.load("imagens/menu/instrucoes.jpg")
tela_creditos = pygame.image.load("imagens/menu/creditos.jpg")
tela_mudar = pygame.image.load("imagens/menu/opcoes.jpg")
HUD = pygame.image.load("imagens/telas/hud.png")
separador = pygame.image.load("imagens/telas/separador.png")
conf = pygame.image.load("imagens/opcoes/conf.png")
cancel = pygame.image.load("imagens/opcoes/cancel.png")
joystick_img = pygame.image.load("imagens/opcoes/joystick.png")
keyboard_img = pygame.image.load("imagens/opcoes/keyboard.png")

# sons
menu_music = pygame.mixer.music.load("sons/menu.mp3")

window = pygame.display.set_mode((width, hight))
mapa_img = pygame.image.load("imagens/mapa/TERRAMEDIA.png")
pygame.display.set_caption('THE LORD OF PYGAMES')
window.blit(mapa_img, (0, 0))

mapa = matriz_espacos(20, 25)
blocos = [(16,0),
	 (16,1),
	 (16,3),
	 (16,4),
	 (16,5),
	 (17,5),
	 (18,5),
	 (19,5),
	 (20,5),
	 (22,5),
	 (23,5),
	 (24,5),
	 (4,4),
	 (5,4),
	 (9,6),
	 (13,9),
	 (16,9),
	 (17,9),
	 (9,11),
	 (2,14),
	 (14,15),
	 (15,15),
	 (18,16),
	 (14,17)]

bota_blocos_em_matriz(mapa, blocos)

frodo = Frodo()
aragorn = Aragorn()
legolas = Legolas()
gandalf = Gandalf()
gimli = Gimli()
orc = Orc()
haradrim = Haradrim()
uruk = Urukhai()
saruman = Saruman()
wraith = Wraith()

cursor = Cursor()
cursor_ativado = True

up = pygame.K_UP
down = pygame.K_DOWN
right = pygame.K_RIGHT
left = pygame.K_LEFT
confirm = pygame.K_z
back = pygame.K_x
Team1 = [gandalf, aragorn, legolas, gimli, frodo]
Team2 = [wraith, uruk, orc, saruman, haradrim]

main_menu()

posicao_randomica()
atualiza_mapa()
pygame.display.flip()
game_loop()
