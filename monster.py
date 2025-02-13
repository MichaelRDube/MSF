#Put monster superclass stuff here
import threading
import time
import pygame
import math
class Monster:
    def __init__(self, screen):
        
        self.screen = screen

        self.name = ""
        self.health_max = 0
        self.health_current = 0
        self.alive = True
        self.strength = 0
        self.true_strength = 0
        self.speed = 0
        self.progress = 0
        self.life_steal = 0
        self.resistance = 0
        self.target = None
        self.retreat = 0

        self.position = [0, 0]
        
        self.item = None
        
    def run(self, time):
        #to be overridden by child class
        #general upkeep function
        return
    
    def set_position(self, new_pos):
        self.position = new_pos
        
    def calculate_attack(self):
        #to be overridden by child class
        #calculate raw damage number here
        return
    
    def attack(self, damage, true_damage):
        #to be overridden by child class
        #apply on-attack effects
        #send raw damage number to opponent
        return
    
    def receive_attack(self, damage, true_damage):
        #to be overridden by child class
        #apply on-defend effects
        #apply resistances
        return
    
    def apply_damage(self, total_damage):
        #to be overridden by child class
        #apply damage
        #apply on-damage effects
        return
    
    def apply_special_damage(self, damage, true_damage):
        #to be overridden by child class
        #apply special, non-attack type damage (bleed, poison, reflect, etc)
        return
    
    def die(self):
        self.alive = False
        print(f"{self.name} has died.\n")
        if self.target != None:
            self.target.get_kill()
        else:
            print("No target to award kill")
    
    def get_kill(self):
        #any effects that might happen when a monster gets a kill
        return
    
    def observe_damage(self, dealt_damage):
        #So the monster can know how much damage was actually done to target
        #for healing purposes
        return
    
    def render(self):
        self.render_health()
        self.render_progress()
        #render monster sprite
    
    def render_health(self):
        pygame.draw.rect(self.screen, (0, 0, 0), [self.position[0], self.position[1], 200, 50])
        pygame.draw.rect(self.screen, (211, 211, 211), [self.position[0]+2, self.position[1]+2, 196, 46])
        health_length = int(196*self.health_current/self.health_max)
        pygame.draw.rect(self.screen, (90, 255, 90), [self.position[0]+2, self.position[1]+2, health_length, 46])
    
    def render_progress(self):
        pygame.draw.rect(self.screen, (0, 0, 0), [self.position[0], self.position[1]+55, 200, 50])
        pygame.draw.rect(self.screen, (211, 211, 211), [self.position[0]+2, self.position[1]+57, 196, 46])
        progress_length = int(196*self.progress/self.speed)
        pygame.draw.rect(self.screen, (150, 150, 255), [self.position[0]+2, self.position[1]+57, progress_length, 46])