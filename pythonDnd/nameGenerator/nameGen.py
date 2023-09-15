import random
import json

name = json.loads(open('fantasyNameList.json').read())

rollName = int(random.randint(0,len(name)-1))
rollSurname = int(random.randint(0,len(name)-1))

print(str("\nYour name is: ")+str(name[rollName])+str(" ")+str(name[rollSurname]))