#Put monster superclass stuff here
import threading
import time
import pygame
class Monster:
    def __init__(self):
        
        self.name = ""
        self.health_max = 0
        self.health_current = 0
        self.strength = 0
        self.speed = 0
        self.progress = 0
        self.life_steal = 0
        self.resistance = 0
        self.target = None
        
        self.item = None
        
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
        print(f"{self.name} has died.")
        self.thread._stop()
        if self.target != None:
            self.target.get_kill()
        else:
            print("No target to award kill")
    
    def get_kill(self):
        #any effects that might happen when a monster gets a kill
        return