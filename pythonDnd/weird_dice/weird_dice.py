
class Weird_Dice:
    
    def roll_dice(input: str) -> tuple:
        dice = Weird_Dice.parse_command(input=input)
        num, sided = dice[0], dice[1]
        
        import random
        total = 0
        individuals = []
        for _ in range(num):
            random.seed()
            outcome = random.randint(1, sided)
            total += outcome
            individuals.append(outcome)
        
        res = f"Rolling {num}d{sided}\nTotal: {total}\nRolls: {individuals}\n"
        print(res)
        
    def parse_command(input: str) -> tuple:
        import re
        pattern = r'\D'
        pattern = re.sub(pattern, " ", input)
        pattern = pattern.split(" ")
        numbers = [int(x) for x in pattern if x]
        if len(numbers) > 2:
            print ("Parsing Error")
            return
        return numbers
        
if __name__ == "__main__":
    user_input = input("Enter your dice roll as NumdSides: ")
    res = Weird_Dice.roll_dice(user_input)
