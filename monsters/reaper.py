import pygame
from monster import Monster

class Reaper(Monster):
    
    def __init__(self, screen):
        super().__init__(screen)
        
        self.name = "Reaper"
        self.health_max = 210
        self.health_current = self.health_max
        self.strength = 1
        self.true_strength = 1
        self.speed = 12
        self.progress = 0
        self.life_steal = 0
        self.resistance = 3
        
    def run(self, time):
        
        self.progress += time
        
        if self.progress >= self.speed:
            self.progress = self.progress%self.speed
            self.touch_of_death()
        
    def calculate_attack(self):
        #calculate raw damage number here
        self.attack(self.strength, self.true_strength)
        
    def touch_of_death(self):
        #insta-kill target
        print(f"{self.name} touches {self.target.name} with death!")
        self.target.health_current = 0
        self.target.die()
    
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