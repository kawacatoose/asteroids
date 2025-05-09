# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt=0
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return    			
			
		updatable.update(dt)

		for asteroid in asteroids:
			if player.collides_with(asteroid) == True:
				sys.exit("Game Over!")
			for shot in shots:
				if shot.collides_with(asteroid):
					shot.kill()
					asteroid.split()



		screen.fill(("black"))

		for object in drawable:
			object.draw(screen)
		
		pygame.display.flip()

		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
