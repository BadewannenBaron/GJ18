# -*- coding: UTF-8 -*-

# Pygame Modul importieren.
import pygame
import Background
import Player
import enemy as E
from random import randint
import Bucket
# Unser Tilemap Modul
#import Tilemap

# Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.
if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')
if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')

def main():
	counter2 = 0
	counter3 = 0
	enemy = []
	# Initialisieren aller Pygame-Module und 
	# Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
	pygame.init()
	pygame.font.init()
	myfont = pygame.font.SysFont('Comic Sans MS', 30)
	screen = pygame.display.set_mode((1366, 768))
	
	# Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.
	pygame.display.set_caption("Pygame-Tutorial: Animation")
	#pygame.mofrom random import randintuse.set_visible(1)
	pygame.key.set_repeat(1, 30)

	# Clock-Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.
	clock = pygame.time.Clock()
	
	# Wir erstellen eine Tilemap.
	#map = Tilemap.Tilemap()
	ranen = randint(0, 5)
	player = Player.Player()
	bucket = Bucket.bucket()
	for ene in range(ranen):
		enemy.append(E.Enemy())
	# Die Schleife, und damit unser Spiel, läuft solange running == True.
	BackGround = Background.Background('images/Background.png', [0,0])
	running = True
	count = 0
	while running:
		# Framerate auf 30 Frames pro Sekunde beschränken.
		clock.tick(30)
		count += 1
		if (count == 15):
			count = 0
			ranen = randint(0, 5)
			for ene in range(1):
				enemy.append(E.Enemy())
		# Pygame wartet, falls das Programm schneller läuft.
		for j in enemy: 
			j.falldown()
		# screen Surface mit Schwarz (RGB = 0, 0, 0) füllen.
		screen.fill([255, 255, 255])
		screen.blit(BackGround.image, BackGround.rect)

		# Alle aufgelaufenen Events holen und abarbeiten.
		for event in pygame.event.get():
			# Spiel beenden, wenn wir ein QUIT-Event finden.
			if event.type == pygame.QUIT:
				running = False
			
			# Wir interessieren uns auch für "Taste gedrückt"-Events.
			if event.type == pygame.KEYDOWN:
				# Wenn Escape gedrückt wird posten wir ein QUIT-Event in Pygames Event-Warteschlange.
				if event.key == pygame.K_ESCAPE:
					pygame.event.post(pygame.event.Event(pygame.QUIT))
				
				# Alle Tastendrücke auch der Tilemap mitteilen.
				player.handle_input(event.key)
				bucket.handle_input(event.key)
				
		
		player.render(screen)
		bucket.render(screen)
		for i in enemy: 	
			i.render(screen)
		xbuck, ybuck = bucket.update()
		for n in enemy:
			x, y = n.update()
			xbuck, ybuck = bucket.update()
			if ((y >= (ybuck - 56)) and (x >= xbuck - 64 )and (x <= (xbuck + 32))):
				counter2 += 1
				enemy.remove(n)
			textsurface = myfont.render('Punkte:'+ str(counter2) , False, (0, 0, 0))
			screen.blit(textsurface,(0,0))
			if (y >= 800):
				counter3 += 1
				enemy.remove(n)
			if (counter3 >=25):
				screen.fill([255, 255, 255])
				textsurface = myfont.render('WE ALL GONNA DIE' ,False, (0, 0, 0))
				


			
		# Die Tilemap auf die screen-Surface rendern.
		#map.render(screen)
		
		# Inhalt von screen anzeigen
		pygame.display.flip()


# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.
if __name__ == '__main__':
	# Unsere Main-Funktion aufrufen.
	main()
