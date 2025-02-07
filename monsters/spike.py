
import pygame
import math
from monster import Monster

class Spike(Monster):
    
    def __init__(self, screen):
        super().__init__(screen)
        
        self.name = "Spike Monster"
        self.health_max = 400
        self.health_current = self.health_max
        self.strength = 15
        self.true_strength = 0
        self.speed = 4
        self.progress = 0
        self.life_steal = 0
        self.resistance = 5
        
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
    
    def receive_attack(self, damage, true_damage):
        #apply on-defend effects
        #apply resistances
        damage -= self.resistance
        if damage+true_damage < 1:
            true_damage = 1
            
        self.reflect_damage(damage, true_damage)
        self.apply_damage(damage + true_damage)
        
    def reflect_damage(self, damage, true_damage):
        flat_reflect= 5
        percent_reflect = math.ceil(.07*(damage+true_damage))
        total_reflect = flat_reflect + percent_reflect
        
        print(f"{self.name} reflects {total_reflect} damage!")
        self.target.apply_damage(total_reflect)
        
    
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