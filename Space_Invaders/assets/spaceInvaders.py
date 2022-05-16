import pygame
import os
import time
import random
pygame.font.init()

#set height and width to run program
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#set the caption or name of our window
pygame.display.set_caption("Space Shooter Tutorial")

# Load images
redSpaceShip = pygame.image.load(os.path.join("Space_Invaders", "assets", "pixel_ship_red_small.png"))
greenSpaceShip = pygame.image.load(os.path.join("Space_Invaders", "assets", "pixel_ship_green_small.png")) 
blueSpaceShip = pygame.image.load(os.path.join("Space_Invaders", "assets", "pixel_ship_blue_small.png")) 

#Load Player ship
yellowSpaceShip = pygame.image.load(os.path.join("Space_Invaders", "assets", "pixel_ship_yellow.png")) 

#Load Lazers
redLaser = pygame.image.load(os.path.join("Space_Invaders", "assets", "pixel_laser_red.png"))
greenLaser = pygame.image.load(os.path.join("Space_Invaders", "assets", "pixel_laser_green.png"))
blueLaser = pygame.image.load(os.path.join("Space_Invaders", "assets", "pixel_laser_blue.png"))
yellowLaser = pygame.image.load(os.path.join("Space_Invaders", "assets", "pixel_laser_yellow.png"))

#Load Background (transform.scale) scales BBG to WIDTH and HEIGHT parameters
BBG = pygame.transform.scale(pygame.image.load(os.path.join("Space_Invaders", "assets", "background-black.png")), (WIDTH, HEIGHT))

class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.coolDownCounter = 0
    
    def draw(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y, 50, 50), 0)
        window.blit(self.ship_img (self.x, self.y))

def main():
    run = True
    FPS = 30
    level = 1
    lives = 3
    clock = pygame.time.Clock()
    #create a font
    mainFont = pygame.font.SysFont("comicsans", 50)
    playerVel = 5
    ship = Ship(300, 650)

    def redrawWindow():            
        # blit takes an image(surface) and draws at location defined
        WIN.blit(BBG, (0,0))
        # draw text
        livesLabel = mainFont.render(f"Lives: {lives}", 1, (255,255,255))
        levelLabel = mainFont.render(f"Level: {level}", 1, (255,255,255))
        #barely offset lives label but level label on the right
        WIN.blit(livesLabel, (10, 10))
        WIN.blit(levelLabel, (WIDTH - levelLabel.get_width() - 10, 10))
        
        ship.draw(WIN)

        # (255,255,255) is all white [search up color codes]
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redrawWindow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and ship.x - playerVel - 0: # left
            ship.x -= playerVel
        if keys[pygame.K_d] and ship.x + playerVel + 50 < WIDTH: # right
            ship.x += playerVel
        if keys[pygame.K_w] and ship.y - playerVel > 0: # up
            ship.y -= playerVel
        if keys[pygame.K_s] and ship.y + playerVel + 50 < HEIGHT: # down
            ship.y += playerVel

main()
#CALL YOUR FUNCTIONS