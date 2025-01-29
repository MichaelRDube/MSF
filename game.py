#put game stuff here
import pygame
import time
import sys
from monsters.goblin import Goblin
class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.last_update = pygame.time.get_ticks()
        
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
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # Check for quit event
                        pygame.quit()
                        sys.exit()

                now = pygame.time.get_ticks()
                time_elapsed = (now-self.last_update)/1000
                self.last_update = now
                
                self.current_cpu_monster.run(time_elapsed)
                self.current_player_monster.run(time_elapsed)

                self.clock.tick(60)
                self.render()

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

        goblin = Goblin(self.screen)
        goblin.name = "Player Goblin 1"
        goblin.set_position([50, 275])
        self.player_monsters.append(goblin)

        goblin = Goblin(self.screen)
        goblin.name = "Player Goblin 2"
        goblin.set_position([50, 275])
        self.player_monsters.append(goblin)

        goblin = Goblin(self.screen)
        goblin.name = "Player Goblin 3"
        goblin.set_position([50, 275])
        self.player_monsters.append(goblin)

        goblin = Goblin(self.screen)
        goblin.name = "CPU Mega Goblin"
        goblin.set_position([550, 275])
        goblin.speed = 1.8
        goblin.health_max = 500
        goblin.health_current = 500
        self.cpu_monsters.append(goblin)

    def render(self):
        self.screen.fill((255, 255, 255))

        self.current_cpu_monster.render()
        self.current_player_monster.render()

        pygame.display.flip()