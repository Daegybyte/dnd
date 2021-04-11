import random

party = ["Selsys", "Nestor", "Rafe", "Friday","Theodor","Sever"]
race = [
"Dragonborn",
"Dwarf",
"Elf",
"Gnome",
"Half-Elf",
"Halfling",
"Half-Orc",
"Human",
"Tiefling",
"Changeling",
"Kalashtar",
"Shifter",
"Warforged",
"Aarakocra",
"Genasi",
"Goliath",
"Centaur",
"Loxodon",
"Minotaur",
"Simic Hybrid",
"Vedalken",
"Aetherborn",
"Aven",
"Khenra",
"Kor",
"Merfolk",
"Naga",
"Siren",
"Vampire",
"Aasimar",
"Bugbear",
"Firbolg",
"Goblin",
"Hobgoblin",
"Kenku",
"Kobold",
"Lizardfolk",
"Orc",
"Tabaxi",
"Triton",
"Yuan-ti Pureblood",
"Gith",
"Locathah",
"Tortle",
"Verdan "
]

rollRace = int(random.randint(0,len(race)-1))
rollParty = int(random.randint(0,len(party)-1))

print(str("\n")+str(party[rollParty])+str(" has been turned into a ")+str(race[rollRace])) 