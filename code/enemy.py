# -*- coding: UTF-8 -*-

import pygame
import Utils
import Animation
from random import randint


# Die Player Klasse verwendet zwei Animationen, um eine steuerbare66666 Spielfigur dazustellen.
class Enemy(object):
		def __init__(self):
				pic = randint(0, 9)
				
				if (pic == 0 or pic == 1 or pic == 2):
					self.anim_image_left = Utils.load_image("images/Bachelor64.png", (0, 0, 0))
				elif (pic == 3 or pic == 4):
					self.anim_image_left = Utils.load_image("images/Aktenkoffer64.png", (0, 0, 0))
				elif (pic == 5):
					self.anim_image_left = Utils.load_image("images/Doktor64.png", (0, 0, 0))
				else:
					self.anim_image_left = Utils.load_image("images/Bomb64.png", (0, 0, 0))
				# Bild laden und erste Animation erstellen: 
				self.anim_left = Animation.Animation(self.anim_image_left, 0, 0, 1, 64, 64, 15)	
				
				# Die Grafik spiegeln und in einer neuen Surface speichern,
				# dann können wir die linke Animation erstellen.
				#self.anim_image_right= pygame.transform.flip(self.anim_image_left, True, False)
				#self.anim_right = Animation.Animation(self.anim_image_right, 0, 0, 1, 64, 124, 15)
				
				# Start-Position des Players festlegen und
				# merken in welche Richtung wir schauen und ob wir überhaupt laufen.
				self.pos_x = randint(0, 1366)
				self.pos_y = 3*32			
				self.dir = 0
				self.walking = False
				
				
		def render(self, screen):
				# Die Blickrichtung ist links:
				
						# Wenn der Spieler die linke oder rechte Pfeiltaste gedrückt hat sind wir am laufen,
													
								# nur dann die Animation updaten.
				self.anim_left.update()
						# Blickrichtung links rendern.
				self.anim_left.render(screen, (self.pos_x, self.pos_y))	 
			
				
				# De Laufen-Zustand zurücksetzen, im nächsten Frame bleiben wir stehen.
				self.walking = False

		def update(self):
			return self.pos_x, self.pos_y
		def falldown(self):
				self.pos_y+= 5
				self.dir = -1
				self.walking = True		
		
		def handle_input(self, key):
				# Linke Pfeiltaste wird gedrückt:
				if key == pygame.K_LEFT:
						# x-Position der Spielfigur anpassen,
						# die Blickrichtung festlegen
						# und den Laufen-Zustand einschalten.
						self.pos_x -= 5
						self.dir = -5
						self.walking = True
				'''if key == pygame.K_UP:
						# x-Position der Spielfigur anpassen,
						# die Blickrichtung festlegen
						# und den Laufen-Zustand einschalten.
						self.pos_y -= 1
						self.dir = -1
						self.walking = True'''
				
				# Und nochmal für die rechte Pfeiltaste.
				if key == pygame.K_RIGHT:
						self.pos_x += 5
						self.dir = 5
						self.walking = True
