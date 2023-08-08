#this is everything before I start moving the bike, so screen set up is mostly done

import pygame #this is a graphics library to help animate the bike
import math

pygame.init() #initialize pygame


#PARAMETERS
INIT_VELOCITY = 20 #initial velocity of the bike in m/s
BIKE_MASS = 9 #mass of the bike in kg
PERSON_MASS = 58 #mass of the person in kg


SCALE = 1
TIMESTEP = 10 #10 seconds in simulation = 1 second in real life
WIDTH, HEIGHT = 800, 500 #set the width and height of the screen
GROUND_Y = 400 #height of the ground in pixels
RADIUS = 100 #height of the bike circle in pixels

#colors
GREEN = (0, 100, 0)
BACKGROUND = (255, 255, 240) #ivory

screen = pygame.display.set_mode((WIDTH, HEIGHT)) #set the screen
pygame.display.set_caption("Bike Simulation with Air Resistance") #set the title of the screen

class Bike:
    def __init__(self, x, y, velocity, mass):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.mass = mass
        self.time_elapsed = 0 #should stop incrementing when velocity = 0
        self.radius = RADIUS
        
        self.velocity_history = []  #[] means it's a list, roughly equivalent to an array


    def draw (self, screen):
        x = self.x * SCALE
        Y = self.y * SCALE
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.radius) #draw the bike as a circle


def main ():
    run = True
    clock = pygame.time.Clock() #to sync speed/regulate frame rate

    bike1 = Bike(100, GROUND_Y - RADIUS, INIT_VELOCITY, BIKE_MASS) #create a bike object

    while run:
        clock.tick(60) #60 frames per second
        screen.fill(BACKGROUND) #fill the screen with ivory
        pygame.draw.rect(screen, GREEN, pygame.Rect((0, GROUND_Y), (WIDTH, HEIGHT - GROUND_Y))) #draw the ground

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        bike1.draw(screen) #draw the bike

        pygame.display.update() #update the screen

    pygame.quit()


main()