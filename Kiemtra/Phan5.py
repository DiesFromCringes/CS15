import random
while True:
    score = 0
    a = random.randint(5, 10)
    b = random.randint(1, 2)
    a2 = random.randint(5, 10)
    b2 = random.randint(1, 2 )
    list_str = [f'{a} / {b} < 0', f'{a} * {b} = 1', f'{a} + {b} < 0', f'{a2} - {b2} =  0']
    def randomSkill(list_skill):
        return random.choice(list_skill)
    machineInput = randomSkill(list_str)
    print(machineInput)
    userInput = int(input('Answer '))
    if userInput == 0:
        score = score + 1 