#put program entry stuff here
from monsters.goblin import Goblin
from game import Game
import time

player_team = []
cpu_team = []

goblin = Goblin()
goblin.name = "Player Goblin 1"
player_team.append(goblin)

goblin = Goblin()
goblin.name = "Player Goblin 2"
player_team.append(goblin)

goblin = Goblin()
goblin.name = "Player Goblin 3"
player_team.append(goblin)

goblin = Goblin()
goblin.name = "CPU Mega Goblin"
goblin.speed = 1.8
goblin.health_max = 500
goblin.health_current = 500
cpu_team.append(goblin)

game = Game(player_team, cpu_team)

game.run_game()
