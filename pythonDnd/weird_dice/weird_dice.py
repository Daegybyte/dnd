
class Sandbox:
    def do_it():
        raise NotImplementedError("method not implemented")
    
    def roll_dice(command: str) -> tuple:
        dice = Sandbox.parse_command(command=command)
        num, sided = dice[0], dice[1]
        # print(num, sided)
        
        import random
        total = 0
        individuals = []
        for _ in range(num):
            random.seed()
            outcome = random.randint(1, sided)
            total += outcome
            individuals.append(outcome)
        
        res = f"Total: {total}\n{individuals}\n"
        print(res)
        # return (total, individuals)

        
        
        
    def parse_command(command: str) -> tuple:
        import re
        pattern = r'\D'
        pattern = re.sub(pattern, " ", command)
        pattern = pattern.split(" ")
        numbers = [int(x) for x in pattern if x]
        if len(numbers) > 2:
            print ("Invalid input -- Parsing Error")
            return
        # print(numbers)
        return numbers
        
    
if __name__ == "__main__":
    s = Sandbox
    user_input = input()
    res = s.roll_dice(user_input)
