import random
import json

name = json.loads(open('fantasyNameList.json').read())
race = json.loads(open('racesDnd.json').read())
charClass = json.loads(open('classesDnd.json').read())

rollName = int(random.randint(0,len(name)-1))
rollSurname = int(random.randint(0,len(name)-1))
rollRace = int(random.randint(0,len(race)-1))
rollClass = int(random.randint(0,len(charClass)-1))

print(str("\nA ")+str(race[rollRace])+str(" ")+str(charClass[rollClass])+str(" named ")+str(name[rollName])+str(" ")+str(name[rollSurname])+str(" "))