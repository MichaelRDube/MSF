#put game stuff here
import pygame
import time
from monsters.goblin import Goblin
class Game:
    def __init__(self):
        self.update_interval = .0167
        
        self.cpu_monsters = []
        self.player_monsters = []
        
        print(f"New game started!!")

        self.pick_phase()

        self.current_cpu_monster = self.cpu_monsters[0]
        self.current_player_monster = self.player_monsters[0]

        self.current_cpu_monster.target = self.current_player_monster
        self.current_player_monster.target = self.current_cpu_monster
        
    def run_game(self):
        while self.cpu_monsters and self.player_monsters:
            while self.current_cpu_monster.alive and self.current_player_monster.alive:
        
                time.sleep(self.update_interval)
                self.current_cpu_monster.run(self.update_interval)
                self.current_player_monster.run(self.update_interval)

            if not self.current_cpu_monster.alive:
                #remove monster from team
                self.cpu_monsters.remove(self.current_cpu_monster)
                if self.cpu_monsters:
                    #replace monster
                    self.current_cpu_monster = self.cpu_monsters[0]

                    #update monster targets
                    self.current_cpu_monster.target = self.current_player_monster
                    self.current_player_monster.target = self.current_cpu_monster

            if not self.current_player_monster.alive:
                #remove monster from team
                self.player_monsters.remove(self.current_player_monster)
                if self.player_monsters:
                    #replace monster
                    self.current_player_monster = self.player_monsters[0]

                    #update monster targets
                    self.current_cpu_monster.target = self.current_player_monster
                    self.current_player_monster.target = self.current_cpu_monster

        if self.cpu_monsters:
            print(f"Computer is victorious!")
            
        elif self.player_monsters:
            print(f"Player is victorious!")
            
        else:
            print(f"Tie!")

    def pick_phase(self):
        self.player_monsters = []
        self.cpu_monsters = []

        goblin = Goblin()
        goblin.name = "Player Goblin 1"
        self.player_monsters.append(goblin)

        goblin = Goblin()
        goblin.name = "Player Goblin 2"
        self.player_monsters.append(goblin)

        goblin = Goblin()
        goblin.name = "Player Goblin 3"
        self.player_monsters.append(goblin)

        goblin = Goblin()
        goblin.name = "CPU Mega Goblin"
        goblin.speed = 1.8
        goblin.health_max = 500
        goblin.health_current = 500
        self.cpu_monsters.append(goblin)