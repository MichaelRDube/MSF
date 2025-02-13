#code for monster panels
import pygame
class Monster_Panel:
    
    def __init__(self, screen, monster, location, dimension, height=True):
        
        self.screen = screen
        self.monster = monster
        
        self.location = [0, 0]
        self.p_location = [0, 0]
        
        self.dimensions = [0, 0]
        self.p_dimensions = [0, 0]
        
        if height:
            self.dimensions= [int(.5*dimension), dimension]
        else:
            self.dimensions = [dimension, 2*dimension]
            
        self.bg_color = (211, 211, 211)
        
    def render(self):
        pygame.draw.rect(self.screen, self.bg_color, [self.location[0], self.location[1], self.dimensions[0], self.dimensions[1]])