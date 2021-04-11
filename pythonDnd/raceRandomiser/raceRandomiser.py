import random
import json



race = json.loads(open('racesDnd.json').read())
rollRace = int(random.randint(0,len(race)-1))

print(race[rollRace])
