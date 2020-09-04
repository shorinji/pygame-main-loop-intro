# Example code applying the structure from Readme.md
# Displays a circle that the player can move using arrow keys
import pygame
import sys
from pygame.locals import *

# "constants"
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
FRAME_DELAY = 100

PLAYER_COLOR = (255, 200, 200)
PLAYER_CIRCLE_RADIUS = 50
PLAYER_MOVE_SPEED = 5

# initial game state
done = False
dx, dy = 0, 0
playerX, playerY = 400, 300

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])


while not done:
	# stage 1 - handle events
	for event in pygame.event.get():
		if event.type == QUIT:
			done = True
		if event.type == KEYDOWN and event.key == K_ESCAPE:
			done = True

	keys = pygame.key.get_pressed()

	# stage 2 - run game logic

	if keys[K_LEFT]:
		dx = -PLAYER_MOVE_SPEED
	elif keys[K_RIGHT]:
		dx = PLAYER_MOVE_SPEED
	else:
		dx = 0

	if keys[K_DOWN]:
		dy = PLAYER_MOVE_SPEED
	elif keys[K_UP]:
		dy = -PLAYER_MOVE_SPEED
	else:
		dy = 0

	playerX = (playerX + dx) % WIDTH
	playerY = (playerY + dy) % HEIGHT

	# stage 3 - display graphics
	screen.fill(BACKGROUND_COLOR)
	
	pygame.draw.circle(screen, PLAYER_COLOR, (playerX, playerY), PLAYER_CIRCLE_RADIUS)

	pygame.display.flip()
	pygame.time.wait(FRAME_DELAY)
