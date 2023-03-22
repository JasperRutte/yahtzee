import random

def askUser(question: str, options: list) -> str:  # function for asking user questions
    while True:
        userInput = input(question).lower()
        if userInput in options:
            return userInput
        else:
            print("Sorry I didn't quite understood that...")


def rollDice(amount: int) -> list:  # function for giving random dices
    dices = []
    for number in range(amount):
        randomNumb = random.randint(1, 7)
        dices.append(randomNumb)
    return dices



