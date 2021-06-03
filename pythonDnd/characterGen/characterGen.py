import random
import json

name = json.loads(open('pythonDnd/characterGen/fantasyNameList.json').read())
race = json.loads(open('pythonDnd/characterGen/racesDnd.json').read())
charClass = json.loads(open('pythonDnd/characterGen/classesDnd.json').read())

rollName = int(random.randint(0,len(name)-1))
rollSurname = int(random.randint(0,len(name)-1))
rollRace = int(random.randint(0,len(race)-1))
rollClass = int(random.randint(0,len(charClass)-1))

# def charGen(race, charClass, name, surname):
    

print(str("\nA ")+str(race[rollRace])+str(" ")+str(charClass[rollClass])+str(" named ")+str(name[rollName])+str(" ")+str(name[rollSurname])+str(" "))