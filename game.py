#put game stuff here
import pygame
import time
class Game:
    def __init__(self, player_team, cpu_team):
        self.update_interval = .0167
        
        print(f"New game started!!")

        self.cpu_monsters = cpu_team
        self.player_monsters = player_team

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