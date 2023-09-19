
class Weird_Dice:
    
    def roll_dice(input: str) -> tuple:
        dice = Weird_Dice.parse_command(input=input)
        num_dice, sides = dice[0], dice[1]
        
        import random
        rolls = []
        for _ in range(num_dice):
            random.seed()
            outcome = random.randint(1, sides)
            rolls.append(outcome)
                
        max = num_dice * sides
        min = num_dice
        d_range = max + min
        roll_sum = sum(rolls)
        avg =  d_range // 2
        out = f"Rolling {num_dice}d{sides}...\nMin:Max: {min}:{max}\nAverage: {avg}\n\nRoll(s): {rolls}\nTotal: {roll_sum}\n"
        print(out)        
        
    def parse_command(input: str = "1d20") -> tuple:
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
    import sys
    user_input = ""
    if len(sys.argv) < 2:
        user_input = "1d20"
    else:
        user_input = sys.argv[1]

Weird_Dice.roll_dice(user_input)