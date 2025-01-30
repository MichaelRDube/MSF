import pygame
import math
from monster import Monster

class Vampire(Monster):
    
    def __init__(self, screen):
        super().__init__(screen)
        
        self.name = "Vampire"
        self.health_max = 250
        self.health_current = self.health_max
        self.strength = 23
        self.true_strength = 0
        self.speed = 2
        self.progress = 0
        self.life_steal = .33
        self.resistance = 0
        
    def run(self, time):
        
        self.progress += time
        
        if self.progress >= self.speed:
            self.progress = self.progress%self.speed
            self.calculate_attack()
        
    def calculate_attack(self):
        #calculate raw damage number here
        self.attack(self.strength, self.true_strength)
    
    def attack(self, damage, true_damage):
        #apply on-attack effects
        #send raw damage number to opponent
        print(f"{self.name} attacks for {damage + true_damage} damage!")
        self.target.receive_attack(damage, true_damage)
        return
    
    def receive_attack(self, damage, true_damage):
        #apply on-defend effects
        #apply resistances
        self.apply_damage(damage + true_damage)
    
    def apply_damage(self, total_damage):
        #apply damage
        #apply on-damage effects
        self.health_current -= total_damage
        if self.health_current < 0:
            self.health_current = 0
            
        self.target.observe_damage(total_damage)
        print(f"{self.name} receives {total_damage} damage!")
        print(f"{self.name} has {self.health_current} health remaining.\n")

        if self.health_current <= 0:
            self.die()
            
    def observe_damage(self, dealt_damage):
        healing = int(math.ceil(self.life_steal*dealt_damage))
        self.health_current += healing
        if self.health_current > self.health_max:
            self.health_current = self.health_max
            
        print(f"{self.name} stole {healing} health from {self.target.name}!")
        print(f"{self.name} now with {self.health_current} health!")