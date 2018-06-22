import pygame

     

    # UEberpruefen, ob die optionalen Text- und Sound-Module geladen werden konnten.

if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')

if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')

def main():
# Initialisieren aller Pygame-Module und    
# Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repraesentiert).
	pygame.init()
	screen = pygame.display.set_mode((1080, 920))
# Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendruecke wiederholt senden.
	pygame.display.set_caption("Pygame-Tutorial: Grundlagen")
	pygame.mouse.set_visible(1)
	pygame.key.set_repeat(1, 30)
# Clock-Objekt erstellen, das wir benoetigen, um die Framerate zu begrenzen.
	clock = pygame.time.Clock()
# Die Schleife, und damit unser Spiel, laeuft solange running == True.
	running = True

	while running:
# Framerate auf 30 Frames pro Sekunde beschraenken.# Pygame wartet, falls das Programm schneller laeuft.
		clock.tick(30)
# screen-Surface mit Schwarz (RGB = 0, 0, 0) fuellen.
		screen.fill((0, 0, 0))
# Alle aufgelaufenen Events holen und abarbeiten.
		for event in pygame.event.get():
# Spiel beenden, wenn wir ein QUIT-Event finden.
			if event.type == pygame.QUIT:
				running = False
# Wir interessieren uns auch fuer "Taste gedrueckt"-Events.
			if event.type == pygame.KEYDOWN:
# Wenn Escape gedrueckt wird, posten wir ein QUIT-Event in Pygames Event-Warteschlange.
				if event.key == pygame.K_ESCAPE:
					pygame.event.post(pygame.event.Event(pygame.QUIT))
# Inhalt von screen anzeigen.
		pygame.display.flip()

 # Ueberpruefen, ob dieses Modul als Programm laeuft und nicht in einem anderen Modul importiert wird.

if __name__ == '__main__':

        # Unsere Main-Funktion aufrufen.
	main()
