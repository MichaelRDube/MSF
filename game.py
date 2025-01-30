#put game stuff here
import pygame
import time
import sys
from monsters.goblin import Goblin
from monsters.spike import Spike
from monsters.speed_demon import Speed_Demon
from monsters.ghost import Ghost
from monsters.vampire import Vampire

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

        vampire = Vampire(self.screen)
        vampire.name = "Player Vampire"
        vampire.set_position([50, 275])
        self.player_monsters.append(vampire)

        spike = Spike(self.screen)
        spike.name = "Player Spike"
        spike.set_position([50, 275])
        self.player_monsters.append(spike)

        goblin = Goblin(self.screen)
        goblin.name = "Player Goblin"
        goblin.set_position([50, 275])
        self.player_monsters.append(goblin)

        goblin = Goblin(self.screen)
        goblin.name = "CPU Goblin"
        goblin.set_position([550, 275])
        self.cpu_monsters.append(goblin)

        speed_demon = Speed_Demon(self.screen)
        speed_demon.name = "CPU Speed Demon"
        speed_demon.set_position([550, 275])
        self.cpu_monsters.append(speed_demon)
        
        ghost = Ghost(self.screen)
        ghost.name = "CPU Ghost"
        ghost.set_position([550, 275])
        self.cpu_monsters.append(ghost)

    def render(self):
        self.screen.fill((255, 255, 255))

        self.current_cpu_monster.render()
        self.current_player_monster.render()

        pygame.display.flip()