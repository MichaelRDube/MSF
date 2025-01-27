#put program entry stuff here
from monsters.goblin import Goblin

gob1 = Goblin()
gob1.name = "Hee hee boy"

gob2 = Goblin()
gob2.name = "Bad little man"

gob1.target = gob2
gob2.target = gob1

while gob1.health_current > 0 and gob2.health_current > 0:
    continue

if gob1.health_current <= 0:
    print(f"{gob2.name} is victorious!")
    
else:
    print(f"{gob1.name} is victorious!")