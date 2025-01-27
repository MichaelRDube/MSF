#Put monster superclass stuff here
import threading
import time
import pygame
class Monster:
    def __init__(self):
        
        self.name
        self.health
        self.strength
        self.speed
        self.life_steal
        self.resistance
        
        self.item
        
        #start thread
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()
        
    def run(self):
        #to be overridden by child class
        #general upkeep function
        return
        
    def calculate_attack(self):
        #to be overridden by child class
        #calculate raw damage number here
        return
    
    def attack(self):
        #to be overridden by child class
        #apply on-attack effects
        #send raw damage number to opponent
        return
    
    def receive_attack(self):
        #to be overridden by child class
        #apply on-defend effects
        #apply resistances
        return
    
    def apply_damage(self):
        #to be overridden by child class
        #apply damage
        #apply on-damage effects
        return
    
    def die(self):
        print(f"{self.name} has died.")
    